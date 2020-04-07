import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyDevPackage.FetchEnvironment import getLoggedInPage


class Xpath_Util:
    """Class to generate the xpaths"""

    def __init__(self):
        self.elements = None
        self.guessable_elements = ['input', 'button']
        self.known_attribute_list = ['id', 'name', 'placeholder', 'value', 'title', 'type', 'class']

    def generate_xpath(self, soup):
        "generate the xpath"
        result_flag = False
        try:
            for guessable_element in self.guessable_elements:
                self.elements = soup.find_all(guessable_element)
                for element in self.elements:
                    if (not element.has_attr("type")) or (element.has_attr("type") and element['type'] != "hidden"):
                        for attr in self.known_attribute_list:
                            if element.has_attr(attr):
                                locator = self.guess_xpath(guessable_element, attr, element)
                                if len(driver.find_elements_by_xpath(locator)) == 1:
                                    result_flag = True
                                    print(locator.encode('utf-8'))
                                    break
                            elif guessable_element == 'button' and element.getText():
                                button_text = element.getText()
                                if element.getText() == button_text.strip():
                                    locator = xpath_obj.guess_xpath_button(guessable_element, "text()",
                                                                           element.getText())
                                else:
                                    locator = xpath_obj.guess_xpath_using_contains(guessable_element, "text()",
                                                                                   button_text.strip())
                                if len(driver.find_elements_by_xpath(locator)) == 1:
                                    result_flag = True
                                    print(locator.encode('utf-8'))
                                    break
        except Exception as e:
            print("Exception when trying to generate xpath for:%s" % guessable_element)
            print("Python says:%s" % str(e))

        return result_flag

    def guess_xpath(self, tag, attr, element):
        "Guess the xpath based on the tag,attr,element[attr]"
        # Class attribute returned as a unicodeded list, so removing 'u from the list and joining back
        if type(element[attr]) is list:
            element[attr] = [i.encode('utf-8') for i in element[attr]]
            element[attr] = ' '.join(element[attr])
        self.xpath = "//%s[@%s='%s']" % (tag, attr, element[attr])

        return self.xpath

    def guess_xpath_button(self, tag, attr, element):
        "Guess the xpath for button tag"
        self.button_xpath = "//%s[%s='%s']" % (tag, attr, element)

        return self.button_xpath

    def guess_xpath_using_contains(self, tag, attr, element):
        "Guess the xpath using contains function"
        self.button_contains_xpath = "//%s[contains(%s,'%s')]" % (tag, attr, element)

        return self.button_contains_xpath

#-------START OF SCRIPT--------
if __name__ == "__main__":
    print("Start of %s" % __file__)

    # Initialize the xpath object
    xpath_obj = Xpath_Util()

    driver = webdriver.Chrome()

    driver.get('http://automationpractice.com/index.php')
    getLoggedInPage(driver)
    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[4]/a/span').click()
    #print(driver.current_url)

    url = driver.current_url
    page = driver.execute_script("return document.body.innerHTML").encode('utf-8')
    soup = BeautifulSoup(page, 'html.parser')

    if xpath_obj.generate_xpath(soup) is False:
            print("No XPaths generated for the URL:%s"%url)

    driver.quit()