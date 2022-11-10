from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time

driver = webdriver.Firefox()
driver.get("https://www.drfrostmaths.com/timestables-game.php")
driver.implicitly_wait(20)

start_button = driver.find_element(By.ID, "question")
start_button.click()
print("Timer started.")

try:
    while True:
        question = start_button.text
        tokens = question.split(" ")
        operand_1, operator, operand_2 = tokens[0], tokens[1], tokens[2]
        input_box = driver.find_element(By.ID, "calculator-display")
        if operator == "÷":
            result = int(int(operand_1) / int(operand_2))
            input_box.send_keys(str(result) + Keys.ENTER)
        elif operator == "×":
            result = int(int(operand_1) * int(operand_2))
            input_box.send_keys(str(result) + Keys.ENTER)
        input_box.send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
        time.sleep(0.25)
except ElementNotInteractableException:
    print("Timer finished.")