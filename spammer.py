# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from random import randint

class Spammer:
    def __init__(self):
        self.load_data()
        self.phone = input("Phone...")
        self.count = int(input("How many times?.."))

        # for i in range(self.count):
        #     self.curr_firstname = self.firstnames[randint(0, len(self.firstnames)-1)]
        #     print(self.curr_firstname)
        #     self.curr_secondname = self.secondnames[randint(0, len(self.secondnames)-1)]
        self.curr_proxy = self.proxy_adrs[randint(0, len(self.proxy_adrs)-1)]
        self.loop_call()

    def give_proxy(self, proxy_adr):
        print(proxy_adr)
        self.proxy_adr = proxy_adr.split(':')
        self.proxy_ip = self.proxy_adr[0]
        self.proxy_port = int(self.proxy_adr[1])
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("permissions.default.image", 2)
        self.profile.set_preference("network.proxy.http", self.proxy_ip)
        self.profile.set_preference("network.proxy.http_port", self.proxy_port)
        self.profile.set_preference("network.proxy.ftp", self.proxy_ip)
        self.profile.set_preference("network.proxy.ftp_port", self.proxy_port)
        self.profile.set_preference("network.proxy.ssl", self.proxy_ip)
        self.profile.set_preference("network.proxy.ssl_port", self.proxy_port)
        self.profile.set_preference("network.proxy.socks", self.proxy_ip)
        self.profile.set_preference("network.proxy.socks_port", self.proxy_port)
        self.profile.set_preference("network.proxy.type", 1)
        self.profile.set_preference("permissions.default.image", 2)
        return self.profile

    def load_data(self):
        # self.firstnames = open("firstnames_list.txt", "r").read().split(" ")
        # self.secondnames = open("secondnames_list.txt", "r").read().split(" ")
        self.proxy_adrs = open("proxy_list.txt").read().split(" ")
        self.sites = open("sites.txt").read().split(" ")

    def call(self, url, mode = 0):
        self.driver.get(url)
        if mode == 0:
            self.phone_button = self.driver.find_element_by_id("bingc-phone-button")
            self.phone_button.click()
            self.num_form = self.driver.find_element_by_id("bingc-passive-get-phone-form-input")
            self.submit_button = self.driver.find_element_by_id("bingc-passive-phone-form-button")
        else:
            self.num_form = self.driver.find_element_by_id("bingc-active-get-phone-form-input")
            self.submit_button = self.driver.find_element_by_id("bingc-active-phone-form-button")
        self.num_form.send_keys(self.phone)
        self.submit_button.click()
        print("#Good! Continue...")

    def loop_call(self):
        for i in range(self.count):
            self.curr_proxy = self.proxy_adrs[randint(0, len(self.proxy_adrs)-1)]
            self.driver = webdriver.Firefox(self.give_proxy(self.curr_proxy))
            for i in self.sites:
                try:
                    self.call(i)
                    pass
                except (ElementClickInterceptedException, NoSuchElementException) as ex:
                    try:
                        self.call(i, 1)
                    except (ElementClickInterceptedException, NoSuchElementException) as exep:
                        print("#!!!Bad element id!!! Site: " + i + " Continue...")
                    pass
                except (TimeoutException, WebDriverException) as e:
                    print("#!!!Some error!!! Continue...")
                    self.driver.quit()
                    self.curr_proxy = self.proxy_adrs[randint(0, len(self.proxy_adrs)-1)]
                    self.driver = webdriver.Firefox(self.give_proxy(self.curr_proxy))
            self.driver.quit()

spammer = Spammer()
