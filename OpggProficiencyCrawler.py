from selenium import webdriver
from bs4 import BeautifulSoup
import time
import traceback
import logging

driver = webdriver.Chrome()
driver.implicitly_wait(100)
count = 1
logging.basicConfig(filename="test.log", level=logging.ERROR)
with open("./heheeh.txt", "r") as file:
    line = file.readline().rstrip()
    while line:
        championName = line.split(",")[1]
        nickname = line.split(",")[2]
        url = f"https://www.op.gg/summoners/kr/{nickname}/champions"
        driver.get(url)
        time.sleep(8)
        try:
            soup = None
            trs = []
            soup = BeautifulSoup(driver.page_source, "html.parser")
            trs = soup.select("#content-container > div > table > tbody > tr")
            time.sleep(8)

            if trs == []:
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, "html.parser")
                trs = soup.select("#content-container > div > table > tbody > tr")
                time.sleep(16)

            win = ""
            lose = ""
            for elem in trs:
                cnn = elem.select_one("td:nth-child(2) > div.champion-container > div.summoner-name > a").text
                logging.critical(cnn)
                if championName == cnn:
                    logging.critical(championName + " == " + cnn)
                    ratio = elem.select_one("td:nth-child(3) > div.win-ratio > span").text
                    if ratio != "0%" and ratio != "100%":
                        win = elem.select_one("td:nth-child(3) > div.win-ratio > div.winratio-graph > div.winratio-graph__text.left").text
                        lose = elem.select_one("td:nth-child(3) > div.win-ratio > div.winratio-graph > div.winratio-graph__text.right").text
                    elif ratio == "0%":
                        win = "0승"
                        lose = elem.select_one("td:nth-child(3) > div.win-ratio > div.winratio-graph > div.winratio-graph__text.right").text
                    elif ratio == "100%":
                        win = elem.select_one("td:nth-child(3) > div.win-ratio > div.winratio-graph > div.winratio-graph__text.left").text
                        lose = "0패"
                    score = elem.select_one("td:nth-child(4) > div > strong").text
                    with open("./temp_proficiency.txt", "a") as file2:
                        file2.write(nickname + "," + championName + "," + win + "," + lose + "," + score)
                        file2.write("\n")
                    break

            if win == "" or lose == "":
                with open("./temp_proficiency.txt", "a") as file3:
                    file3.write(nickname + "," + championName + ",not found proficiency")
                    file3.write("\n")
        except Exception as e:
            with open("./temp_proficiency.txt", "a") as file4:
                file4.write(nickname + "," + championName + ",not found user")
                file4.write("\n")
            logging.critical(championName + " " + nickname + " " + str(count))
            logging.critical(traceback.format_exc())
            count += 1
            line = file.readline().rstrip()
            continue
        line = file.readline().rstrip()
        count += 1


