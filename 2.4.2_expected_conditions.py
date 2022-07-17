import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(link)
    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(calc(x.text))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()

