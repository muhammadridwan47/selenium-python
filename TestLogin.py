import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self): # GLobal command to open browser
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_success_login(self): # test case
        browser = self.browser # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # open the site
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("dedeghulam@jagoqa.com") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("dedeghulam") # input email
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # click button signin
        time.sleep(1)

        # validation
        topPopup = browser.find_element(By.ID,"swal2-title").text
        bottomPopup = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', topPopup)
        self.assertEqual(bottomPopup, 'Anda Berhasil Login')

    def test_failed_login_with_wrong_password(self):
        browser = self.browser  # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # Open the site
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("dedeghulam@jagoqa.com") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("lorem") # input password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # click button signin
        time.sleep(1)

        # validation
        topPopup = browser.find_element(By.ID,"swal2-title").text
        bottomPopup = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", topPopup)
        self.assertEqual(bottomPopup, 'Email atau Password Anda Salah')

    def test_failed_login_with_invalid_email(self):
        browser = self.browser # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # Open the site
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("dedeghulam") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("lorem") # input password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()  # click button signin
        time.sleep(1)

        # validation
        email_component = browser.find_element(By.ID,"email")
        validationMessage = email_component.get_attribute("validationMessage");

        # expectation  
        self.assertIn("Please include an '@' in the email address. 'dedeghulam' is missing an '@'", validationMessage) # relative by your browser validationMessage

    def test_failed_login_with_max_char_in_email(self):
        browser = self.browser  # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # Open the site
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("loremipsumdolorsitametconsecteturadipisicingelit@jagoqa.com") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("lorem") # input password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # click button signin
        time.sleep(1)

        # validation
        topPopup = browser.find_element(By.ID,"swal2-title").text
        bottomPopup = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", topPopup)
        self.assertEqual(bottomPopup, "Email atau Password Anda Salah")


    def test_failed_login_with_empty_email(self):
        browser = self.browser  # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # Open the site
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("lorem") # input password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # click button signin
        time.sleep(1)

        # validation
        topPopup = browser.find_element(By.ID,"swal2-title").text
        bottomPopup = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", topPopup)
        self.assertEqual(bottomPopup, "Email atau Password Anda Salah")

    def test_failed_login_with_empty_password(self):
        browser = self.browser  # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # Open the site
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("dedeghulam@jagoqa.com") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # input password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # click button signin
        time.sleep(1)

        # validation
        topPopup = browser.find_element(By.ID,"swal2-title").text
        bottomPopup = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", topPopup)
        self.assertEqual(bottomPopup, "Email atau Password Anda Salah")


    def test_failed_login_with_empty_email_and_password(self):
        browser = self.browser  # Open the browser
        browser.get("http://barru.pythonanywhere.com/daftar") # Open the site
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("") # input email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # input password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # click button signin
        time.sleep(1)

        # validation
        topPopup = browser.find_element(By.ID,"swal2-title").text
        bottomPopup = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", topPopup)
        self.assertEqual(bottomPopup, "Email atau Password Anda Salah")

    def tearDown(self): # Global command to close browser
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
