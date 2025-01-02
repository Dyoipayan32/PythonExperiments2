import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib3.util import Timeout

timeout = Timeout(connect=10)


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("http://www.google.com")


def test01():
    chrome_options = Options()
    # path_to_binary_chrome = r"C:\Users\Dwaipayan_Das\ChromeBrowserAutomation\chrome-win64\chrome.exe"
    # chrome_options.binary_location = path_to_binary_chrome
    # print(path_to_binary_chrome)
    path_to_chromedriver_exe = r"C:\Users\Dwaipayan_Das\ChromeBrowserAutomation\chrome-win64\chromedriver64\chromedriver.exe"
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:51134")
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(service=ChromeService(executable_path=path_to_chromedriver_exe,
                                                    chrome_options=chrome_options))
    print(driver.title)
    api_url = "http://www.facebook.com"
    driver.get(api_url)
    driver.find_element(By.NAME, "email").send_keys("dwaipayandasi10@gmail.com")
    # driver.find_element(By.NAME, "email").clear()
    original_session_id = driver.session_id
    print("Session ID:", original_session_id)
    yield driver
