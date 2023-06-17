from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

with open("./records.txt", "r") as file:
    line = file.readline()
    while line:
        s = line.split(",")
        url = f"https://www.op.gg/summoners/kr/{s[2]}/champions"
