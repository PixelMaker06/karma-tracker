import os
try:
  from selenium import webdriver
except:
  os.system('py -m pip install selenium')

username = input("Username \n> ")

driver = webdriver.Chrome("drivers\chromedriver.exe ")

driver.set_page_load_timeout(10)
driver.get("https://www.reddit.com/user/{}/".format(username))
print(driver.find_element_by_id("profile--id-card--highlight-tooltip--karma").get_attribute('innerHTML'))
driver.quit()
