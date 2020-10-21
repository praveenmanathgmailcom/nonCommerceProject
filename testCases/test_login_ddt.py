import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_ddt_Login(self, setup):
        self.logger.info("***********test_ddt_Login***********")
        self.logger.info("***********Verifying The Login Test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("No of Rows in Excel : ", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(10)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************Login Test Passed**********")
                    lst_status.append("Pass")
                    print(lst_status)
                    self.lp.clickLogout()
                    assert True
                elif self.exp == "Fail":
                    self.logger.info("************Login Test Failed**********")
                    lst_status.append("Fail")
                    print(lst_status)
                    self.lp.clickLogout()
                    assert False
            elif act_title != exp_title:
                if self.exp == "Fail":
                    self.logger.info("************Login Test Passed**********")
                    lst_status.append("Pass")
                    print(lst_status)
                    assert True
                elif self.exp == "Pass":
                    self.logger.info("************Login Test Failed**********")
                    lst_status.append("Fail")
                    print(lst_status)
                    assert False

        if "Fail" not in lst_status:
            self.logger.info("*********Login DDT Test Passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********Login DDT Test Failed*********")
            self.driver.close()
            assert False
        self.logger.info("**************End of Login Test*****************")
