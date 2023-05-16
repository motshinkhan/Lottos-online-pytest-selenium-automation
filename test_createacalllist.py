import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get("https://lottosonline.thefamcomlab.com/")
driver.maximize_window()
time.sleep(15)
driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.ID, "email").send_keys("pradeepadmin@yopmail.com")
driver.find_element(By.ID, "password").send_keys("famcom")
driver.find_element(By.ID, "submit_button").click()
driver.find_element(By.LINK_TEXT, "Call List Settings").click()
driver.find_element(By.LINK_TEXT, "Create Call Lists").click()
driver.find_element(By.ID, "addRecord").click()
time.sleep(5)

search_field = driver.find_element(By.ID, 'call_list_name')
search_field.send_keys("New Test call list V2")
time.sleep(5)

# Find the dropdown element and create a Select object
#dropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-id']"))
# Select the option using its xpath
#dropdown.select_by_xpath("//option[@value='option-value']")
#//*[@id="cid"]/option[30]
# element = driver.find_element(By.CSS_SELECTOR, ".modal-content:nth-child(2) > .modal-body")
# actions = ActionChains(driver)
# actions.move_to_element(element).click_and_hold().perform()
# element = driver.find_element(By.CSS_SELECTOR, ".modal-content:nth-child(2) > .modal-body")
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
# element = driver.find_element(By.CSS_SELECTOR, ".modal-content:nth-child(2) > .modal-body")
# actions = ActionChains(driver)
# actions.move_to_element(element).release().perform()

# driver.find_element(By.ID, "call_list_name").send_keys("C1")
dropdown = driver.find_element(By.ID, "cid")
dropdown.find_element(By.XPATH, "//option[. = 'India']").click()
driver.find_element(By.ID, "max_records").send_keys("4")
driver.find_element(By.ID, "save").click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="menu"]/li[14]/a').click()
time.sleep(5)
driver.quit()