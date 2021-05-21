from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputFirst = browser.find_element_by_name("firstname")
    inputFirst.send_keys("Ivan")

    inputSec = browser.find_element_by_name("lastname")
    inputSec.send_keys("Ivanov")

    inputMail = browser.find_element_by_name("email")
    inputMail.send_keys("Ivan@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()