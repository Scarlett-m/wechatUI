# coding=utf-8
# author:
# datetime:2021-03-07 15:43

from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """
    页面的一些通用操作
    """

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def find_element_and_click(self, locator):
        """
        找到元素并点击
        :param locator:
        :return:
        """
        return self.driver.find_element(*locator).click()

    def quit(self):
        self.driver.quit()
