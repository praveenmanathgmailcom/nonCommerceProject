import random
import string
import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*************Test 003 Started**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("**************Enter Login Details***********")
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword((self.password))
        self.lp.clickLogin()
        self.logger.info("***************Login Successful*************")
        time.sleep(3)
        self.logger.info("****************Starting Add Customer************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickonCustomerMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("*****************Provide Customer info************")
        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Customer2")
        self.addcust.setLastName("info2")
        self.addcust.setGender("Female")
        self.addcust.setDOB("04/01/2011")
        self.addcust.setCompanyName("heist")
        self.addcust.setNewsLetter("Your store name")
        self.addcust.setCustomerRole("Vendors")
        self.addcust.setMangerofVendor("Vendor 1")
        self.addcust.setAdminConment("This is for Testing")
        self.addcust.clickOnSave()
        self.logger.info("***********Saving Customer Info**************")
        self.logger.info("***********Add Customer Validation Started********")
        self.msg = self.driver.find_element_by_tag_name("body").text
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("***********Add Customer Validation Passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("***********Add Customer Validation Failed*********")
            assert False
        self.driver.close()
        self.logger.info("***********Test 003 AddCustomer End********")

    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
