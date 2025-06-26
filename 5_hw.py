from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

def test_find_bunch_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    try:
        username_field = driver.find_element(By.NAME, "user-name")
        password_field = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login-button')
        assert username_field is not None
        assert password_field is not None
        assert submit_button is not None
        print('Элементы найдены')
    except NoSuchElementException:
        print('Элемент не найден')
        assert False