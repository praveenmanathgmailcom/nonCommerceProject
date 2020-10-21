import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AddCustomer:
    lnkCustomer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btn_Addnew_xpath = "//a[@class='btn bg-blue']"

    txt_Email_css = "input[id='Email']"
    txt_Password_css = "input[id='Password']"
    txt_FirstName_css = "input[id='FirstName']"
    txt_LastName_css = "input[id='LastName']"
    rb_Gender_male_css = "input[id='Gender_Male']"
    rb_Gender_female_css = "input[id='Gender_Female']"
    txt_Calendar_css = "input[id='DateOfBirth']"
    txt_Company_css = "input[id='Company']"
    chk_istaxexmpt_css = "input[id='IsTaxExempt']"

    txt_Newsletter_xpath = "//div[@class='panel-body']/div[9]/div[2]/div/div/div"
    lstitem_yourstorename_xpath = "//li[contains(text(), 'Your store name')]"
    lstitme_Teststore2_xpath = "//li[contains(text(),'Test store 2')]"

    txt_Customerrole_xpath = "//div[@class='panel-body']/div[10]/div[2]/div/div/div"
    lstitemAdminstrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    drpmrgofVendor_xpath = "//*[@id='VendorId']"

    chk_active_css = "input['#Active']"
    txt_Admincomment_xpath = "//*[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.xpath, self.lnkCustomer_menu_xpath)))
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def clickonCustomerMenuItem(self):
       # WebDriverWait(self.driver, 10).until(
       #     EC.presence_of_element_located((By.XPATH, self.lnkCustomer_menuitem_xpath)))
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        # WebDriverWait(self.driver, 10).
        # until(EC.presence_of_element_located((By.xpath,btn_Addnew_xpath)))
        self.driver.find_element_by_xpath(self.btn_Addnew_xpath).click()

    def setEmail(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.txt_Email_css)))
        self.driver.find_element_by_css_selector(self.txt_Email_css).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_css_selector(self.txt_Password_css).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_css_selector(self.txt_FirstName_css).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_css_selector(self.txt_LastName_css).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_css_selector(self.rb_Gender_male_css).click()
        elif gender == 'Female':
            self.driver.find_element_by_css_selector(self.rb_Gender_female_css).click()
        else:
            self.driver.find_element_by_css_selector(self.rb_Gender_male_css).click()

    def setDOB(self, dob):
        self.driver.find_element_by_css_selector(self.txt_Calendar_css).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element_by_css_selector(self.txt_Company_css).send_keys(companyname)

    def setNewsLetter(self, News):
        self.driver.find_element_by_xpath(self.txt_Newsletter_xpath).click()
        time.sleep(3)
        if News == 'Your store name':
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.lstitem_yourstorename_xpath)))
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_yourstorename_xpath)
        else:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.lstitme_Teststore2_xpath)))
            self.listitem = self.driver.find_element_by_xpath(self.lstitme_Teststore2_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setCustomerRole(self, role):
        self.driver.find_element_by_xpath(self.txt_Customerrole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdminstrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemForumModerators_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setMangerofVendor(self, value):
        select = Select(self.driver.find_element_by_xpath(self.drpmrgofVendor_xpath))
        select.select_by_visible_text(value)

    def setAdminConment(self, admincomment):
        self.driver.find_element_by_xpath(self.txt_Admincomment_xpath).send_keys(admincomment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
