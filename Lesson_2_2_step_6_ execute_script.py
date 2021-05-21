from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    numbX = browser.find_element_by_id("input_value")
    x = int(numbX.text)

    y=calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()



    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

   



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()