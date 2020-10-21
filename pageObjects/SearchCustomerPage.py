class SearchCustomer:
    # WebElements
    txtEmail_css = "#SearchEmail"
    txtFirstname_css = '#SearchFirstName'
    txtLastname_css = '#SearchLastName'
    txtMonth_css = '#SearchMonthOfBirth'
    txtDay_css = 'SearchDayOfBirth'
    btnSearch_css = '#search-customers'
    table_css = ".dataTables_scroll"
    tblSearchResult_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setSearchEmail(self, email):
        self.driver.find_element_by_css_selector(self.txtEmail_css).clear()
        self.driver.find_element_by_css_selector(self.txtEmail_css).send_keys(email)

    def setSearchFN(self, firstname):
        self.driver.find_element_by_css_selector(self.txtFirstname_css).clear()
        self.driver.find_element_by_css_selector(self.txtFirstname_css).send_keys(firstname)

    def setSearchLN(self, lastname):
        self.driver.find_element_by_css_selector(self.txtLastname_css).clear()
        self.driver.find_element_by_css_selector(self.txtLastname_css).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element_by_css_selector(self.btnSearch_css).click()

    def getNoRow(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoColumn(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoRow()+1):
            table = self.driver.find_element_by_css_selector(self.table_css)
            emailid = table.find_element_by_xpath('//table[@id="customers-grid"]//tbody/tr["str(r)"]/td[2]').text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoRow()+1):
            table = self.driver.find_element_by_css_selector(self.table_css)
            name = table.find_element_by_xpath('//table[@id="customers-grid"]//tbody/tr["str(r)"]/td[3]').text
            if name == Name:
                flag = True
                break
        return flag

