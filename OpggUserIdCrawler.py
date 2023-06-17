from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

url = "https://www.op.gg/leaderboards/tier?page=1005"


driver = webdriver.Chrome()
driver.get(url)

tbody = driver.find_element(By.CSS_SELECTOR, '#content-container > div.css-ndvmk6.e1fnyy5m0 > table > tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

with open("./ids.txt", "a") as file:

    for elem in trs:
        file.write(elem.get_attribute('id') + '\n')
        

driver.close()