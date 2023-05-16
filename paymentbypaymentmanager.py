from typing import KeysView
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver_path = 'path/to/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)
    
driver.get('https://lottosonline.thefamcomlab.com')
time.sleep(15)
driver.maximize_window()

# click on the "Login" link
driver.find_element(By.LINK_TEXT, "Login").click()
# fill in the login form
driver.find_element(By.ID, "email").send_keys("pradeepsalesmanager@yopmail.com")
driver.find_element(By.ID, "password").send_keys("famcom")
driver.find_element(By.ID, "submit_button").click()
time.sleep(2)

driver.find_element(By.ID, "save").click()
time.sleep(2)
# call list link
driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/a').click()
time.sleep(2)


#click on the call list
driver.find_element(By.LINK_TEXT, "New 6 march test list-").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, 'https://lottosonline.thefamcomlab.com/admin/sp_customer_search.php?sp_customer_id=85628').click()

#driver.find_element(By.XPATH, '//*[@id="recordListing"]/tbody/tr[1]/td[2]/a').click()


#driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a').click()
time.sleep(2)
                    
# # click on the "Customer List" link
# customer_search_link = driver.find_element(By.XPATH, "//a[contains(@href,'customer_search')]")
# customer_search_link.click()
# time.sleep(2)

# click on the "Search Panel" button
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[2]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol1_tag_input') 
search_field.send_keys("Hunny")
search_field.send_keys(Keys.RETURN)
time.sleep(2)


driver.find_element(By.XPATH, '//*[@id="dyntable"]/tbody/tr/td[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/ul/li[1]/a').click()
time.sleep(2)
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .button-playnow").click()
driver.find_element(By.LINK_TEXT, "Quick pick").click()
driver.find_element(By.CSS_SELECTOR, ".ticket-container:nth-child(3) > .qp").click()
driver.find_element(By.CSS_SELECTOR, ".ticket-container:nth-child(4) > .qp").click()
driver.find_element(By.CSS_SELECTOR, ".ticket-container:nth-child(5) > .qp").click()
driver.find_element(By.CSS_SELECTOR, ".ticket-container:nth-child(6) > .qp").click()
driver.find_element(By.CSS_SELECTOR, ".button-playnow").click()
time.sleep(2)

element = driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.CSS_SELECTOR, ".ui-slider-range")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, ".ui-slider-range")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
driver.find_element(By.CSS_SELECTOR, ".ui-slider-handle").click()
#driver.find_element(By.CSS_SELECTOR, ".row > #submit_button").click()
driver.find_element(By.XPATH, '//*[@id="card_details_container"]/div[2]/a[2]').click()

#driver.find_element(By.ID, "submit_button").click()




driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) img").click()

driver.find_element(By.LINK_TEXT, "Login").click()

driver.find_element(By.CSS_SELECTOR, "body").click()
driver.find_element(By.ID, "email").send_keys("iampradeepgoswami@gmail.com")
driver.find_element(By.ID, "password").send_keys("famcom")
driver.find_element(By.ID, "submit_button").click()
driver.find_element(By.LINK_TEXT, "View").click()
driver.find_element(By.ID, "tarans_id").click()
driver.find_element(By.ID, "tarans_id").send_keys("test03112022008")
driver.find_element(By.ID, "submit_button2").click()
time.sleep(10)
