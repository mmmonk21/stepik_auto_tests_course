from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button1 = browser.find_element(By.ID, "price")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    button2 = browser.find_element(By.ID, "book")
    button2.click()
    
    button3 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
    
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
     
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button3.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла