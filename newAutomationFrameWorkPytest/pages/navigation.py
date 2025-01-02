import glob
import os
import shutil
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, WebDriverException, \
    ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from newAutomationFrameWorkPytest.pages.basePage import BasePage
from newAutomationFrameWorkPytest.utility.TestingUtil import TestingUtil


class NavigationLocators(object):
    # Generic Navigation NavigationLocators
    ACTION_MENU_CONTAINER = (By.XPATH, "//div[@class='action-menu--container']")
    BREADCRUMB = (By.XPATH, "//span[@class ='ant-breadcrumb-link']//a[normalize-space()='{}']")
    SETTINGS_TEXT = (By.XPATH, "//div[@class='vtx-dropdown-button']//button[@aria-label='{}']")
    SETTINGS_DROPDOWN_MENU = (By.XPATH, "//span[@class='ant-dropdown-menu-title-content']//span[contains(text(),'{}')]")
    CONFIG_TAB = (By.XPATH, "//button[@class='chakra-tabs__tab vtx-tab css-1thkgfg' and text() = '{}']")
    DATE_COL_FILTER = (By.XPATH, ".//input[@placeholder='yyyy-mm-dd']")
    FILTER_TEXT_FILTER = (By.XPATH, "//input[@placeholder='Filter...']|//input[@placeholder='yyyy-mm-dd']")
    FILTER_MENU = (By.XPATH, ".//div[@class='ag-tabs-body ag-menu-body']")
    FILTER_TEXT = (By.XPATH, ".//input[@placeholder='Filter...']")
    GRID = (By.XPATH, ".//div[@role='row']")
    GRID_CHECKBOX = (
        By.XPATH, "//div[@aria-rowindex='{}']//div[@aria-colindex='1']//input[contains(@type, 'checkbox')]//..")
    GRID_ROW = (By.XPATH, "//div[@class='ag-center-cols-container']/div[@row-index='{}']")
    GRID_ACTIONS_ROW = (By.XPATH, "//div[@class='ag-pinned-right-cols-container']/div[@row-index='{}']")
    GRID_EMPTY = (By.XPATH,
                  "//div[@data-automation-class='vtx-commonGrid']//span[contains(text(),'{}')] | //div[contains(text(),'{}')]")
    GRID_FILTER_BY_TEXT = (By.XPATH, ".//input[@data-automation-class='vtx-input']")
    LINK = (By.XPATH, "//a[contains(text(),'{}')]")
    LOGOUT = (By.XPATH, "//span[contains(text(),'Log Out')]")  # Note: This Xpath doesn't exist anymore in Dev but
    TEXT_FIELD_LABEL = (By.XPATH, "//label[normalize-space(.) = '{}']")
    # does in QA
    MODAAL_HEADER_SUBLEVEL_TITLE = (By.XPATH, "//div[@class='ant-modal-title']")
    MODAL_BUTTON = (By.XPATH, "//div[@role='dialog']//*[@data-automation-class='vtx-button']//span[text() = '{}']/..")
    MODAL_BODY = (By.XPATH, "//div[contains(@class,'ant-modal-body')]")
    ALERT_TEXT = "//div[@class='ant-alert-message']"
    PAGE_HEADER = (By.XPATH, "//h1[@data-automation-class='vtx-title']")
    SIDE_NAV_ITEM = (By.XPATH, "//child::div[@class='menu-item-inner']//*[contains(text(), '{}')]")
    SECOND_FILTER_TEXT = (By.XPATH, ".//input[@placeholder='Search...']")
    FILTER_TEXT_BOX = (By.XPATH, ".//input[@data-automation-class='vtx-input']")
    CHECKBOX = (By.XPATH, "//div[@data-automation-class='vtx-checkbox']//*//span[contains(text(),'{}')]")
    RADIO_BUTTON = (By.XPATH, "//fieldset[@data-automation-class='vtx-radio-group']//*//span[contains(text(),'{}')]")
    DATE_COL_FILTER = (By.XPATH, ".//input[@placeholder='yyyy-mm-dd']")
    FILTER_TEXT_FILTER = (By.XPATH, "//input[@placeholder='Filter...']|//input[@placeholder='yyyy-mm-dd']")
    REMOVE_SELECT_VALUE = (By.XPATH, "//div[@aria-label='Remove {}']")
    FORM_LABEL = (By.XPATH, "//label[normalize-space(.) = '{}']")
    GRID_ROW_CONTAINER = (By.CLASS_NAME, 'ag-center-cols-container')
    ALL_GRID_ROWS = (By.XPATH, ".//div[@role='row']")
    NOTIFICATION_TEXT_MESSAGE = (By.XPATH, "//div[@class='ant-notification-notice-description']")
    NOTIFICATION_SUCCESS_TEXT_MESSAGE = (
        By.XPATH, "//div[@class='ant-notification-notice-message'][contains(text(), 'Success')]/following-sibling::div")
    TOAST_MESSAGE_BOX = (By.CSS_SELECTOR, ".ant-notification.ant-notification-topRight")
    NOTIFICATION_BOX = (By.XPATH, "//div[@class='ant-notification-notice-wrapper']")
    CLEAR_SINGLE_SELECT = (
        By.XPATH, "//label[normalize-space(.) = '{}']/..//following-sibling::div//span[@aria-label='clear']")


class Navigation(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.colIndex = 0
        self.rowIndex = 0

    def launch_application(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(5)

    def get_page_title(self):
        return self.driver.title

    def __check_if_element_exists(self, search_tuple):
        try:
            self.driver.find_element(*search_tuple)
            return True
        except NoSuchElementException:
            return False

    def login(self, username=None, base_url=None, password=None):

        if username is None:
            username = os.getenv('NG_TESTER_USERNAME')
        if password is None:
            password = os.getenv('NG_PASSWORD')
        if base_url is None:
            base_url = os.getenv('NG_URL_UI')
        self.driver.get(base_url)

        try:
            self.driver.maximize_window()
            time.sleep(0.5)
        except WebDriverException:
            pass

        userNameInput = WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='username']")))
        if 'Email address' in userNameInput.get_attribute('innerHTML'):
            try:
                WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(
                    username)
                self.driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()
                WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(
                    password)
                elements = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Continue')]")
                elements[-1].click()
            except:
                print(self.driver.page_source)
                assert False, 'Login timed out'
        else:
            WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
            self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
            self.driver.find_element(By.XPATH,
                                     ".//button[contains(@data-automation-class,'vtx-button')]/span[contains(text(),'Log in')]").click()

        # wait for first gif to disappear
        self._wait_for_loading_gif()
        # wait for second gif to disappear
        self._wait_for_loading_gif()

    def select_application(self, application):
        """Selects the given application to login into from the main application page

        :param application: Name of application as it appears in the UI (Ex: Vertex Cloud VAT Compliance)"""

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='" + application + "']"))).click()

        # UI is default loading page; wait for 'loading' gif to disappear
        self._wait_for_loading_gif()

    def refresh_browser(self):
        """
        Refreshes the current browser page.

        :return: None
        """

        self.driver.refresh()

    def browser_back(self):

        """Clicks the browser back button"""

        self.driver.back()

    def minimize_browser(self):

        """Minimizes browser window"""

        self.driver.minimize_window()

    def maximize_browser(self):

        """Maximizes browser window"""

        self.driver.maximize_window()

    def switch_driver_tab(self):

        """Switches the driver focus to the next tab in browser"""

        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                print('title is ', self.driver.title)
                break

    def wait_for_loading(self, isSnapshot=False):
        """
        Waits for spinner to finish loading

        : param isSnapshot : Optional. Boolean value for waiting on sign off/snapshot (longer removal wait time).
            Defaults to False.
        : return : None
        """
        self._wait_for_loading_gif(isSnapshot)

    def scroll_bottom_of_page(self):
        """
        Scrolls down to bottom of page

        : return : None
        """
        # footer = self.driver.find_element(By.XPATH, "//footer[@data-automation-id='footer-layout-footer']")
        # self.driver.execute_script("arguments[0].scrollIntoView()", footer)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

    def scroll_middle_of_page(self):
        """
        Scrolls down to middle of page

        : return : None
        """
        self.driver.execute_script("window.scrollTo(0,(document.body.scrollHeight)/2)")
        time.sleep(1)

    def scroll_top_of_page(self):
        """
        Scrolls up to top of page

        : return : None
        """
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)

        ############################
        #   Side Menu Components   #
        ############################

    def menu_click(self, menuName, waitForLoading=True):
        """
        Clicks the desired menu item(s) from the left side navigation menu.
        Works with both a single menu item or a list of menu items. By default, waits for
        loading after the last menu item is selected.

        :param menuName:  Full menu name as appears in UI (case sensitive) or a list of them
        :param waitForLoading: Optional. Boolean value to wait for loading after last menu item selected. Defaults to True.
        :return: None
        """
        try:
            xpath = self._format_tuple(NavigationLocators.SIDE_NAV_ITEM, menuName)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath)).click()
        except NoSuchElementException:
            assert False, f'No side navigation item found with text {menuName}'
        except TimeoutException:
            assert False, f'Unable to select side navigation item with text {menuName}'

    def click_main_menu(self):
        """
        Clicks the MAIN MENU option on the nav bar when it is present
        """
        actionChains = ActionChains(self.driver)
        mainMenuBtn = self.driver.find_element(By.XPATH, "//button[@data-testid='main-menu-item']")
        actionChains.move_to_element(mainMenuBtn).perform()
        mainMenuBtn.click()

        ########################
        #   Click Components   #
        ########################

    def click_button(self, textOnButton):
        """
        Clicks a button with the specified text on the UI

        : param textOnButton : Text of button as it appears in the UI
        : return : None
        """
        try:
            self._css_button_click(textOnButton)
        except NoSuchElementException:
            assert False, textOnButton + " button not found."

    def click_link(self, linkText, linkIndex=0):
        """
        Clicks a link on the UI with the given text

        :param linkText: Text of link as it appears in the UI. Only use the first line of text if it's multilined.
        :param linkIndex: Index of the link to be clicked on starting with 0 being first link
        :return: Launches new tab in Chrome
        """
        xpath = self._format_tuple(NavigationLocators.LINK, linkText)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath))
        actionChains = ActionChains(self.driver)
        if linkIndex == 0:
            elem = self.driver.find_element(*xpath)
        else:
            elements = self.driver.find_elements(*xpath)
            elem = elements[linkIndex]
        actionChains.move_to_element(elem).perform()
        actionChains.click(elem).perform()

    def click_checkbox_button(self, checkboxText):
        """
        Clicks the checkbox button with the given text.

        :param checkboxText: The checkbox label; the text next to the checkbox.
        """

        xpath = self._format_tuple(NavigationLocators.CHECKBOX, checkboxText)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath))
        self.driver.find_element(*xpath).click()

    def click_radio_button(self, radiobuttonText):
        """
        Clicks the radio button with the given text.
        param radiobuttonText: The radiobutton label; the text next to the radiobutton.
        """

        xpath = self._format_tuple(NavigationLocators.RADIO_BUTTON, radiobuttonText)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath))
        self.driver.find_element(*xpath).click()

    def click_radio_button_using_javascript(self, radioButtonText):
        """
        This component with click on radio button using javascript
        :param radioButtonText: Label of the radio button to be used to click
        :return: None
        """
        try:
            xpath = self._format_tuple(NavigationLocators.RADIO_BUTTON, radioButtonText)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath))

            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*xpath))
        except:
            raise NoSuchElementException(f"Radio button {radioButtonText} was not found on the page.")

    def click_select_single_clear(self, dropdownLabel):
        """
        Locates a single form select with the given label and clicks clear icon
        :param dropdownLabel: Label of dropdown as seen in UI
        """

        # Find form select by label and get attribute
        # Keeping these two pieces because it ensures that the label and drop down are both present/selectable

        formattedXpath = self._format_tuple(NavigationLocators.CLEAR_SINGLE_SELECT, dropdownLabel)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(formattedXpath))
        self.driver.find_element(*formattedXpath).click()

    def get_radio_button_status(self, radiobuttonText):
        """
        Gets the radio button status with the given text, true is enabled and false is disabled.
        :param radiobuttonText: The radiobutton label; the text next to the radiobutton.
        :return : True if radio button is enabled and False if radio button is disabled
        """
        xpath = self._format_tuple(NavigationLocators.RADIO_BUTTON, radiobuttonText)
        button = self.driver.find_element(*xpath)
        parent = button.find_element(By.XPATH, '..')
        return parent.get_attribute('disabled')

    def get_radio_button_selection_status(self, radiobuttonText):
        """
        This component will check that radio button is selected or not
        :param radiobuttonText: The radiobutton label; the text next to the radiobutton.
        :return: True if radio button is selected and False if radio button is not selected
        """
        time.sleep(10)
        xpath = self._format_tuple(NavigationLocators.RADIO_BUTTON, radiobuttonText)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath))
        radioButton = self.driver.find_element(*xpath)
        input = radioButton.find_element(By.XPATH, '..')
        class_checked = str(input.get_attribute('class'))
        if class_checked.__contains__('ant-radio-wrapper-checked'):
            status = True
        else:
            status = False
        print(status)
        return status

    def click_breadcrumb(self, breadcrumbText):
        self.scroll_top_of_page()
        xpath = self._format_tuple(NavigationLocators.BREADCRUMB, breadcrumbText)
        self.driver.find_element(*xpath).click()

    def click_settings_icon(self, settingsText):
        self.scroll_top_of_page()
        xpath = self._format_tuple(NavigationLocators.SETTINGS_TEXT, settingsText)
        self.driver.find_element(*xpath).click()

        ###################
        # Grid Components #
        ###################

    def scroll_num_right_of_grid(self, columns):
        """
        Scrolls the grid horizontally a set amount of columns to the right.

        : param columns : Integer number of columns to scroll right
        : return : None
        """
        firstColumnLocator = (By.XPATH, "(//span | //div)[@role='columnheader' and @aria-colindex='2'][2]")
        firstColumnLocator1 = (By.XPATH, "(//span | //div)[@role='columnheader' and @aria-colindex='2'][1]")
        try:
            firstColumnHeader = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(firstColumnLocator))
        except:
            firstColumnHeader = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(firstColumnLocator1))
        # Select header once for focus. Then restore original sorting.
        firstColumnHeader.click()
        firstColumnHeader.click()
        firstColumnHeader.click()
        actionChains = ActionChains(self.driver)
        for i in range(columns):
            actionChains.send_keys(Keys.RIGHT)
        actionChains.perform()
        self.colIndex = 2 + columns

    def scroll_num_left_of_grid(self, columns):
        """
        Scrolls the grid horizontally a set amount of columns to the left.

        : param columns : Integer number of columns to scroll left
        : return : None
        """
        columnLocator = (By.XPATH, f"(//span | //div)[@role='columnheader' and @aria-colindex='{self.colIndex}']")
        columnHeader = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(columnLocator))
        # Select header once for focus. Then restore original sorting.
        columnHeader.click()
        columnHeader.click()
        columnHeader.click()
        actionChains = ActionChains(self.driver)
        for i in range(columns):
            actionChains.send_keys(Keys.LEFT).perform()
        self.colIndex = self.colIndex - columns

    def click_on_action_icon(self, rowValue):
        """
        Clicks on the action button on the Actions column on specified row number.
        : param rowValue :  The value of row within the grid, starting at 0
        : param columnValue : Column name value as shown in the UI
        """
        row = self._get_actions_cell_value(rowValue)
        row.click()

    def select_action(self, firstColName, firstObjName, action, secColName='', secObjName=''):
        """
        Finds the row within the grid of specified column name(s) and object name(s) within the cell. This can be used to
        search up to 2 column names and its object within the cell. Selects the specified action on the Action menu.

        : param firstColName : Name of first column used for comparison
        : param firstObjName : Text within the cell under the first column name to search
        : param action : Action type from action menu section (E.g. View)
        : param secColName : Name of the second column used for comparison. Optional; leave it as '' if not needed
        : param secObjName : Text within the cell under the second column name to search. Optional; leave it as '' if not needed
        : return : None
        """

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(NavigationLocators.GRID))

        rowContainers = self.driver.find_elements(*NavigationLocators.GRID_ROW_CONTAINER)
        for r in rowContainers:
            if r.is_displayed():
                rowContainer = r
                break
        else:
            assert False, 'No visible row containers on the screen.'
        rows = rowContainer.find_elements(*NavigationLocators.ALL_GRID_ROWS)
        for num, row in enumerate(rows):
            firstName = row.find_element(By.XPATH, ".//div[@col-id='" + self._retrieve_col_id(firstColName) + "']").text
            if secColName:
                secName = row.find_element(By.XPATH, ".//div[@col-id='" + self._retrieve_col_id(secColName) + "']").text
                if firstObjName in firstName and secObjName == secName:
                    numRow = str(num)
                    break
            else:
                if firstObjName in firstName:
                    numRow = str(num)
                    break
        else:
            if secColName:
                assert False, "Cannot find column names {} and {} with matching values of {} and {}".format(
                    firstColName, secColName, firstObjName, secObjName)
            else:
                assert False, "Cannot find column name {} with matching value of {}".format(firstColName, firstObjName)

        self._find_action_row(numRow, action)

    def click_column_header(self, columnName):
        """
        This will click the column header once if found. This can be used to sort column.
        pass in once to sort ascendeing
        pass in twice to sort descending
        pass in three times to clear sort
        :param columnName: Case sensitive header name.
        :return: None
        """

        columnToClick = self.driver.find_element(By.XPATH, f"//span[@class='ag-header-cell-text']"
                                                           f"[normalize-space()='{columnName}']")
        self.highlight_element(columnToClick)
        columnToClick.click()

    def get_grid_row_value_text(self, rowValue, columnValue):
        """Will return the text for the selected row and column value
        : param rowValue :  The value of row within the grid, starting at 0
        : param columnValue : Column name value as shown in the UI
        : param expectedValue : The expected section name value that needs to be verified
        """
        row = self._get_cell_value(rowValue, columnValue)
        actualValue = row.text
        return actualValue

    def wait_for_grid_to_load(self):
        """
        This component will verify grid is loaded on the page to perform further actions
        :return: None
        """
        try:
            gridRow = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, ".//div[@role='rowgroup']")))
        except TimeoutException:
            assert False, 'Grid is not loaded within 20 seconds'

    def edit_row_values_in_grid(self, cellValue, columnName, rowNum=-1, inputType='text'):
        """
        Edits specified value within the grid based on the row index and column name.
        : param cellValue : New value of the specified cell
        : param rowNum : Row index within the grid, starting at 0. default value is -1 and if it is -1 we need to call get_row_number_from_row_text component before this component to fill up self.rowIndex variable
        : param columnName : Name of the column as shown in the UI
        : return : None
        """
        rowCell = self._find_rowcell_using_rowNum_and_columnName(rowNum, columnName)
        self._fill_grid_cell_based_on_input_type(rowCell, inputType, cellValue)

    def select_grid_row(self, rowNumber: int):
        """
        Component to click on grid row checkbox
        Params:
            rowNumber: position of the checkbox, 0 - will select all, > 0 will select from rows
        """
        formattedXpath = self._format_tuple(NavigationLocators.GRID_CHECKBOX, rowNumber + 1)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(formattedXpath))
        self.driver.find_element(*formattedXpath).click()

        ########################
        #    Tab Components    #
        ########################

    def verify_configuration_tab(self, expectedTabText, isVisible=True):
        """
        Verifies if the tab is visible and matches with the expected tab text
        : param expectedTabText : Expected string on tab as appears in the UI
        : param isVisible : Expected tab to be visible or not; Defaults to True
        : return : None
        """
        if len(expectedTabText) == 0:
            assert False, f"No tab title of {expectedTabText} given. Please re-enter a valid tab title."
        xpath = self._format_tuple(NavigationLocators.CONFIG_TAB, expectedTabText)
        try:
            self.driver.find_element(*xpath)
        except NoSuchElementException:
            if isVisible:
                assert False, f"Tab {expectedTabText} was not found on the page."
            return
        if not isVisible:
            assert False, f"Tab {expectedTabText} was found, but was not expected."

    def select_configuration_tab(self, textOfTab):
        """
        Selects a tab in one of the configuration UIs.

        :param textOfTab: the name of the tab as it appears in the UI. Eg: Return Processing Signed-Off
        """
        tabs = ["//*[@data-automation-class='vtx-button']//span[text() = '" + textOfTab + "']",
                "//button[@type='button' and text() = '" + textOfTab + "']",
                "//*[@data-automation-class='vtx-tab' and text() = '" + textOfTab + "']"]

        for item in tabs:
            try:
                xpath = (By.XPATH, item)
                self.driver.find_element(*xpath)
                button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(xpath))
                button.click()
                break
            except NoSuchElementException:
                continue
        else:
            assert False, f'{textOfTab} tab not found.'

        ########################
        #   Select Components  #
        ########################

    def select_from_menu_dropdown(self, menuText):
        self.scroll_top_of_page()
        menuItem = self.driver.find_element(By.XPATH, f"//span[contains(text(), '{menuText}')]/ancestor::a")
        menuItem.click()

    def form_selector(self, selectType, dropdownLabel, valueToSelect):
        """
        UI component that is able to interact with both single select drop downs, and
        multi select dropdowns.
        Component leverages the two internal single select and multi select in the BasePage class
        Params:
            selectType: the type of selection you wish to use: acceptable params are "single" and "multi"
            dropdownLabel: the label of the drop-down. This is converted into the input ID for the specified dropdown
            valueToSelect: the value of the element we wish to select out of the drop down selector in the UI: Eg; 'company' or 'jurisdiction'
        """

        if selectType.lower() == 'single':
            self._form_select_single(dropdownLabel=dropdownLabel, valueToSelect=valueToSelect)
            # This short wait gives the UI time to update
            time.sleep(3)
        elif selectType.lower() == "multi":
            self._form_select_multi(dropdownLabel=dropdownLabel, valueToSelect=valueToSelect)
            # This short wait gives the UI time to update
            time.sleep(3)
        else:
            assert False, "Input Type {} does is not a valid parameter, use 'single' or 'multi'".format(selectType)

        ########################
        #   Verify Components   #
        ########################

    def verify_grid_column_header(self, text, expectedValue, isVisible=True):
        """Verifies if the column name displayed on the grid and matches with expected value
        : param expectedValue : Expected column name as appears in the UI
        : param isVisible : Expected tab to be visible or not; Defaults to True
        : return : None
        """
        try:
            columnName = self.driver.find_element(By.XPATH, f"//span[@class='ag-header-cell-text']"
                                                            f"[normalize-space()='{text}']")
            self.highlight_element(columnName)
        except NoSuchElementException:
            if isVisible:
                assert False, f"Column Name: {expectedValue} was not found on the page."
            return
        if not isVisible:
            assert False, f"Column Name: {expectedValue} was found, but was not expected."

    def verify_grid_column_main_header(self, text, expectedValue, isVisible=True) -> None:
        """Verifies if the column name displayed on the grid and matches with expected value
        : param text : text locator of the main header menu
        : param expectedValue : Expected column name as appears in the UI
        : param isVisible : Expected tab to be visible or not; Defaults to True
        : return : None
        """
        try:
            columnName = self.driver.find_element(By.XPATH, f"//span[text()='{text}' and @role='presentation']")
            self.highlight_element(columnName)
        except NoSuchElementException:
            if isVisible:
                assert False, f"Column Name: {expectedValue} was not found on the page."
            return
        if not isVisible:
            assert False, f"Column Name: {expectedValue} was found, but was not expected."

    def verify_grid_column_sub_header(self, locatorId, expectedValue, isVisible=True) -> None:
        """Verifies if the column name displayed on the grid and matches with expected value
        : param locatorId : id locator of the sub header menu
        : param expectedValue : Expected column name as appears in the UI
        : param isVisible : Expected tab to be visible or not; Defaults to True
        : return : None
        """
        try:
            columnName = self.driver.find_element(By.XPATH, f"//div[@col-id='{locatorId}']//div[@role='presentation']"
                                                            f"//div[@role='presentation']//div[@role='presentation']")
            self.highlight_element(columnName)
        except NoSuchElementException:
            if isVisible:
                assert False, f"Column Name: {expectedValue} was not found on the page."
            return
        if not isVisible:
            assert False, f"Column Name: {expectedValue} was found, but was not expected."

    def verify_column_header_order(self, columnList: str):
        """
        This component will take the list of column header as parameter and validate the same order on UI
        :param columnList: list of column header in expected order.Pass column headers separated by "|" symbol for e.g. "Jurisdiction|Tax Area ID"
        :return: None
        """
        columns = self.driver.find_elements(By.XPATH, f"//span[@class='ag-header-cell-text']")
        actualColumnList = []
        expectedColumnList = []
        for expectedColumn in columnList.split("|"):
            expectedColumnList.append(expectedColumn)
        for column in columns:
            actualColumnList.append(column.text)
        assert expectedColumnList == actualColumnList, f"Expected column order {expectedColumnList} does not match actual column order {actualColumnList}"

    def verify_grid_is_empty(self, text='No Rows To Show'):
        """
        Component to verify an AG-Grid is empty
        :param text: Expected text to show on grid when it is empty(default to No Rows To Show)
        """
        formattedXpath = self._format_tuple(NavigationLocators.GRID_EMPTY, [text, text])
        grid = self.driver.find_element(*formattedXpath)
        if not grid:
            assert False, "Grid is not empty"

    def verify_import_log_section_field_name(self, text, expectedValue, isVisible=True):
        """Verifies if the section field name displayed on the import log page and matches with expected value
        : param text : Text value to identify the section field name
        : param expectedValue : Expected column name as appears in the UI
        : param isVisible : Expected tab to be visible or not; Defaults to True
        : return : None
        """
        try:
            columnName = self.driver.find_element(By.XPATH, f"//div[@class ='vtx-space']//div["
                                                            f"@class='section-field-name'][normalize-space()='{text}']")
            self.highlight_element(columnName)
        except NoSuchElementException:
            if isVisible:
                assert False, f"Column Name: {expectedValue} was not found on the page."
            return
        if not isVisible:
            assert False, f"Column Name: {expectedValue} was found, but was not expected."

    def wait_for_import_status_change(self, importDateTime: str, maxAttempts=180):
        """Will wait for the import to complete.
        If the import has an error this will fail or if process  still is in progress and attempts reach to max count
        : param importDateTime : Unique Text value to identify that row in import grid for e.g. Jul 26, 2023, 20:34:09 ETZ
        : param maxAttempts: Optional. Denotes the number of loops to sleep for e.g. 180
        : return : None
        """
        attempts = 0
        while attempts < maxAttempts:
            try:
                self.click_button('Refresh')
                self.wait_for_loading()

                rows = self.driver.find_elements(By.XPATH, "//div[@class='ag-center-cols-container']/div[@role='row']")
                for row in rows:
                    search_column_xpath = f".//div[@col-id='importDateTime']"
                    cell = row.find_element(By.XPATH, search_column_xpath)
                    if importDateTime in cell.text:
                        target_column_xpath = f".//div[@col-id='status']"
                        target_cell = row.find_element(By.XPATH, target_column_xpath)
                        actualStatus = target_cell.text

                        if actualStatus == 'Import Done':
                            return
                        elif actualStatus == 'Import In Progress':
                            pass
                        elif actualStatus == 'Import Failed':
                            return
                        break
                attempts += 1

            except Exception as caughtException:
                assert False, caughtException

        else:
            assert False, f"'Status is in progress after {maxAttempts} attempts."

    def verify_import_log_section_field_value(self, sectionName, expectedValue, checkForEmpty=False):
        """Will map the given column number to the given mappedValue
        : param sectionName :  The section name displayed on the import log page.
        : param expectedValue : The expected section name value that needs to be verified
        : param checkForEmpty : Use for cases when the value has wrapper to show default text for empty case
        """
        followingSibling = "div"
        if checkForEmpty:
            followingSibling = "span[@class='view-value']"
        sectionValue = self.driver.find_element(By.XPATH, f"//div[@class='section-field-name'][normalize-space()="
                                                          f"'{sectionName}']/following-sibling::{followingSibling}")
        self.highlight_element(sectionValue)
        actualValue = sectionValue.text
        assert actualValue == expectedValue, "Actual value {} does not equal expected value {}".format(actualValue,
                                                                                                       expectedValue)

    def verify_column_values_mapping(self, rowValue, columnValue, expectedValue):
        """Will map the given column number to the given mappedValue
        : param rowValue :  The value of row within the grid, starting at 0
        : param columnValue : Column name value as shown in the UI
        : param expectedValue : The expected section name value that needs to be verified
        """
        row = self._get_cell_value(rowValue, columnValue)
        actualValue = row.text
        assert actualValue == expectedValue, "Actual value {} does not equal expected value {}".format(actualValue,
                                                                                                       expectedValue)

    def verify_page_header(self, expectedHeader):
        """
        Verifies the page header matches the expected page header

        :param expectedHeader: Expected string as appears in the UI
        :return: None
        """
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        content = self.driver.find_element(*NavigationLocators.PAGE_HEADER).text
        assert expectedHeader == content, "Expected and Actual header do not match. Expected: {e} Actual: {a}".format(
            e=expectedHeader, a=content)

    def verify_grid_column_value(self, columnName, expectedValue, rowNum=-1, inputType='text'):
        """
        Verifies row/column value of the first row in the grid equals expected.
        Use filter_column component prior to use to locate specific rows.

        :param columnName :  Column name as it appears in the UI (ex: Country)
        :param expectedValue : Expected value as it appears in the UI (ex: United States)
        :param rowNum : Row number of that column to validate
        :param inputType : type of the input that needs to be verified it can be any of 'text','checkbox' and 'dropdown'
        """
        colId = self._retrieve_col_id(columnName)
        if rowNum == -1:
            rowNum = self.rowIndex + 1
        if colId is not None:
            row = self.driver.find_element(By.XPATH,
                                           f"//div[@class='ag-center-cols-container']//div[@row-index='{rowNum - 1}']//div[@col-id='{colId}']")
        else:
            colName = self.driver.find_element(By.XPATH,
                                               f"//span[text()='{columnName}']/ancestor::div[@role='columnheader']").get_attribute(
                'col-id')
            row = self.driver.find_element(By.XPATH,
                                           f"//div[@class='ag-center-cols-container']//div[@row-index='{rowNum - 1}']//div[@col-id='{colName}']")
        self.highlight_element(row)
        self._verify_cellValue_using_inputType_and_gridcell(inputType, expectedValue, row)

    def verify_field_text(self, expectedTxt):
        """ Validate the fields text on the UI screen.
        : return :False when parm text not found. when find the text return :True
        """
        expectedString = str(expectedTxt)
        try:
            textLocator = (By.XPATH, "//*[text()='{}']".format(expectedString))
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(textLocator))
        except TimeoutException:
            assert False, f"Unable to find visible text {expectedString}"

    def verify_text_is_not_visible_on_page(self, expectedTxt):
        """ Validate text is not visible on the page
        : return: None
        """
        expectedString = str(expectedTxt)
        try:
            textLocator = (By.XPATH, "//*[text()='{}']".format(expectedString))
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(textLocator))
            if element:
                assert False, f'{expectedString} is visible on the page when it should not be.'
        except TimeoutException:
            pass

    def verify_field_is_disabled(self, expectedTxt):
        """
        Validate the fields with text is disabled and not interactable. This method will
        throw assertion failure if field is interactable.
        :param expectedTxt: search for the field with provided string on the page
        :return: None
        """
        expectedString = str(expectedTxt)
        textLocator = (By.XPATH, "//*[text()='{}']".format(expectedString))

        try:
            eleClass = self._get_element_class(textLocator)
            self._validate_element_disabled(eleClass, expectedString)
        except NoSuchElementException:
            assert False, f'Element with {expectedString} is not found'

    def verify_error_message(self, label: str, expectedError: str) -> None:
        """
        Verifies a UI error message for a specific form item.

        :param label: The label of the form item associated with the error message.
        :param expectedError: The expected error message to validate.
        :return: None
        """
        formatted_xpath = self._format_tuple(NavigationLocators.FORM_LABEL, label)
        try:
            labelElement = self.driver.find_element(*formatted_xpath)
            labelId = labelElement.get_attribute('for')
            # To make error message visible, simulate clicking outside the input to trigger the blur event
            labelElement.click()
            errorContainer = self.driver.find_element(By.XPATH, f"//div[@id='{labelId}_help']")
            errorMessage = errorContainer.find_element(By.CLASS_NAME, 'ant-form-item-explain-error').text

            if expectedError != errorMessage:
                assert False, f"Expected error message: '{expectedError}', but got: '{errorMessage}'"
        except NoSuchElementException:
            assert False, f"No error message found for label: '{label}'"

    def verify_text_input_is_disabled(self, inputLabel):
        """
        Add text to the form with the given input_label
        :param inputLabel: Label for text input area (is typically just above the text input area.)  Case sensitive.
        :return: None
        """

        labelXpath = self._format_tuple(NavigationLocators.TEXT_FIELD_LABEL, inputLabel)
        label = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(labelXpath))
        label_for = label.get_attribute('for')

        try:
            text_box = self.driver.find_element(By.XPATH, "//*[@name='{}']".format(label_for))
            if text_box.get_attribute('disabled'):
                pass
            else:
                assert False, f'Text box with {inputLabel} is enabled when it should not be'
        except NoSuchElementException:
            print('first exception')
            try:
                text_box = self.driver.find_element(By.XPATH, "//*[@id='{}']".format(label_for))
                if text_box.get_attribute('disabled'):
                    pass
                else:
                    assert False, f'Text box with {inputLabel} is enabled when it should not be'
            except NoSuchElementException:
                print('second exception')
                text_box = self.driver.find_element(By.XPATH,
                                                    "//label[normalize-space(.) = '{}']/following-sibling::textarea".format(
                                                        inputLabel))
                if text_box.get_attribute('disabled'):
                    pass
                else:
                    assert False, f'Text box with {inputLabel} is enabled when it should not be'

    def verify_button_disabled(self, buttonTxt):
        """
        Verifies the given button is present but disabled
        : param buttonTxt : Expected string on button as appears in the UI
        """

        button = self.driver.find_element(By.XPATH,
                                          "//button[@type='button']//span[text() = '{}']/..".format(buttonTxt))
        disabled = button.get_attribute('disabled')
        if disabled == 'true':
            pass
        else:
            assert False, "{} button is not disabled as expected.".format(buttonTxt)

    def verify_button_enabled(self, buttonTxt: str):
        """
        Verifies the given button is present and enabled
        : param buttonTxt : Expected string on button as appears in the UI
        """

        button = self.driver.find_element(By.XPATH,
                                          "//button[@type='button']//span[text() = '{}']/..".format(buttonTxt))
        enabled = button.get_attribute('disabled')
        if enabled is None or enabled != 'true':
            pass
        else:
            assert False, "{} button is not enabled as expected.".format(buttonTxt)

    def verify_element_is_invisible(self, element):
        """
        This component will verify element is visible or not
        :param element: Web Element that needs to validated as invisible. Take the web element using _get_element_using_locator
        :return: None
        """
        try:
            if element.is_displayed():
                assert False, f'Element {element} is visible when it should not be'
        except StaleElementReferenceException or NoSuchElementException:
            pass

    def verify_toast_message(self, msgText):
        """
        This component will verify the message shown in the toast message whether it is success message or failure message
        :param msgText: Text to be verified
        :return: None
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(NavigationLocators.NOTIFICATION_TEXT_MESSAGE))
            text = element.text
            assert text == msgText, f'Actual message {text} is not matching with expected message {msgText}'
        except TimeoutException:
            assert False, 'Toast Message not found'

    def verify_success_toast_message(self, msgText: str) -> None:
        """
        This component will verify the text shown in the success popup
        :param msgText: Text to be verified
        :return: None
        """
        try:
            element = WebDriverWait(self.driver, 40).until(
                EC.visibility_of_element_located(NavigationLocators.NOTIFICATION_SUCCESS_TEXT_MESSAGE))
            text = element.text
            assert text == msgText, f"Actual message '{text}' is not matching with expected message '{msgText}'"
        except TimeoutException:
            assert False, "Toast Message not found"

    def verify_toast_message_does_not_appear(self, msgText):
        """
        This component will verify toast message did not appear with the message that is provided in the parameter
        :param msgText: Text to be verified
        :return: None
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f'//div[text()="{msgText}"]')))
            if element:
                assert False, f'Toast message with text {msgText} is visible when it should not be.'
        except TimeoutException:
            pass

    def verify_checkbox_selected(self, checkboxText):
        """
        This component will return the selection status of the checkbox
        :param checkboxText: The checkbox label; the text next to the checkbox.
        :return: True if checkbox is selected and False if checkbox is not selected
        """

        xpath = self._format_tuple(NavigationLocators.CHECKBOX, checkboxText)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath))
        return self.driver.find_element(*xpath).is_selected()

    def verify_checkbox_is_selected(self, checkboxText, expectedValue: bool):
        """
        This component will verifies the selection status of the checkbox
        :param checkboxText: The checkbox label; the text next to the checkbox.
        :param expectedValue: expected value of the checkbox boolean
        :return: True if checkbox is selected and False if checkbox is not selected
        """

        xpath = self._format_tuple(NavigationLocators.CHECKBOX, checkboxText)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(xpath))
        result = self.driver.find_element(*xpath).is_selected()
        assert expectedValue == result, f"The {checkboxText} selection is {result}"

    def verify_field_level_validation_message_text(self, inputLabel, validationText, fieldIndex=0):
        """
        This component will check the validation message for text field.
        :param inputLabel: Text filed to be validated for e.g. FEIN Number
        :param validationText: Expected validation message that is shown on UI
        :param fieldIndex : We have added this index for multiple fields with same input label on the form. The default index is 0 for one element and should go on for multiple elements
        :return: None
        """
        labelXpath = self._format_tuple(NavigationLocators.TEXT_FIELD_LABEL, inputLabel)
        if fieldIndex > 0:
            fields = self.driver.find_elements(*labelXpath)
            label = fields[fieldIndex]
        else:
            label = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(labelXpath))
        label_for = label.get_attribute('for')
        try:
            text_box = self.driver.find_element(By.XPATH, f'//div[@id="{label_for}_help"]/div')
            actualText = text_box.text
            assert actualText == validationText, f'Error message {actualText} is not equal to {validationText}'
        except (AssertionError, NoSuchElementException):
            text_box = self.get_textbox_through_inputLabel_for(inputLabel)
            actualText = self._get_field_level_error_message(textbox=text_box)
            assert actualText == validationText, f'Error message {actualText} is not equal to {validationText}'

    def verify_downloaded_export_to_excel_file(self):
        """
        Verifies the export to excel/csv file
        """
        if os.name == 'nt':
            currentPath = str(Path.home()) + "\\Downloads\\Returns - Active.csv"
            destinationPath = "C:\\test\\_data"
            self._move_file(currentPath, destinationPath)
        downloaded_files_path = self._get_downloaded_files_path()
        latest_file = self._get_latest_csv_file(downloaded_files_path)
        assert os.path.exists(latest_file), f"File did not downloaded successfully"

        ########################
        #   Modaal Components   #
        ########################

    def verify_modaal_header_sublevel_title(self, expectedHeader):
        """ Verifies the page header matches the expected page header.
        :param expectedHeader: Expected string as appears in the UI
        :return: None """
        try:
            header_ele = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(NavigationLocators.MODAAL_HEADER_SUBLEVEL_TITLE))
            header_ele.is_displayed()
            self.highlight_element(header_ele)
            print("SessionHeader:" + header_ele.text)
        except (NoSuchElementException, TimeoutException):
            assert False, "Could not find Modaal Header"
        assert header_ele.text == expectedHeader, 'Error: Modaal header title not matching....'

    def verify_modal_body_text(self, expectedText):
        """
        Verifies actual modal body text equals expected
        :param expectedText: Expected text string as it appears in the UI
        :return: None
        """

        body = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(NavigationLocators.MODAL_BODY))

        assert expectedText in body.text, "The actual modal text: {} ,did not match the expected text: {}".format(
            body.text, expectedText)

    def click_modal_button(self, textOnButton: str):
        """
        Clicks a button with the specified text inside the modal
        :param textOnButton : Text of button as it appears in the modal
        :return : None
        """

        try:
            formattedXpath = self._format_tuple(NavigationLocators.MODAL_BUTTON, textOnButton)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(formattedXpath))
            self.driver.find_element(*formattedXpath).click()
        except NoSuchElementException:
            assert False, textOnButton + " button not found in modal."

    def verify_signed_in_user_details(self, expectedValue, isVisible=True):
        """Verifies if the signed in user detail is visible and matches with the expected value
        : param expectedValue : Expected signed in user details as appears in the UI
        : param isVisible : Expected tab to be visible or not; Defaults to True
        : return : None
        """
        try:
            signedInUser = self.driver.find_element(By.XPATH, "//div[@class='client-switcher-dropdown']")
            self.highlight_element(signedInUser)
        except NoSuchElementException:
            if isVisible:
                assert False, f"Tab {expectedValue} was not found on the page."
            return
        if not isVisible:
            assert False, f"Tab {expectedValue} was found, but was not expected."

        ########################
        #   Misc Components    #
        ########################

    def title(self):
        return self.driver.title

    def click_on_body(self):
        """
        Clicks on the body of the current page

        : param : None
        """
        self.driver.find_element(By.XPATH, "//div[@data-testid='client-switcher-label']").click()

    def click_and_download_rejection_file(self, importFileName, columnValue, reportDownloaded=''):
        """ Clicks and downloads the rejection file from the table displayed on the UI grid
        : param importFileName : name of the unique file displayed on the Import History page.
        : param columnValue : grid column value name
        """
        gridRecordLink = self.driver.find_element(By.XPATH, "//div[normalize-space()='" + importFileName + "']"
                                                                                                           "//following-sibling::div[@col-id='" + columnValue + "']")
        gridRecordLink.click()
        self._wait_for_loading_gif()
        list_of_files = glob.glob(TestingUtil()._get_baseline_relative_path() + 'Downloaded_Rejection_File' +
                                  reportDownloaded)
        # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file.split('\\')[-1])
        if reportDownloaded != '':
            path = Path(TestingUtil()._get_relative_path()) / 'Downloaded_Rejection_File' / reportDownloaded
            if os.path.isfile(path) and reportDownloaded == latest_file.split('\\')[-1]:
                print('Download successful')
            else:
                assert False, ("Report did not download")

    def click_rejection_file_link(self, linkText, reportDownloaded=''):
        rejectionLink = self.driver.find_element(By.LINK_TEXT, linkText)
        rejectionLink.click()
        self._wait_for_loading_gif()
        list_of_files = glob.glob(TestingUtil()._get_baseline_relative_path() + 'Downloaded_Rejection_File' +
                                  reportDownloaded)
        # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file.split('\\')[-1])
        if reportDownloaded != '':
            path = Path(os.path.dirname(os.path.realpath(__file__))) / 'Downloaded_Rejection_File' / reportDownloaded
            if os.path.isfile(path) and reportDownloaded == latest_file.split('\\')[-1]:
                print('Download successful')
            else:
                assert False, ("Report did not download")

    def select_actions_menu_item(self, text):
        """
        Selects the value from the actions menu item once user clicked on the action icon
        : param text :  The text value that need to be selected
        """
        time.sleep(1)
        actions_menu_item = self.driver.find_element(By.XPATH,
                                                     f"//span[@class='ant-dropdown-menu-title-content' and text()='{text}']")
        actions_menu_item.click()

    def highlight_element(self, element):
        """ this will highlight the web element on the UI.
        :param: element: web element
        :author: VertexUserTouhidul"""
        # ele = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background:yellow; color: Red; border: 3px dotted solid yellow;")
        time.sleep(1)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "backgroundColor: transparent; color: Green; border: 3px dotted solid yellow;")

    def _get_cell_value(self, rowValue, columnValue):
        """ internal component that uses the row index and column name to fetch the desired cell. """

        # retrieves the proper grid information
        grid = self.driver.find_element(*NavigationLocators.GRID)
        # finds the row index
        xpath = self._format_tuple(NavigationLocators.GRID_ROW, int(rowValue))
        row = grid.find_element(*xpath)
        # retrieves the column name
        rowData = row.find_element(By.XPATH, ".//div[@col-id='" + columnValue + "']")
        return rowData

    def _get_actions_cell_value(self, rowValue):
        """ internal component that uses the row index and column name to fetch the action cell. """

        # retrieves the proper grid information

        rowData = self.driver.find_element(By.XPATH, "//div[@row-index='" + str(
            rowValue) + "']//div[@data-automation-class='vtx-dropdown-button']")
        return rowData

    def _get_textbox_by_name(self, label_for):
        '''
        Internal component to get text box by name
        :param label_for: pass the label for which text box needs to be searched
        :return: None
        '''
        try:
            text_box = self.driver.find_element(By.XPATH, "//*[@name='{}']".format(label_for))
            return text_box
        except NoSuchElementException:
            return False

    def _get_textbox_by_id(self, label_for):
        '''
        Internal component to get text box by name
        :param label_for: pass the label for which text box needs to be searched
        :return: None
        '''
        try:
            text_box = self.driver.find_element(By.XPATH, "//*[@id='{}']".format(label_for))
            return text_box
        except NoSuchElementException:
            return NoSuchElementException

    def _get_textbox_by_xpath(self, inputLabel):
        '''
        Internal component to get text box by name
        :param inputLabel: pass the label for which text box needs to be searched
        :return: None
        '''
        try:
            text_box = self.driver.find_element(By.XPATH,
                                                "//label[normalize-space(.) = '{}']/following-sibling::textarea".format(
                                                    inputLabel))
            return text_box
        except NoSuchElementException:
            return NoSuchElementException

    def get_textbox_through_inputLabel_for(self, inputLabel):
        labelXpath = self._format_tuple(NavigationLocators.TEXT_FIELD_LABEL, inputLabel)
        label = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(labelXpath))
        label_for = label.get_attribute('for')
        try:
            text_box = self._get_textbox_by_name(label_for)
            if not text_box:
                text_box = self._get_textbox_by_id(label_for)
                if not text_box:
                    text_box = self._get_textbox_by_xpath(inputLabel)
                    if not text_box:
                        raise NoSuchElementException
        except:
            raise NoSuchElementException
        return text_box

    def _get_field_level_error_message(self, textbox):
        try:
            describedBy = textbox.get_attribute('aria-describedby')
            actualText = self.driver.find_element(By.CSS_SELECTOR,
                                                  f'#{describedBy} .ant-form-item-explain-error').text
            return actualText
        except NoSuchElementException:
            raise NoSuchElementException

    def filter_column(self, columnName, filterText, uncheckSelectAll=False, isDate=False):
        """
        Selects the grid filter menu for the given column and filter type and enters text provided

        params:
            columnName: Name of column as it appears in the UI
            filterText: Text to enter in filter text box or option to select from drop-down list
            uncheckSelectAll : Optional. Boolean value to uncheck SelectAll checkbox in filter. Default value is False.
                To uncheck the SelectAll checkbox give value as True.
            isDate : Optional. Boolean value if the filtering is for dates. Defaults to False.
        """

        self._click_hamburger_menu(columnName)
        self._click_filter_menu()
        # Clear text box
        menuBox = self.driver.find_element(*NavigationLocators.FILTER_MENU)

        if not isDate:
            # text filter options
            try:
                filterBox = menuBox.find_element(*NavigationLocators.FILTER_TEXT)
            except NoSuchElementException:
                try:
                    filterBox = menuBox.find_element(*NavigationLocators.SECOND_FILTER_TEXT)
                except NoSuchElementException:
                    filterBox = menuBox.find_element(*NavigationLocators.FILTER_TEXT_BOX)
        else:
            # date options
            try:
                filterBox = menuBox.find_element(*NavigationLocators.DATE_COL_FILTER)
            except NoSuchElementException:
                filterBox = menuBox.find_element(*NavigationLocators.FILTER_TEXT_FILTER)

        # clear out text field first and send text
        time.sleep(0.5)
        filterBox.click()
        filterBox.send_keys(Keys.CONTROL + "a")
        filterBox.send_keys(Keys.DELETE)

        # for Select All checkbox
        if uncheckSelectAll:
            selectAll = self.driver.find_element(By.XPATH, "//div[text()= '(Select All)']")
            selectAll.click()

        filterBox.send_keys(filterText)

        # for other checkbox selections
        if self._check_if_col_have_checkbox(columnName):
            filterBox.send_keys(Keys.ENTER)

        # Close filter
        filterBox.send_keys(Keys.ESCAPE)

    def filter_column_by_text(self, columnName: str, filterText: str):
        """
        Selects the grid text filter menu for the given column and filter type and enters text provided
        :param columnName: Name of column as it appears in the UI
        :param filterText: Text to enter in filter text box or option to select from drop-down list
        """

        self._click_hamburger_menu(columnName)
        self._click_filter_menu()
        # Clear text box
        menuBox = self.driver.find_element(*NavigationLocators.FILTER_MENU)
        filterBox = menuBox.find_element(*NavigationLocators.GRID_FILTER_BY_TEXT)

        # clear out text field first and send text
        time.sleep(0.5)
        filterBox.click()
        filterBox.send_keys(Keys.CONTROL + "a")
        filterBox.send_keys(Keys.DELETE)

        filterBox.send_keys(filterText)

        # Close filter
        filterBox.send_keys(Keys.ESCAPE)

    def remove_page_filter_element(self, valueToRemove: str) -> None:
        """
        Removes the selected value from a multi-select dropdown.
        :param valueToRemove: The value in the dropdown to be removed, as seen in the UI.
        :return: None
        """
        formattedXpath = self._format_tuple(NavigationLocators.REMOVE_SELECT_VALUE, valueToRemove)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(formattedXpath))
        self.driver.find_element(*formattedXpath).click()

    def _check_if_col_have_checkbox(self, columnName):
        """ Internal component that returns a boolean if column name has checkbox filters """

        colWithCheckboxes = ['filing jurisdictions', 'returns setup',
                             'country', 'taxpayer', 'taxpayer code',
                             'jurisdiction', 'import file']

        if columnName.lower() in colWithCheckboxes:
            return True
        else:
            return False

    def run_more_actions(self, action):
        """
        : param action: menu item to run (Ex: Export To Excel)"""

        try:
            option = self.driver.find_element(By.XPATH, f"//span[contains(text(), '{action}')]")
        except NoSuchElementException:
            raise AssertionError(f"Option with Text {action}")
        WebDriverWait(self.driver, 30).until(EC.visibility_of(option))
        option.click()

    def get_client_secret(self):
        clientSecret = self.driver.find_element(By.XPATH, "//span[@data-testid='credential-table-secret']")
        self.highlight_element(clientSecret)
        secretText = clientSecret.text
        return secretText

    def _find_action_row(self, numRow, action):
        """ Finds the action row and clicks on the specified button """

        actionCols = self.driver.find_elements(By.XPATH, "//div[@class='ag-pinned-right-cols-container']")
        for a in actionCols:
            if a.is_displayed():
                actionCol = a
                break
        else:
            assert False, 'No visible actions column on the page.'
        row = actionCol.find_element(By.XPATH, ".//div[@row-index='" + numRow + "']")
        row.find_element(By.XPATH, ".//div[@data-automation-class='vtx-dropdown-button']").click()
        self.wait_for_loading()
        self.driver.find_element(By.XPATH,
                                 f"//span[@class='ant-dropdown-menu-title-content' and text()='{action}']").click()

    def form_text_input(self, inputLabel, inputText):
        """
        Add text to the form with the given input_label
        :param inputLabel: Label for text input area (is typically just above the text input area.)  Case sensitive.
        :param inputText:  Text value to enter into the input field.
        :return: None
        """

        labelXpath = self._format_tuple(NavigationLocators.TEXT_FIELD_LABEL, inputLabel)
        label = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(labelXpath))
        label_for = label.get_attribute('for')

        try:
            text_box = self.driver.find_element(By.XPATH, "//*[@name='{}']".format(label_for))
            text_box.send_keys(Keys.CONTROL, 'a')
            text_box.send_keys(Keys.DELETE)
            text_box.send_keys(inputText)
        except NoSuchElementException:
            print('first exception')
            try:
                text_box = self.driver.find_element(By.XPATH, "//*[@id='{}']".format(label_for))
                text_box.send_keys(Keys.CONTROL, 'a')
                text_box.send_keys(Keys.DELETE)
                text_box.send_keys(inputText)
            except NoSuchElementException:
                print('second exception')
                text_box = self.driver.find_element(By.XPATH,
                                                    "//label[normalize-space(.) = '{}']/following-sibling::textarea".format(
                                                        inputLabel))
                text_box.send_keys(Keys.CONTROL, 'a')
                text_box.send_keys(Keys.DELETE)
                text_box.send_keys(inputText)

    def text_filed_input(self, inputLabel, inputText):
        try:
            text_box = self.driver.find_element(By.XPATH, "//label[normalize-space(.) = 'Client Secret']/../..//input"
                                                .format(inputLabel))
            time.sleep(5)
            text_box.send_keys(Keys.CONTROL, 'a')
            text_box.send_keys(Keys.DELETE)
            text_box.send_keys(inputText)
        except NoSuchElementException:
            print('Element not found exception')

    def get_element_using_locator(self, locatorValue):
        """
        This component would find the element and return the same
        :param locatorValue:  Pass the locator value directly as written in NavigationLocators. Including locator Type and locator Value
        :return: Web Element
        """
        try:
            xpath = self._format_tuple(locatorValue, '')
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath))
            return element
        except TimeoutException:
            assert False, f'Unable to fine element with locator {locatorValue} '

    def clear_text_box(self, inputLabel):
        '''
        This method will be used to clear any existing text in the text box
        :param inputLabel: Label for text input area (is typically just above the text input area.)  Case sensitive.
        :return: None
        '''
        labelXpath = self._format_tuple(NavigationLocators.TEXT_FIELD_LABEL, inputLabel)
        label = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(labelXpath))
        label_for = label.get_attribute('for')

        try:
            text_box = self.driver.find_element(By.XPATH, "//*[@name='{}']".format(label_for))

            text_box.send_keys(Keys.CONTROL, 'a')
            text_box.send_keys(Keys.DELETE)
        except NoSuchElementException:
            print('first exception')
            try:
                text_box = self.driver.find_element(By.XPATH, "//*[@id='{}']".format(label_for))
                text_box.send_keys(Keys.CONTROL, 'a')
                text_box.send_keys(Keys.DELETE)
            except NoSuchElementException:
                print('second exception')
                text_box = self.driver.find_element(By.XPATH,
                                                    "//label[normalize-space(.) = '{}']/following-sibling::textarea".format(
                                                        inputLabel))
                text_box.send_keys(Keys.CONTROL, 'a')
                text_box.send_keys(Keys.DELETE)

    def get_text_from_textbox(self, inputLabel):
        '''
        This method will be used to clear any existing text in the text box
        :param inputLabel: Label for text input area (is typically just above the text input area.)  Case sensitive.
        :return: Text of the text
        '''
        labelXpath = self._format_tuple(NavigationLocators.TEXT_FIELD_LABEL, inputLabel)
        label = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(labelXpath))
        label_for = label.get_attribute('for')

        try:
            text_box = self.driver.find_element(By.XPATH, "//*[@name='{}']".format(label_for))

        except NoSuchElementException:
            print('first exception')
            try:
                text_box = self.driver.find_element(By.XPATH, "//*[@id='{}']".format(label_for))

            except NoSuchElementException:
                print('second exception')
                text_box = self.driver.find_element(By.XPATH,
                                                    "//label[normalize-space(.) = '{}']/following-sibling::textarea".format(
                                                        inputLabel))
        try:
            return text_box.get_attribute('value')
        except NoSuchElementException:
            assert False, f'text box with label {inputLabel} not found on the page.'

    def wait_for_toast_message_to_disappear(self):
        """
        Waits for the toast message to go away.

        :return:
        """

        appearanceTimeout = 10
        removalTimeout = 20
        try:
            self.driver.implicitly_wait(0)
            # Wait for toast message to disappear.
            WebDriverWait(self.driver, appearanceTimeout).until(
                EC.presence_of_element_located(NavigationLocators.TOAST_MESSAGE_BOX))
            WebDriverWait(self.driver, removalTimeout).until_not(
                EC.presence_of_element_located(NavigationLocators.TOAST_MESSAGE_BOX))
        except TimeoutException:
            return
        finally:
            self.driver.implicitly_wait(10)

    def close_notification_message(self):
        """
        This component will close the notification message.
        :return: None
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(NavigationLocators.TOAST_MESSAGE_BOX))
            notification = self.driver.find_element(*NavigationLocators.TOAST_MESSAGE_BOX)
            notification.find_element(By.XPATH, ".//span[@class='ant-notification-notice-close-x']//parent::a").click()
        except NoSuchElementException:
            pass

    def close_all_notification_messages(self):
        """
        This component will all close the notification message.
        :return: None
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(NavigationLocators.NOTIFICATION_BOX))
            notifications = self.driver.find_elements(*NavigationLocators.NOTIFICATION_BOX)
            for notification in notifications:
                notification.find_element(By.XPATH,
                                          ".//span[@class='ant-notification-notice-close-x']//parent::a").click()
        except NoSuchElementException or ElementClickInterceptedException:
            pass

    def _get_element_class(self, locator):
        """Get the class attribute of the element identified by the locator"""
        element = self.driver.find_element(*locator)
        return element.get_attribute('class')

    def _validate_element_disabled(self, eleClass, expectedString):
        """Check if the element with the given class is disabled"""
        if str(eleClass).__contains__('section-field-name') or str(eleClass).__contains__('view-value') or \
                str(eleClass).__contains__(''):
            pass
        else:
            assert False, f'{expectedString} is enabled when it should not be.'

    def get_row_number_from_row_text(self, rowText, columnName):
        """
        This component will give the rowIndex for the rowText and column name as passed in the parameter
        :param rowText: pass text to find the row number from the grid for e.g. location code or company code
        :param columnName: Column name under which row text should be searched for e.g. code column
        :return: None
        """
        self.rowIndex = 0
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, ".//div[@role='gridcell' and @col-id='{}']".format(columnName))))
        rows = self.driver.find_elements(By.XPATH, ".//div[@role='gridcell' and @col-id='{}']".format(columnName))
        for row in rows:
            if row.text == rowText:
                break
            self.rowIndex += 1

    def _find_rowcell_using_rowNum_and_columnName(self, rowNum=-1, columnName=''):
        """
        This internal component will be used to return rowCell based on the row number and column name
        :param rowNum: default value is -1 and if it is -1 we need to call get_row_number_from_row_text component before this component to fill up self.rowIndex variable
        :param columnName: Name of the column or column header text to fetch the intersection of the column and row index
        :return: return grid cell as web element
        """
        grid = self.driver.find_element(*NavigationLocators.GRID)
        xpath = self._xpath_for_row(rowNum)
        row = grid.find_element(*xpath)
        colName = self._get_colid_from_colname(columnName)
        self.verify_grid_column_header(columnName, columnName)

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, f".//div[@col-id='{colName}']")))
            rowCell = row.find_element(By.XPATH, f".//div[@col-id='{colName}']")
        except StaleElementReferenceException:
            raise StaleElementReferenceException
        return rowCell

    def _get_input_element_by_label(self, label: str) -> WebElement:
        """
        The internal component to get the input element based on the label.

        :param label: Form item label name
        :return: label associated input element
        """
        formattedXpath = self._format_tuple(NavigationLocators.FORM_LABEL, label)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(formattedXpath))
        label = self.driver.find_element(*formattedXpath)
        labelID = label.get_attribute('for')
        # Find form select dropdown and send keys to select option after clearing the forms contents
        selectBox = self.driver.find_element(By.XPATH, "//input[@id='{}']".format(labelID))
        return selectBox

    def _fill_grid_cell_based_on_input_type(self, rowCell, inputType, cellValue):
        """
        This internal component will fill up the grid cell based on cell provided and input value and text provided
        :param rowCell: grid cell to be passed as an element
        :param inputType: input type can be only 'text','checkbox' and 'dropdown'
        :param cellValue: pass the text when input type is text, pass 'true' or 'false' as text when input type is checkbox and pass the text visible in dropdown and needs th be selected
        :return: None
        """

        if inputType.lower() == 'text':
            self._fill_grid_textbox(rowCell, cellValue)
        elif inputType.lower() == 'dropdown':
            self._select_grid_cell_dropdown(rowCell, cellValue)
        elif inputType.lower() == 'checkbox':
            self._check_uncheck_grid_cell_checkbox(rowCell, cellValue)
        else:
            assert False, 'Allowed value for inputType is only text,checkbox or dropdown'

    def _verify_cellValue_using_inputType_and_gridcell(self, inputType, expectedValue, gridCell):
        """
        This Internal component will use the gridcell provided and validate the value is matching the expected value
        :param inputType: this can be only 'text' and 'checkbox'
        :param expectedValue: This needs to be expected text in the grid cell and 'true' or 'false' to validate checkbox status
        :param gridCell: cell to be validated
        :return: None
        """
        actualValue = ''
        if inputType == 'checkbox':
            try:
                cl = gridCell.find_element(By.XPATH, ".//span[contains(@class, 'vtx-icon-check')]").get_attribute(
                    'class')
                if str(cl).__contains__('check'):
                    actualValue = 'true'
            except NoSuchElementException:
                actualValue = 'false'
        else:
            actualValue = gridCell.text
        assert actualValue == expectedValue, "Actual value {} does not equal expected value {}".format(actualValue,
                                                                                                       expectedValue)

    def _xpath_for_row(self, rowNum):
        if rowNum == -1:
            xpath = self._format_tuple(NavigationLocators.GRID_ROW, int(self.rowIndex))
        else:
            xpath = self._format_tuple(NavigationLocators.GRID_ROW, int(rowNum))
        return xpath

    def _get_colid_from_colname(self, columnName):
        colName = self.driver.find_element(By.XPATH,
                                           f"//span[text()='{columnName}']/ancestor::div[@role='columnheader']").get_attribute(
            'col-id')
        return colName

    def _fill_grid_textbox(self, rowCell, cellValue):
        actionChains = ActionChains(self.driver)
        actionChains.click(rowCell).perform()
        cellBox = rowCell.find_element(By.TAG_NAME, 'input')
        actionChains.double_click(cellBox).perform()
        cellBox.send_keys(Keys.BACKSPACE)
        cellBox.clear()
        cellBox.send_keys(cellValue)
        cellBox.send_keys(Keys.ENTER)

    def _select_grid_cell_dropdown(self, rowCell, cellValue):
        actionChains = ActionChains(self.driver)
        actionChains.click(rowCell).perform()
        rowCell.send_keys(cellValue)
        dropdownValue = self.driver.find_element(By.XPATH, f"//span[text()='{cellValue}']")
        actionChains.scroll_to_element(dropdownValue).perform()
        actionChains.click(dropdownValue).perform()

    def _check_uncheck_grid_cell_checkbox(self, rowCell, cellValue):
        checkbox = rowCell.find_element(By.XPATH, './/span')
        cl = checkbox.get_attribute('class')
        if cellValue == 'true':
            if cl == 'ant-checkbox ant-checkbox-checked':
                pass
            else:
                checkbox.click()
        elif cellValue == 'false':
            if cl == 'ant-checkbox ant-checkbox-checked':
                checkbox.click()
            else:
                pass
        else:
            assert False, 'Accepted cell value parameter for input type check box is either true or false'

    def _get_downloaded_files_path(self):
        """
        Returns the path to the directory where downloaded files are stored
        """
        return TestingUtil()._get_jenkins_downloaded_path()

    def _get_latest_csv_file(self, directory):
        """
        Returns the path to the latest file in the specified directory with csv file
        """
        list_of_files = glob.glob(directory + '/*.csv')
        return max(list_of_files, key=os.path.getctime)

    def _move_file(self, currentPath, destinationPath):
        """
        Move file from current path to destination path
        """
        shutil.move(currentPath, destinationPath)
