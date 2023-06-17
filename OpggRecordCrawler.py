from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# proficiencyUrl = f'https://www.op.gg/summoners/kr/{line}/champions'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 100)

with open("./ids.txt", "r") as file:
    userName = file.readline()
    while userName:
        recordUrl = f"https://www.op.gg/summoners/kr/{userName}"
        driver.get(recordUrl)
        wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#content-container > div.css-150oaqg.e1shm8tx0 > div.css-164r41r.e1r5v5160",
                )
            )
        )
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "li.css-1qq23jn.e1iiyghw3")
            )
        )
        time.sleep(3)
        gameList = driver.find_element(
            By.CSS_SELECTOR,
            "#content-container > div.css-150oaqg.e1shm8tx0 > div.css-164r41r.e1r5v5160",
        )
        records = gameList.find_elements(By.CSS_SELECTOR, "li.css-1qq23jn.e1iiyghw3")

        for li in records:
            wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "div:first-child > div.content > div > div.game > div.type",
                    )
                )
            )
            time.sleep(3)
            gametype = li.find_element(
                By.CSS_SELECTOR,
                "div:first-child > div.content > div > div.game > div.type",
            ).text
            isregame = li.find_element(
                By.CSS_SELECTOR, "div:first-child"
            ).get_attribute("result")

            if gametype == "솔랭" and isregame != "REMAKE":
                li.find_element(
                    By.CSS_SELECTOR, "div:first-child > div.action > button.detail"
                ).click()
                time.sleep(2)

                red = li.find_element(
                    By.CSS_SELECTOR,
                    "div.css-b7t7nt.e1769nho1 > div.css-1dm3230.eo0wf2y0 > table.css-4vxytv.e15ptgz10 > tbody ",
                )

                blue = li.find_element(
                    By.CSS_SELECTOR,
                    "div.css-b7t7nt.e1769nho1 > div.css-1dm3230.eo0wf2y0 > table.css-6ojc70.e15ptgz10 > tbody",
                )
                trs = red.find_elements(By.TAG_NAME, "tr")
                trs2 = blue.find_elements(By.TAG_NAME, "tr")

                for index, tr in enumerate(trs):
                    champ = tr.find_element(
                        By.CSS_SELECTOR, "td:first-child > a > div > img"
                    ).get_attribute("alt")
                    spell_1 = tr.find_element(
                        By.CSS_SELECTOR, "td.spells > div:first-child > img"
                    ).get_attribute("alt")
                    spell_2 = tr.find_element(
                        By.CSS_SELECTOR, "td.spells > div:nth-child(2) > img"
                    ).get_attribute("alt")
                    runes_1 = tr.find_element(
                        By.CSS_SELECTOR, "td.runes > div:first-child > img"
                    ).get_attribute("alt")
                    runes_2 = tr.find_element(
                        By.CSS_SELECTOR, "td.runes > div:nth-child(2) > img"
                    ).get_attribute("alt")
                    nickname = tr.find_element(By.CSS_SELECTOR, "td.name > a").text
                    result = tr.get_attribute("result")
                    r = (
                        result
                        + ","
                        + champ
                        + ","
                        + nickname
                        + ","
                        + spell_1
                        + ","
                        + spell_2
                        + ","
                        + runes_1
                        + ","
                        + runes_2
                    )
                    with open("./records.txt", "a") as file2:
                        file2.write(r)
                        file2.write("\n")

                for index, tr in enumerate(trs2):
                    champ = tr.find_element(
                        By.CSS_SELECTOR, "td:first-child > a > div > img"
                    ).get_attribute("alt")
                    spell_1 = tr.find_element(
                        By.CSS_SELECTOR, "td.spells > div:first-child > img"
                    ).get_attribute("alt")
                    spell_2 = tr.find_element(
                        By.CSS_SELECTOR, "td.spells > div:nth-child(2) > img"
                    ).get_attribute("alt")
                    runes_1 = tr.find_element(
                        By.CSS_SELECTOR, "td.runes > div:first-child > img"
                    ).get_attribute("alt")
                    runes_2 = tr.find_element(
                        By.CSS_SELECTOR, "td.runes > div:nth-child(2) > img"
                    ).get_attribute("alt")
                    nickname = tr.find_element(By.CSS_SELECTOR, "td.name > a").text
                    result = tr.get_attribute("result")
                    r = (
                        result
                        + ","
                        + champ
                        + ","
                        + nickname
                        + ","
                        + spell_1
                        + ","
                        + spell_2
                        + ","
                        + runes_1
                        + ","
                        + runes_2
                    )
                    with open("./records.txt", "a") as file2:
                        file2.write(r)
                        file2.write("\n")
        userName = file.readline()
        print(userName)
driver.close()
