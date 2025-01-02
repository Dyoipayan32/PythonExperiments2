import pdb
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session")
def driver_setup(request):
    path_to_chromedriver_exe = r"C:\Users\Dwaipayan_Das\ChromeBrowserAutomation\chrome-win64\chromedriver64\chromedriver.exe"
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:51134")
    # driver = webdriver.Chrome(service=ChromeService(executable_path=path_to_chromedriver_exe,
    #                                                 chrome_options=chrome_options))
    driver = webdriver.Chrome(service=ChromeService(executable_path=path_to_chromedriver_exe))
    driver.maximize_window()
    yield driver
    if request.node.session.config.pluginmanager.get_plugin('terminalreporter').stats.get("failed") is None:
        driver.quit()


def t_launch_fb_page01(driver_setup):
    driver = driver_setup
    api_url = "http://www.facebook.com"
    driver.get(api_url)
    driver.find_element(By.NAME, "email").send_keys("dwaipayandasi10@gmail.com")
    original_session_id = driver.session_id
    print("Session ID 1:", original_session_id)
    driver.find_element(By.NAME, "email").clear()
    original_session_id = driver.session_id
    print("Session ID 1:", original_session_id)


def t_common_keys_function02(driver_setup):
    driver = driver_setup
    api_url = "http://www.google.co.in"
    driver.get(api_url)
    searchBox = driver.find_element(By.XPATH, "//*[@title='Search']")
    searchBox.send_keys("Gemini ai")
    searchBox.send_keys(Keys.DOWN)
    searchBox.send_keys(Keys.DOWN)
    searchBox.send_keys(Keys.ENTER)
    time.sleep(3)

    elements = driver.execute_script("return document.querySelectorAll('h3>a');")
    # Interact with the first element
    # driver.execute_script("arguments[0].click();", elements[3])

    action = ActionChains(driver)
    for element in elements:
        if 'Gemini app on iOS and Android' in element.text:
            print(element.text)
            action.move_to_element(element).perform()
            action.send_keys_to_element()
            driver.execute_script("arguments[0].style.border='3px solid yellow'", element)
            time.sleep(2)
            driver.execute_script("arguments[0].style.border='3px solid green'", element)
            element.click()

            break

    time.sleep(3)


def test_window_switch03(driver_setup):
    driver = driver_setup
    api_url = "http://www.google.co.in"
    driver.get(api_url)
    searchBox = driver.find_element(By.XPATH, "//*[@title='Search']")
    searchBox.send_keys("Gemini ai")
    searchBox.send_keys(Keys.DOWN)
    searchBox.send_keys(Keys.DOWN)
    searchBox.send_keys(Keys.ENTER)
    time.sleep(3)

    elements = driver.execute_script("return document.querySelectorAll('h3>a');")
    getPageLink = elements[0].get_attribute('href')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(getPageLink)
    # Interact with the first element
    # driver.execute_script("arguments[0].click();", elements[3])

    action = ActionChains(driver)
    signIn = driver.find_element(By.XPATH,".//span[contains(text(), 'Sign in')]/parent::a")
    bodyElement = driver.find_element(By.XPATH, ".//*[@class='carousel-container']")
    action.context_click(bodyElement).perform()
    for element in elements:
        if 'Gemini app on iOS and Android' in element.text:
            print(element.text)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("arguments[0].style.border='3px solid yellow'", element)
            action.move_to_element(element).context_click(element).pause(10).perform()
            driver.execute_script("arguments[0].style.border='3px solid green'", element)
            element.click()

            break

    time.sleep(3)
