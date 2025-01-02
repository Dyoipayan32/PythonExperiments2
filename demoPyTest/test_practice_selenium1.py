import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

path = os.getcwd()
currentDirectory = os.path.dirname(os.path.realpath(__file__))


def test_one():
    assert path == currentDirectory


def test_two():
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=r"C:\Users\Dwaipayan_Das\ChromeBrowserAutomation\chrome-win64\chromedriver64\chromedriver.exe"))
    driver.get("https://www.facebook.com")
    # Similar as clicking on a link that opens a new window
    driver.execute_script("window.open('');")
    windowHandles = driver.window_handles
    currentWindow = driver.current_window_handle
    assert currentWindow == windowHandles[0]
    driver.switch_to.window(currentWindow)
