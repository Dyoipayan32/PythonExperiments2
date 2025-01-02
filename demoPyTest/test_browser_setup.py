import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Define the command to open Chrome with remote debugging enabled
# new_chrome_path = "C:/Users/Dwaipayan_Das/.wdm/drivers/chromedriver/win64/131.0.6778.85/chromedriver-win32/chromedriver.exe"
# chrome_path = os.path.abspath(os.path.join(os.getcwd(), "chromedriver.exe"))

# port = "49242"
# command = f'Start-Process "chromedriver.exe" -ArgumentList "--remote-debugging-port={port}", "--user-data-dir={user_data_dir}"'
# # Use subprocess to run the command
# process = subprocess.Popen(command, shell=True)
# # Optional: Wait for the command to complete
# process.wait()
# print(f"Chrome launched with remote debugging on port {port}.")
# print("Done")


def test_launch_a_page_with_remote_debugging():
    # chrome_driver_path = ChromeDriverManager().install()
    # driver = webdriver.Chrome(chrome_driver_path)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # service = Service(ChromeDriverManager().install())
    # options = webdriver.ChromeOptions()
    # options.browser_version = 'stable'
    # options.add_argument('--headless')
    # options.add_experimental_option("debuggerAddress", f'127.0.0.1:49249')
    # driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(service=service, options=options)
    # # additional options here if needed, e.g., options.add_argument('--headless')
    # options.add_experimental_option("debuggerAddress", f'127.0.0.1:{port}')
    # Get session ID and executor URL from the original driver
    driver.get("http://www.google.com")
    original_session_id = driver.session_id
    original_executor_url = driver.command_executor._url
    print("Session ID:", original_session_id)
    print("Executor URL:", original_executor_url)


