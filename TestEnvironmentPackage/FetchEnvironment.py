from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep


# Open automation practice web page My Account page
def getLoggedInPage(driver):
    # Find and click sign in link
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
    sleep(3)

    # Sign in to shop account
    # enter email address as username
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('automationtestuser613@gmail.com')

    # get password
    file = open('/Users/jechrz/PycharmProjects/WebUi-TestAutomation/TestEnvironmentPackage/credentials.txt', "r")
    # enter password
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(file.read())
    file.close()
    # click sign in button
    driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span').click()

    return driver




