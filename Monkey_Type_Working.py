from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from time import sleep
from selenium.webdriver.chrome.options import Options

#keep open afterwards
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

#open and load chrome at the website 
keyboard = Controller()
driver = webdriver.Chrome(chrome_option)
driver.get('https://monkeytype.com/')


print('starting!')

#code for typing
while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
    
    #find the active word
    active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
    
    #find the specific letters
    letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
    print(letters)
    keyboard.type(letters)
    #sleep(0.02)
sleep(100)
print('done!')