import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_005_SearchCutomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchcutomerbyname(self, setup):
        self.logger.info("********SearchCustomerByEmail_004 Started*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************Login Successful***************")
        self.logger.info("************Start Searching by Name***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickonCustomerMenuItem()
        self.logger.info("************Searching customer by Name***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setSearchFN("Victoria")
        searchcust.setSearchLN("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("************TC Search customer by Name Finished***************")
        self.driver.close()
