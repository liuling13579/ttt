#coding:utf-8
from common.base import Base
import common.parms as pa
import time

class Login_TT(Base):
    '''跟单宝登录'''
    loc_username =("xpath","//input[@placeholder='请输入账号']")
    loc_psw = ("xpath","//input[@placeholder='请输入密码']")
    loc_verify = ("xpath","//input[@placeholder='请输入图片验证码']")
    loc_rember = ("xpath","//*[@class='el-checkbox__inner']")
    loc_login = ("xpath","//button/span[text()='登录']")
    loc_loginname = ("xpath","//*[@class='head-ico']/span")
    loc_ = ("","")

    def input_username(self,username):
        self.sendKeys(self.loc_username,username)

    def input_pwd(self,pwd):
        self.sendKeys(self.loc_psw,pwd)

    def inpt_verify(self,verify):
        self.sendKeys(self.loc_verify,verify)

    def click_rember_login(self):
        self.click(self.loc_rember)

    def click_login(self):
        self.click(self.loc_login)

    def login_tt(self,username=pa.loc_name_admin,psw=pa.loc_name_admin_pwd,verify=pa.loc_verify):
        self.driver.get(pa.host)
        self.driver.maximize_window()
        self.input_username(username)
        self.input_pwd(psw)
        self.inpt_verify(verify)
        self.click_rember_login()
        self.click_login()

    def is_login_success(self):
        try:
            name = self.findElementNew(self.loc_loginname).text
            print("login seccess"+name)
            return name
        except:
            print("获取用户名失败")
            return ""

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login_TT(driver)
    L.login_tt()
    L.is_login_success()





