import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_004_SearchCutomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchcutomerbyemail(self, setup):
        self.logger.info("********SearchCustomerByEmail_004 Started*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************Login Successful***************")
        self.logger.info("************Start Searching by Email***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickonCustomerMenuItem()
        self.logger.info("************Searching customer by Email***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setSearchEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("************TC Search customer by Email Finished***************")
        self.driver.close()
