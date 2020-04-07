import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    def test_loginByEmail(self):
        # Instantiate Chrome Webdriver
        driver = webdriver.Chrome()
        driver.get("http://automationpractice.com/index.php")

        # Maximize browser
        driver.maximize_window()

        # Find and click sign in link
        driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        sleep(3)

        # Sign in to shop account
        # enter email address as username
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('automationtestuser613@gmail.com')

        # get password
        file = open('/Users/jechrz/PycharmProjects/JRPortfolio/PyDevPackage/credentials.txt', "r")
        # enter password
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(file.read())
        file.close()
        # click sign in button
        driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span').click()
        # Check if account logged in
        # check sign in link/button is gone (or check if sign out is displayed)
        check = str.lower(driver.find_element_by_xpath('//*[@id="columns"]/div[1]/span[2]').text)
        self.assertEqual(str.lower(check), 'my account')

        driver.close()

if __name__ == "__main__":
    unittest.main()
