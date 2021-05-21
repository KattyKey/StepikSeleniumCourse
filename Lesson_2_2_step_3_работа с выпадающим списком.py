from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    numbA = browser.find_element_by_id("num1")
    A = int(numbA.text)
    numbB = browser.find_element_by_id("num2")
    B = int(numbB.text)
    res = A+B

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(res))


    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

   



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()