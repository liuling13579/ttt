#coding:utf-8

from selenium import webdriver
import unittest
from pages.login import Login_TT

class LoginTTTest(unittest.TestCase):
    '''登录测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login_TT(cls.driver)

    def test_01(self):
        '''
        "admin","123456"
        '''
        self.L.login_tt("admin","123456")
        t = self.L.is_login_success()
        print("获取的结果：%s"%t)
        self.assertIn("admin",t)

    def test_02(self):
        '''
        "11111","123456"
        '''
        self.L.login_tt("11111","123456")
        t = self.L.is_login_success()
        print("获取的结果：%s"%t)
        self.assertIn("admin",t)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

