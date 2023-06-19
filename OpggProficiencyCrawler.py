from selenium import webdriver
from bs4 import BeautifulSoup
import time
import traceback
import logging

driver = webdriver.Chrome()
driver.implicitly_wait(100)
count = 1
logging.basicConfig(filename="test.log", level=logging.ERROR)
with open("./temp_record.txt", "r") as file:
    line = file.readline().rstrip()
    while line:
        championName = line.split(",")[1]
        nickname = line.split(",")[0]
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


# 웹서버에 너무 짧은 시간에 많은 요청을 하면 429 too many requests 에러가 발생한다.
# 따라서 적당한 시간 간격을 두고 요청해야한다.
# 파이썬에서 한 라인을 얻어올때 마지막문자는 개행문자가 붙으므로 rstrip()으로 제거해준다.
# 파일을 open할때 가능한 as file에서 file의 이름을 각각 다르게 해준다. 같은 파일을 연다고 하더라도 다르게 해준다.
# 지고 이기는게 자명한 경우는 그나마 정확도가 있을법 하고, 애매한경우는 애매하게 예측될듯
# 레이어를 나눈다던지? 가지처럼
