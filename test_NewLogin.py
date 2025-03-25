import re
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys

from Logger import BaseClass
from homePage import HomePage1


class TestTwo(BaseClass):

    def test_VendorR(self):
        time.sleep(5)


        # customer login page
        homepage = HomePage1(self.driver)
        # homepage.getEmail().send_keys("john.doe@hypermatica.com.dev3")
        username = "john.doe@hypermatica.com.dev3"  # Change this for testing
        # Regular expression for email validation
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if re.match(email_regex, username):
            homepage.getEmail().send_keys(username)
            print("Entered email:", username)
        else:
            print("Incorrect username")

        # homepage.getPassword().send_keys("Test@1234")
        password = "Test@1234"
        password_regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(password_regex, password):
            homepage.getPassword().send_keys(password)
            print("Valid password entered")
        else:
            print("Invalid password! (Must be at least 8 characters, include letters, numbers, and a special character)")
        
        homepage.getCheckBox().click()

        try:
            sign_in_button = homepage.getSignIn()  # Using the method from homePage.pygibe
            sign_in_button.click()
            time.sleep(3)  # Wait for any response
            print("Sign-in button clicked successfully!")
        except NoSuchElementException:
            print("Sign-in button not found!")
        print("Sign in successfully")
        time.sleep(3)

        # vendor request page

        actions = ActionChains(self.driver)

        # Test Data
        name = "jhon"
        vendor_type = "Some Vendor Type"
        business_case = "xyz"
        first_name = "brian"
        last_name = "lara"
        email2 = "Hello@gmail.com"
        phone = "7218296837"

        # Validation regex
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        phone_regex = r"^\d{10}$"
        name_regex = r"^[a-zA-Z]+$"

        # Click and scroll
        homepage.getclick().click()
        actions.send_keys(Keys.PAGE_DOWN).perform()

        # Validate and enter Name
        if re.match(name_regex, name):
            homepage.getName().send_keys(name)
            print("You Entered Correct Vendor Name")
        else:
            print("Invalid Name Format!")

        # Click Vendor Type
        homepage.getvendertype().click()
        homepage.getvendertypeselect().click()

        time.sleep(2)

        # Enter Business Case
        homepage.getBusinessCase().send_keys(business_case)

        # Validate and enter First Name
        if re.match(name_regex, first_name):
            homepage.getFirstName().send_keys(first_name)

        else:
            print("Invalid First Name Format!")

        time.sleep(2)

        # Validate and enter Last Name
        if re.match(name_regex, last_name):
            homepage.getLastName().send_keys(last_name)
        else:
            print("Invalid Last Name Format!")

        # Validate and enter Email
        if re.match(email_regex, email2):
            homepage.getEmail2().send_keys(email2)
            print("Correct Email")
        else:
            print("Invalid Email Format!")

        time.sleep(2)

        # Validate and enter Phone Number
        if re.match(phone_regex, phone):
            homepage.getPhone().send_keys(phone)
            print("Correct Phone Number")
        else:
            print("Invalid Phone Number! Must be 10 digits.")

        # Click Next
        homepage.getNext().click()
        time.sleep(2)

time.sleep(10)