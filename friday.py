from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://mail.Google.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('malvina415@gmail.com')

loginElem = browser.find_element_by_id('next')
loginElem.click()

print('Input your password')
userPassword = input()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(userPassword)
passwordElem.submit()

composeElem = browser.find_element_by_class_name('z0')
composeElem.click()

print('Input recipient')
userRecipient = input()

toElem = browser.find_element_by_id(':n4')
toElem.send_keys(userRecipient)
toElem.click()

print('Input your subject')
userSubject = input()

subjectElem = browser.find_element_by_id(':mp')
subjectElem.send_keys(userSubject)
subjectElem.click()

print('Input body of email here')

bodyElem = browser.find_element_by_id(':nr')
bodyElem.send_keys(userBody)