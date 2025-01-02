import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BaseLocators(object):
    LOADING_GIF = (By.XPATH, "//div[@data-automation-class='vtx-loading-indicator'] "
                             "| //div[@class='ag-overlay']//div[@class='loading-indicator'] "
                             "| //button[@data-automation-class='vtx-button'][contains(@class,'ant-btn-loading')] "
                             "| //svg[contains(@class,'lds-dual-ring')]")
    SIDE_MENU_SKELETON = (By.XPATH, "//nav[@data-testid='side-menu-skeleton']")
    SIDE_MENU = (By.XPATH, "//nav[@id='side-menu-wrapper']")
    FORM_LABEL = (By.XPATH, "//label[normalize-space(.) = '{}']")
    GRID = (By.XPATH, "//div[@role='treegrid']")
    GRID_HEADER_SORT = (By.CLASS_NAME, "ag-header-cell-sortable")
    GRID_HEADER_TEXT = (By.XPATH, ".//div[@role='columnheader']")
    BURGER_MENU = (By.XPATH, ".//span[@class='ag-icon ag-icon-menu']")
    SIDE_NAV = (By.CLASS_NAME, 'site-nav__container')
    # Single and Multi select endpoints
    MULTI_SELECT = (By.XPATH,
                    ".//div[contains(@class, 'vtx-multi-select__value-container vtx-multi-select__value-container--is-multi')]")
    SINGLE_SELECT = (By.XPATH, ".//div[contains(@class, 'vtx-select__input-container')]")
    SELECT_OPTIONS = (By.XPATH, ".//div[contains(@class, 'vtx-select__option')]")
    SPECIFIC_SINGLE_SELECT = (
        By.XPATH, ".//div[contains(@class, 'ant-select-single') and contains(@class, 'ant-select-show-arrow')]")
    SPECIFIC_SELECT_OPTIONS = (By.XPATH, ".//div[@class='ant-select-item-option-content']")


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    ####################
    #   Button Clicks  #
    ####################

    def _css_button_click(self, descriptor):
        """
        Clicks `button` type button based on descriptor

        :param descriptor:Input button name as appears in the UI
        """
        button = None
        try:
            xpath = (By.XPATH, "//*[@data-automation-class='vtx-button']//span[text() = '" + descriptor + "']/..")
            self.driver.find_element(*xpath)
            button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath))
        except NoSuchElementException:
            xpath = (By.XPATH, "//button[@type='button' and text() = '" + descriptor + "']")
            self.driver.find_element(*xpath)
            button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath))
        finally:
            assert button, f'No button found with the text {descriptor}'
            button.click()

    def _css_button_submit_click(self, descriptor):
        """
        Clicks `submit` type button based on descriptor

        :param descriptor:Input button name as appears in the UI
        """
        actionChains = ActionChains(self.driver)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']//span[text() = '" + descriptor + "']")
        if button:
            self.highlight_element(button)
            button.click()

    ########################
    #   Form Interactions  #
    ########################

    def _form_select_single(self, dropdownLabel, valueToSelect):
        """
        Locates a single form select with the given label and selects single value provided

        :param dropdownLabel: Label of dropdown as seen in UI
        :param valueToSelect: Value in dropdown to select as seen in the UI
        """

        # Find form select by label and get attribute
        # Keeping these two pieces because it ensures that the label and drop down are both present/selectable

        formattedXpath = self._format_tuple(BaseLocators.FORM_LABEL, dropdownLabel)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(formattedXpath))
        # Find form select dropdown and send keys to select option
        select_box = self.driver.find_element(By.XPATH,
                                              "//input[contains(@id,'{}-input')]".format(dropdownLabel.lower()))
        select_box.click()
        select_box.send_keys(Keys.CONTROL, 'a')
        select_box.send_keys(Keys.DELETE)
        select_box.send_keys(valueToSelect)
        select_box.send_keys(Keys.ENTER)

    def _form_select_multi(self, dropdownLabel, valueToSelect):
        """
        Locate a mutli select form give a specified label and select a value out of the option list. To select
        multiple options at this time, call the component a second time

        params:
            dropdownLabel: Label of dropdown as seen in UI
            valueToSelect: Value in dropdown to select as seen in the UI
        """
        optionBar = self.driver.find_element(*BaseLocators.MULTI_SELECT)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(optionBar))
        optionBar.click()

        try:
            optionBar.find_element(By.TAG_NAME, 'input').send_keys(valueToSelect, Keys.ENTER)
            return
        except NoSuchElementException:
            options = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'multiSelect__option')]")
            print(options)
            for option in options:
                print(option.find_elements(By.TAG_NAME, "span")[2].text.lower())
                if option.find_elements(By.TAG_NAME, "span")[2].text.lower() == valueToSelect.lower():
                    option.click()
                    break
            else:
                assert False, f"Unable to find option of {valueToSelect}"

    ####################
    #       Misc       #
    ####################

    def _format_tuple(self, tpl, formatValue):
        """
        Formats the second item in the tuple. This is used to have variable xpath.

        :param tpl: Tuple object to edit
        :param formatValue: Value to add to the format string.
        :return: Tuple object.
        """
        lst = list(tpl)
        if type(formatValue) == list:
            lst[1] = lst[1].format(*formatValue)
        else:
            lst[1] = lst[1].format(formatValue)
        return tuple(lst)

    def _validate_bool(self, value):
        """
        Will convert the given value into bool True or False. If value is not a true or false string then it will return an error.

        :param value: String 'true' or 'false'
        :return: Bool
        """
        if type(value) is bool:
            return value

        boolDict = {'true': True,
                    'false': False}

        assert value.lower() in boolDict.keys(), '{} is not a true or false string. Please enter "true" or "false".'.format(
            value)
        return boolDict[value.lower()]

    def _wait_for_loading_gif(self, isSnapshot=False):
        """
        Waits for the loading gif to go away.

        :param isSnapshot: Optional. Boolean value to wait longer for removal if it is for snapshot. Defaults to False
        :return:
        """
        appearanceTimeout = 10
        removalTimeout = 120
        if (isSnapshot):
            removalTimeout = 1800

        try:
            # `conftest.py` default always implicitly retries `presence_of_element_located` for 10s,
            # which adds unnecessary delay before a passing `until_not` check below.
            self.driver.implicitly_wait(0)
            # Wait for loading icon to go away if it is present.
            WebDriverWait(self.driver, appearanceTimeout).until(
                EC.presence_of_element_located(BaseLocators.LOADING_GIF))
            WebDriverWait(self.driver, removalTimeout).until_not(
                EC.presence_of_element_located(BaseLocators.LOADING_GIF))
        except TimeoutException:
            return
        finally:
            self.driver.implicitly_wait(10)

    def _click_hamburger_menu(self, columnName):

        """Will click the hamburger menu for the specified column in the grid"""

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(BaseLocators.GRID))
        grids = self.driver.find_elements(*BaseLocators.GRID)
        for g in grids:
            if g.is_displayed():
                grid = g
                break
        else:
            assert False, 'No visible grid was found on the page.'
        headers = grid.find_elements(*BaseLocators.GRID_HEADER_SORT)
        for header in headers:
            if columnName == header.text:
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(header).perform()
                burger = header.find_element(*BaseLocators.BURGER_MENU)
                actionChains.move_to_element(burger).perform()
                actionChains.click(burger).perform()
                break
        else:
            assert False, 'No header found with the name ' + columnName

    def _click_filter_menu(self):
        """
        Prereq: _click_hamburger_menu must be run first.
        Clicks on the filter menu within the hamburger menu for the given column.
        """
        try:
            # checks if filter tab is already selected
            if 'ag-tab-selected' in self.driver.find_element(By.XPATH,
                                                             "//div[@ref='eHeader']//span[@class='ag-icon ag-icon-filter']/..").get_attribute(
                'outerHTML'):
                pass
            else:
                filterMenu = self.driver.find_element(By.XPATH,
                                                      "//div[@ref='eHeader']//span[@class='ag-icon ag-icon-filter']")
                filterMenu.click()
        except NoSuchElementException:
            # filterMenu = self.driver.find_element(By.XPATH, "//span[@class='ag-tab ag-tab-selected']//span[@class='ag-icon ag-icon-filter']")
            pass

    def _retrieve_col_id(self, colName):
        """ Returns the col-id of specified column name in grid """

        gridCol = {
            # taxpayer grid columns
            'taxpayer': 'company',
            'taxpayer code': 'companyCode',
            'country': 'country',
            'filing jurisdictions': 'filingJurisdictions',
            'returns setup': 'returns',
            'status': 'status',
            # jurisdiction grid columns
            'jurisdiction': 'jurisdictionName',
            'state gross': 'stateGross',
            'state taxable': 'stateTaxable',
            'state deductions': 'stateDeductions',
            'states tax': 'stateTax',
            'county gross': 'countyGross',
            'county taxable': 'countyTaxable',
            'county deductions': 'countyDeductions',
            'countys tax': 'countyTax',
            'city gross': 'cityGross',
            'city taxable': 'cityTaxable',
            'city deductions': 'cityDeductions',
            'city tax': 'cityTax',
            'district gross': 'districtGross',
            'district taxable': 'districtTaxable',
            'district deductions': 'districtDeductions',
            'jurisdictions': 'jurisdiction',
            'district tax': 'districtTax',
            'locations': 'locationCount',
            'jurisdiction specific settings': 'specialJurisdictionRule',
            # Location grid columns
            'code': 'code',
            # Tax data grid columns
            'state tax': 'field-2',
            'county tax': 'field-3',
            'filing tax categories': 'field-1',
            'state tax by destination': 'field-3',
            'filing tax categories by destination': 'field-2',
            'location by destination': 'field-1',
            'location': 'field-1',
            'jurisdiction tax data': 'field-0'
        }

        if colName.lower() in gridCol:
            return gridCol[colName.lower()]
        else:
            "Column name does not exist. Enter the column name as shown exactly on UI and try again."

    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background:yellow; color: Red; border: 3px dotted solid yellow;")
        time.sleep(1)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "backgroundColor: transparent; color: Green; border: 3px dotted solid yellow;")
