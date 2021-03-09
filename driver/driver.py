# -*- coding:utf-8 -*-
#author:Manjusaka
from time import sleep
from selenium import webdriver

class Driver():

    def create_driver(self):

        # 声明Chrome参数
        chrome_args = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_args.debugger_address = '127.0.0.1:9222'
        # 将Chrome参数传递给driver
        self.driver = webdriver.Chrome(options=chrome_args)
        # 使用remote复用已有浏览器
        # self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)
        return self
