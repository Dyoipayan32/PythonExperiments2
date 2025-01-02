# import selenium
# from selenium import webdriver
# import webdriver_manager.chrome.service import ChromeDriverManger
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# browser = webdriver.get_driver("chromedriver")
#
# handles = browser.getWinHandles()
# current_window = browser.switch_to(handles[0])
# current_window.find_element(By.xpath, "/").click()
# action_chains = ActionChains()
# action
# new_window = browser.switch_to(handles[1])

arr = [10, 9, 8, 7, 11, 12]
new_arr = list()
for i in arr:
    if i != min(arr):
        new_arr.append(i)
print(min(new_arr))
