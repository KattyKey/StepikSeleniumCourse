import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

link_set =[
"https://stepik.org/lesson/236895/step/1"  ,
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
] 

@pytest.mark.parametrize('link_data', link_set)
def test_data_from_links(browser, link_data):
    browser.get(link_data)
    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(2)
    text = browser.find_element_by_class_name("ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(
        str(answer))
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()
    result = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    assert "Correct!"==str(result.text), "Wrong answer!"


