
from typing import KeysView
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
    
driver.get('https://lottosonline.thefamcomlab.com')
time.sleep(10)
driver.maximize_window()

# click on the Login button
driver.find_element(By.LINK_TEXT, "Login").click()
# fill in the login form
driver.find_element(By.ID, "email").send_keys("pradeepadmin@yopmail.com")
driver.find_element(By.ID, "password").send_keys("famcom")
driver.find_element(By.ID, "submit_button").click()
time.sleep(2)
# click on the "Customer List" link
customer_search_link = driver.find_element(By.XPATH, "//a[contains(@href,'customer_search')]")
customer_search_link.click()
time.sleep(2)

# click on the "Search Panel" button
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[3]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol1_tag_input')
search_field.send_keys("Hunny")
search_field.send_keys(Keys.RETURN)
time.sleep(2)

# Removing the search data
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol1_tag_list"]/li/a')
search_button.click()
time.sleep(1)

# Searching by user id
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[2]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol0_tag_input')
search_field.send_keys("134970")
search_field.send_keys(Keys.RETURN)
time.sleep(2)

# Removing the search data from user id
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol0_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by last name
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[4]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol10_tag_input')
search_field.send_keys("goswami")
search_field.send_keys(Keys.RETURN)
time.sleep(1)

# Removing the search data from user id
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol10_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by Email id
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[5]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol2_tag_input')
search_field.send_keys("hunny@yopmail.com")
search_field.send_keys(Keys.RETURN)

time.sleep(1)

# Removing the search data from email id
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol2_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by Phone number
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[6]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, "tagsinputcol3_tag_input")
search_field.send_keys("9599899387")
search_field.send_keys(Keys.RETURN)

# Removing the search data from Phone number
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol3_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by Country name
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[7]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, "tagsinputcol4_tag_input")
search_field.send_keys("India")
search_field.send_keys(Keys.RETURN)

time.sleep(1)
# Removing the search data from Country name
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol4_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by Last Web Purchase date
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[12]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol53_tag_input')
search_field.send_keys("09-May-2023")
search_field.send_keys(Keys.RETURN)

time.sleep(1)
# Removing the search data from Last Web Purchase date
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol53_tag_list"]/li/a')
search_button.click()
time.sleep(2)

time.sleep(1)

# Searching by Reward balance
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[15]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol5_tag_input')
search_field.send_keys("5.54")
search_field.send_keys(Keys.RETURN)

time.sleep(1)

# Removing the search data from Reward balance
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol5_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by cash
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[16]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol6_tag_input')
search_field.send_keys("42")
search_field.send_keys(Keys.RETURN)

# Removing the search data from cash
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol6_tag_list"]/li/a')
search_button.click()
time.sleep(5)

# Searching by cash
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[17]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol7_tag_input')
search_field.send_keys("542.97")
search_field.send_keys(Keys.RETURN)

# Removing the search data from cash
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol7_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by Total sales
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[18]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, "tagsinputcol8_tag_input")
search_field.send_keys("4,552.16")
search_field.send_keys(Keys.RETURN)
time.sleep(2)

# Removing the search data from Total sales
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol8_tag_list"]/li/a')
search_button.click()
time.sleep(5)

# Searching by Last sales diposit date
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[19]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, "tagsinputcol54_tag_input")
search_field.send_keys("30-Aug-2021")
search_field.send_keys(Keys.RETURN)

time.sleep(1)
# Removing the search data from Last sales diposit date
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol54_tag_list"]/li/a')
search_button.click()
time.sleep(5)

# Searching by Last Win Amount
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[20]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol9_tag_input')
search_field.send_keys("542.97")
search_field.send_keys(Keys.RETURN)

time.sleep(1)
# Removing the search data from Last Win Amount
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol9_tag_list"]/li/a')
search_button.click()
time.sleep(2)

# Searching by total Wins 
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[21]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol11_tag_input')
search_field.send_keys("542.97")
search_field.send_keys(Keys.RETURN)

time.sleep(1)
# Removing the search data from Total Wins
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol11_tag_list"]/li/a')
search_button.click()
time.sleep(2)


# Searching by Card Type
search_button = driver.find_element(By.XPATH, '//*[@id="dyntable"]/thead/tr/th[24]/span[2]/i')
search_button.click()

search_field = driver.find_element(By.ID, 'tagsinputcol55_tag_input')
search_field.send_keys("542.97")
search_field.send_keys(Keys.RETURN)

time.sleep(1)
# Removing the search data from Card type
search_button = driver.find_element(By.XPATH, '//*[@id="tagsinputcol55_tag_list"]/li/a')
search_button.click()
time.sleep(2)



