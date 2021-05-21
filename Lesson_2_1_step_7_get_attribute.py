from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_tag_name("img")
    x =chest.get_attribute("valuex")

    y = calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

   



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()