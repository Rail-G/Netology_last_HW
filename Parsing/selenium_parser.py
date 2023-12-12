import json
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from webdriver_manager.microsoft import EdgeChromiumDriverManager


useragent = UserAgent()

edge = EdgeChromiumDriverManager().install()
edge_service = Service(
    executable_path=edge
)

options = webdriver.EdgeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f"user-agent={useragent.edge}")

dict_list = []

def web_wait(driver, wait_second=1):
    return WebDriverWait(driver, wait_second)

def ec(web_wait, by, value):
    return web_wait.until(expected_conditions.presence_of_element_located((by, value)))

try:
    driver = webdriver.Edge(service=edge_service, options=options)
    url = "https://kazan.hh.ru/search/vacancy"
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)

    imput = web_wait(driver, 3)
    ec(imput, By.CSS_SELECTOR, ".supernova-navi-advanced-search-icon").click()

    text = web_wait(driver, 3)
    ec(text, By.XPATH, '//input[@data-qa="vacancysearch__keywords-input"]').send_keys("python")

    reg = web_wait(driver, 10)
    region = ec(reg, By.XPATH, '//input[@data-qa="advanced-search-region-add"]')
    ragions = ['Москва', 'Санкт-Петербург']
    for i in ragions:
        region.send_keys(i)
        time.sleep(1)

    cokkie_but = web_wait(driver, 15)
    ec(cokkie_but, By.XPATH, '//button[@data-qa="cookies-policy-informer-accept"]').click()

    button = web_wait(driver, 20)
    ec(button, By.XPATH, '//button[@class="bloko-button bloko-button_kind-primary bloko-button_scale-large bloko-button_stretched"]').click()

    vacancys = web_wait(driver, 1)
    vacancys = vacancys.until(expected_conditions.presence_of_all_elements_located((By.XPATH, '//a[@class="serp-item__title"]')))
    count = 0
    for i in vacancys:
        if count == 10:  # -- > Ограничения на количество окошек вакансии!
            break
        href = web_wait(driver, 10)
        href = ec(href, By.CLASS_NAME, "serp-item__title").get_attribute("href")
        i.click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
        descripton = web_wait(driver, 5)
        descripton = ec(descripton, By.XPATH, '//div[@class="vacancy-section"]')
        if "Django" in descripton.text or "Flask" in descripton.text:
            com = web_wait(driver, 5)
            com = ec(com, By.XPATH, '//div[@class="vacancy-company-details"]').text
            try:
                city = web_wait(driver, 5)
                city = ec(city, By.XPATH, '//a[@data-qa="vacancy-view-link-location"]').text
            except Exception as ex:
                city = web_wait(driver, 5)
                city = ec(city, By.XPATH, '//p[@data-qa="vacancy-view-location"]').text
            try:
                zp = web_wait(driver, 5)
                zp = ec(zp, By.XPATH, '//div[@data-qa="vacancy-salary"]').text
            except Exception as ex:
                zp = "Зарплата не указана"
            dict_ = {"City": city, "Salary": zp, "Company": com, "Link": href}
            dict_list.append(dict_)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        count += 1
    with open("gigafile.json", "w", encoding="utf-8") as file:
        json.dump(dict_list, file, ensure_ascii=False, indent=2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()