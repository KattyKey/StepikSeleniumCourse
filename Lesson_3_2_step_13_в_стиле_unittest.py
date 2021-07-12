from selenium import webdriver
import time
import unittest
import pytest

class TestAbs(unittest.TestCase):

    def test1Page(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test2Page(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    if __name__ == "__main__":
        test1Page()
        test2Page()
        print("Everything passed")
        #unittest.main()
