
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://barru.pythonanywhere.com/daftar')
web.find_element(By.ID, 'email').send_keys('batch16@gmail.com')
web.find_element(By.ID, 'password').send_keys('batch16')
web.find_element(By.ID, 'signin_login').click()
time.sleep(5)

# validation
popup_atas = web.find_element(By.ID, 'swal2-title').text
#Expectation
assert 'Welcome' in popup_atas

web.close()