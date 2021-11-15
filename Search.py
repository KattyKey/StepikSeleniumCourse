

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "https://dev.bosscasino.com/en-row"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sp-overlay")))

    WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#ifrmCookieBanner")))
    add_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".intro-banner-btn"))).click()
    browser.switch_to.parent_frame()
    open_form = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-background.button-lg.orange"))).click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла