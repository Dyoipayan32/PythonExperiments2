import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from newAutomationFrameWorkPytest.ControllerAPI import ControllerAPI
from newAutomationFrameWorkPytest.PageObjectsUI import PageObjectsUI
from newAutomationFrameWorkPytest.apiModules.client import ApiClient


def pytest_addoption(parser):
    """Directly creates command line arguments with default values and stores them inside request.config """
    parser.addoption(
        "--browser", action="store", default="chrome"
    )
    parser.addoption(
        "--reporter", action="store", default="html"
    )


@pytest.fixture(scope="class")
def ui(request):
    """For browser set up which runs iteratively based on given scope
    param request: For using command line arguments request fixture is invoked here as argument
    :return: returns None but yields the driver or browser to supply across the all the classes
    """
    global DRIVER
    # global REPORTER

    # TEST_CASE_DOC = os.path.join(os.getcwd(), 'SimplifiedTCs.csv')
    # READER_DOC = open(TEST_CASE_DOC, 'r')
    # CSV_READER = csv.DictReader(READER_DOC)
    # REPORTER = request.config.getoption("reporter")
    chrome_path = os.path.abspath(os.path.join(os.getcwd(), "chromedriver.exe"))
    print("inside set up")
    browser_name = request.config.getoption("browser")

    """Selecting driver or browser based on the default browser name"""
    if browser_name == "chrome":
        # DRIVER = webdriver.Chrome(ChromeDriverManager().install())
        service = Service(ChromeDriverManager().install())
        # Create Driver Instance
        DRIVER = webdriver.Chrome(service=service)
    pageObjectCaller = PageObjectsUI(DRIVER)
    yield pageObjectCaller

    DRIVER.close()
    DRIVER.quit()


@pytest.fixture(scope="class")
def api():
    CLIENT = ApiClient()
    apiController = ControllerAPI(CLIENT)
    yield apiController
    CLIENT.close()


@pytest.fixture(params=[("3+4", 7), ("3+5", 8), ("3+3", 6)])
def evaluate_inputs(request):
    return request.param
