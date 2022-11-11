import time
from path import Path
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

dri = Chrome(service=Service(ChromeDriverManager().install()))
dri.get('http://www.manabadi.info/2022/AP-Intermediate-1st-year-regular-exam-results-May-2022.htm')
dri.maximize_window()
dri.implicitly_wait(20)

num = 2207111050
for i in range(0, 150):
    path_f = ""
    dri.find_element(*(By.ID, 'htno')).clear()
    dri.find_element(*(By.ID, 'htno')).send_keys(str(num))
    dri.find_element(*(By.ID, 'btnsubmit')).click()
    file_nam = "{}{}.jpeg".format(path_f, num)
    print(file_nam)
    S = lambda X: dri.execute_script('return document.body.parentNode.scroll' + X)
    dri.set_window_size(S('Width'), S('Height') + 300)
    dri.find_element('body').screenshot(file_nam)
    num += 1

    time.sleep(3)
