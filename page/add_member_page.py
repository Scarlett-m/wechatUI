# -*- coding:utf-8 -*-
#author:Manjusaka
from time import sleep

from selenium.webdriver.common.by import By
from driver.driver import Driver
from page.base_page import BasePage

class AddMemberPage(BasePage):
    """
    继承一个通用页面
    """

    # login_button = (By.XPATH, "//*[@class='index_top_operation_loginBtn']")
    addmember_button = (By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")

    def __init__(self):
        self.obj_driver = Driver.create_driver(self)

    def click_addmember(self):
        self.find_element_and_click(self.addmember_button)

    def submit(self):
        pass

    def click_login(self):
        self.find_element_and_click(self.login_button)
