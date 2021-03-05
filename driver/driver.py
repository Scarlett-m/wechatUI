# -*- coding:utf-8 -*-
#author:Manjusaka
from time import sleep
from selenium import webdriver

class Driver:
    def create_driver(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/")
        sleep(3)
        return driver