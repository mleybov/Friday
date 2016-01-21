from selenium import webdriver

print('Input your Google email address')
userEmail = input()
userEmail = "sfyuba123@gmail.com"
userEmail.send_keys(userEmail)
# try this and see if works

browser = webdriver.Firefox()
browser.get('http://mail.Google.com')

loginElem = browser.find_element_by_id('Email')
loginElem.click()

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(userEmail)
emailElem.submit()

print('Input your Google password')
userPassword = input()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(userPassword)
passwordElem.submit()

composeElem = browser.find_element_by_id(':hw')
composeElem.click()

print('Input recipient')
userRecipient = input()

toElem = browser.find_element_by_id(':n4')
toElem.send_keys(userRecipient)
toElem.click()

subjectElem = browser.find_element_by_id(':mp')
subjectElem.click()

bodyElem = browser.find_element_by_id(':nr')
bodyElem.click()