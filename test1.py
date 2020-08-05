from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.instagram.com/accounts/emailsignup/')

print("successfully opened :- ", driver.title)

# finding instagram elements
email_field =driver.find_elements_by_name("emailOrPhone") 
fullname = driver.find_elements_by_name("fullName")
username = driver.find_elements_by_name("username")
password = driver.find_elements_by_name("password")


if (email_field != [] and fullname!= [] and username!= [] and password != []):
    print("All fields of instagram found !"+'\n'+"----------------------------")
else :
    print("unable to detect fields")

#Opening a new tab with temp mail:-
driver.execute_script("window.open ('https://temp-mail.org/en/','new window')" ) # opens new tab with "tempmail.org"
driver.switch_to.window(driver.window_handles[1])  #switches to the tab
print("successfully opened :- ", driver.title)

copy_button = driver.find_elements_by_id("click-to-copy")
time.sleep(2.5)
copy_button[0].click()

print("temp email copied! :" +'\n'+ "----------------------------------------")

# switching back to the previous tab (instagram/login.com) 
driver.switch_to.window(driver.window_handles[0])

print(email_field)
print(fullname)
print(password)
print(username)
email_field.send_keys(Keys.CONTROL + 'v')







#driver.close()

# some extras
'''
actions = Action(driver)
find = driver.find_element_by_link_text('ABC')
actions.key_down(Keys.CONTROL).click(find).key_up(Keys.CONTROL).perform()

driver.switch_to.window(driver.window_handles[-1])
'''
'''
body = driver.find_elements(By.TAG_NAME,"body")
body[0].send_keys(Keys.CONTROL + 't')
'''
'''
body = driver.find_elements_by_tag_name("body")
body[0].send_keys(Keys.CONTROL + 't')
'''
'''
# open tempmail tor temp email
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get("https://temp-mail.org/en/")
print("successfully opened :- ", driver.title)
'''

