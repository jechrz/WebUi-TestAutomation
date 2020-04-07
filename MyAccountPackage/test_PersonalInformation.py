import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PyDevPackage.FetchEnvironment import getLoggedInPage
from lxml import html


class PersonalInfoTest(unittest.TestCase):
    driver = webdriver.Chrome()

    def test_PersonalInformationPageAccess(self):
        PersonalInfoTest.driver.get("http://automationpractice.com/index.php")
        getLoggedInPage(PersonalInfoTest.driver)
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[4]/a/span').click()
        pagecheck = str.lower(PersonalInfoTest.driver.find_element_by_xpath('//*[@id="columns"]/div[1]/span[3]').text)
        self.assertEqual(str.lower(pagecheck), 'your personal information')
        sleep(3)

    def test_UpdatePersonalInfo(self):  # Happy path update personal information

        # Update Social Title
        selected = PersonalInfoTest.driver.find_element_by_xpath('//*[@id="id_gender1"]').get_property('checked')
        if selected:
            PersonalInfoTest.driver.find_element_by_xpath('//*[@id="id_gender2"]').click()
        else:
            PersonalInfoTest.driver.find_element_by_xpath('//*[@id="id_gender1"]').click()

        # Update First name
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="firstname"]').clear()
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="firstname"]').send_keys('Automation')

        # Update Last name
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="lastname"]').clear()
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="lastname"]').send_keys('User')

        # Update Email
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="email"]').clear()
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="email"]').send_keys('automationtestuser613@gmail.com')

        # Update Date of Birth
        elementDays = Select(PersonalInfoTest.driver.find_element_by_xpath('//*[@id="days"]'))
        elementMonths = Select(PersonalInfoTest.driver.find_element_by_xpath('//*[@id="months"]'))
        elementYears = Select(PersonalInfoTest.driver.find_element_by_xpath('//*[@id="years"]'))

        elementDays.select_by_value('16')
        elementMonths.select_by_value('7')
        elementYears.select_by_value('1961')

        # Update Password
        file = open('/Users/jechrz/PycharmProjects/JRPortfolio/PyDevPackage/credentials.txt', "r")
        hiddenString = file.read()

        # Old Password requirement
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="old_passwd"]').send_keys(hiddenString)

        # Disable above line and enable below line to fail test
        # PersonalInfoTest.driver.find_element_by_xpath('//*[@id="old_passwd"]').send_keys('failPass')

        # New Password
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(hiddenString)

        # Confirm New Password
        PersonalInfoTest.driver.find_element_by_xpath('//*[@id="confirmation"]').send_keys(hiddenString)
        hiddenString = ''
        sleep(3)
        file.close()

        # Save Changes
        PersonalInfoTest.driver.find_element_by_xpath(
            '// *[ @ id = "center_column"] / div / form / fieldset / div[11] / button / span').click()
        sleep(3)

        # Confirm Personal Info Updates Saved
        confirm = PersonalInfoTest.driver.find_element_by_xpath('// *[ @ id = "center_column"] / div / p').text
        self.assertEqual(str.lower(confirm), 'your personal information has been successfully updated.')

        PersonalInfoTest.driver.close()

if __name__ == "__main__":
    unittest.main()
