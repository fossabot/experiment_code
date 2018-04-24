# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-24 14:44:23
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-24 15:15:29
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def mock_nexus5():
    mobile_emulation = {"deviceName": "Nexus 5X"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument('lang=en_US')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://www.baidu.com")
    driver.close()

def mock_useragent():
    mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get("http://www.baidu.com")
    driver.close()

if __name__ == '__main__':
    mock_nexus5()