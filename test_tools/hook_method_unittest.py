# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-19 10:14:01
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-19 10:21:34

import  unittest
from selenium import  webdriver
import time 

class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')

    
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')

    def test_003(self):
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()

if __name__=='__main__':
    # suite=unittest.TestSuite(unittest.makeSuite(TestDiv))
    suite=unittest.TestLoader().loadTestsFromTestCase(TestDiv)
    
    unittest.TextTestRunner(verbosity=2).run(suite)