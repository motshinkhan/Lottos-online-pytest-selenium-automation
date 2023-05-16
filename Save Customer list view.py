
from typing import KeysView
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = 'path/to/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)
    

driver.get('https://lottosonline.thefamcomlab.com')
time.sleep(15)
driver.maximize_window()

# click on the "Login" linkfa
driver.find_element(By.LINK_TEXT, "Login").click()
# fill in the login form
driver.find_element(By.ID, "email").send_keys("pradeepadmin@yopmail.com")
driver.find_element(By.ID, "password").send_keys("famcom")
driver.find_element(By.ID, "submit_button").click()
time.sleep(2)
# click on the "Customer List" link
customer_search_link = driver.find_element(By.XPATH, "//a[contains(@href,'customer_search')]")
customer_search_link.click()
time.sleep(5)

# click on the "Search Panel" button
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[3]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol1_tag_input')
search_field.send_keys("Hunny")
search_field.send_keys(Keys.RETURN)
time.sleep(5)

search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[3]/span[2]/i')
search_button.click()

#driver.find.element(By.id,"save_view").click()

save_view = driver.find_element(By.XPATH, '//*[@id="save_view"]')
save_view.click()
time.sleep(5)


driver.find_element(By.ID,"view_name").send_keys("List V1")

time.sleep(5)
save_view_button = driver.find_element(By.XPATH, '//*[@id="saveViewData"]')
save_view_button.click()







