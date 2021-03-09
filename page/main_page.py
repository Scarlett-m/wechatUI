# coding=utf-8
# author:
# datetime:2021-03-09 08:28
from selenium.webdriver.common.by import By

from driver.driver import Driver
from page.add_member_page import AddMemberPage
from page.base_page import BasePage


class MainPgae(BasePage):
    contract_button = (By.XPATH, "//*[@class='frame_nav_item_title']")

    def __init__(self):
        self.obj_driver = Driver.create_driver(self)

    def click_contract(self):
        self.find_element_and_click(self.contract_button)
        return AddMemberPage(self.obj_driver)



