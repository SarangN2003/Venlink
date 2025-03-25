

from selenium.webdriver.common.by import By



class HomePage1:
    def __init__(self,driver):
        self.driver = driver

    # Cudtomer login page
    Email = (By.XPATH, "//input[@name='username']")
    Password = (By.XPATH, "//input[@name='password']")
    CheckBox = (By.XPATH, "//input[@name='termsConditionsCheckBox']")
    sign_in_button = SignIn = (By.XPATH, "//button[text()='SIGN IN']")

    # vendor request Login Page
    click =(By.XPATH,"//div/div[text()='Vendor']")
    Name = (By.XPATH,"//input[@name='accountName']")
    vender_Type = (By.XPATH,"//button[@id='combobox-button-31']")
    vender_Typeselect = (By.XPATH,"//lightning-base-combobox-item[@id='combobox-button-31-1-31']")
    BusinessCase = (By.XPATH,"//div/textarea[@name='businessCase']")
    FirstName = (By.XPATH,"//input[@name='firstName']")
    LastName = (By.XPATH,"//input[@name='lastName']")
    Email2= (By.XPATH,"//input[@name='email']")
    Phone = (By.XPATH,"//input[@name='phone']")
    Next = (By.XPATH,"//div/button[text()='Next']")






    # custoner login page
    def getEmail(self):
        return self.driver.find_element(*HomePage1.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage1.Password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage1.CheckBox)

    def getSignIn(self):
        return self.driver.find_element(*HomePage1.SignIn)

# first Login Page
    def getclick(self):
        return self.driver.find_element(*HomePage1.click)

    def getName(self):
        return self.driver.find_element(*HomePage1.Name)

    def getvendertype(self):
        return self.driver.find_element(*HomePage1.vender_Type)

    def getvendertypeselect(self):
        return self.driver.find_element(*HomePage1.vender_Typeselect)

    def getBusinessCase(self):
        return self.driver.find_element(*HomePage1.BusinessCase)

    def getFirstName(self):
        return self.driver.find_element(*HomePage1.FirstName)

    def getLastName(self):
        return self.driver.find_element(*HomePage1.LastName)

    def getEmail2(self):
        return self.driver.find_element(*HomePage1.Email2)

    def getPhone(self):
        return self.driver.find_element(*HomePage1.Phone)

    def getNext(self):
        return self.driver.find_element(*HomePage1.Next)
