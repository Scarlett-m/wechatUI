# coding=utf-8
# author:
# datetime:2021-03-07 15:58
from time import sleep

from page.add_member_page import AddMemberPage
from page.main_page import MainPgae


class TestAddMember:

    def setup(self):
        # self.add_member_page = AddMemberPage()
        pass

    def test_add_member(self):
        """
        登录成功后，添加成员
        :return:
        """
        self.main_page = MainPgae()
        add_page = self.main_page.click_contract()
        add_page.click_addmember()


        # self.add_member_page.click_addmember()


    # def test_click_login(self):
    #     """
    #     企业微信官网页点击登录
    #     :return:
    #     """
    #     self.add_member_page.click_login()
    #     self.page = self.add_member_page.driver.page_source
    #     assert "企业注册" in self.page


    # 当复用浏览器时，不生效
    # def teardown(self):
    #     self.add_member_page.quit()
