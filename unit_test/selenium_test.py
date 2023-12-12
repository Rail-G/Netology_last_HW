from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from fake_useragent import UserAgent

def web_wait(driver, wait_time = 1, by=By.XPATH, value=None):
    return WebDriverWait(driver, wait_time).until(expected_conditions.presence_of_element_located((by, value)))

edge = EdgeChromiumDriverManager().install()
edge_service = Service(executable_path=edge)

options = webdriver.EdgeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f'user-agent={UserAgent().edge}')

def sign_in_yandex(login, passw):
    driver = webdriver.Edge(service=edge_service, options=options)
    driver.get('https://passport.yandex.ru/auth/')
    driver.maximize_window()

    loggin = web_wait(driver, wait_time=20, value='//input[@name="login"]')
    loggin.clear()
    loggin = loggin.send_keys(login)
    loggin = web_wait(driver, wait_time=10, value='//div[@class="passp-button passp-sign-in-button"]')
    loggin.click()

    password = web_wait(driver, wait_time=20, value='//input[@name="passwd"]')
    password.clear()
    password = password.send_keys(passw)
    password = web_wait(driver, wait_time=10, value='//div[@class="passp-button passp-sign-in-button"]')
    password.click()
    
    return driver


