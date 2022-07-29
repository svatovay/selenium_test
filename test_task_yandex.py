from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://yandex.ru/')
search_field = driver.find_element(By.ID, 'text')
search_field.send_keys('Тензор')
waiter = WebDriverWait(driver, 5)
search_field_suggest = driver.find_element(By.XPATH, '//ul[contains(@id, "suggest-list-")]')
search_field.send_keys(Keys.ENTER)
search_result = driver.find_element(By.PARTIAL_LINK_TEXT, 'tensor.ru')  # нужно доделать!!
driver.quit()
