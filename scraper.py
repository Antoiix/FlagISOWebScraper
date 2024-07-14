import os
import shutil
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.get("https://www.kaggle.com/datasets/zhongtr0n/country-flag-urls")
driver.implicitly_wait(10000)

print("----------------------------------------------------------------\n------------------ LAUNCH SCRAPER")

driver.find_element(By.CLASS_NAME, "sc-lexAlA.leRLjZ").click()
keys = driver.find_element(By.CLASS_NAME, "sc-lexAlA.leRLjZ")

print("--------- WAITING FOR THE WEBSITE")

for i in range(0, 340):
    keys.send_keys(Keys.ARROW_DOWN)

print("-------- SITE OK")

list = []

try:
    line = driver.find_elements(By.XPATH, "/html/body/main/div[1]/div/div[5]/div[2]/div/div[2]/div/div[5]/div[2]/div/div/div[1]/div/div[3]/div[6]/span")
    for block in line:
        current_block = [block.text.split("\n")[1], block.text.split("\n")[3]]
        list.append(current_block)
except Exception as ex:
    exit(10)

driver.quit()

try:
    os.mkdir("./flags_folder")
except Exception as ex:
    shutil.rmtree("./flags_folder")
    os.mkdir("./flags_folder")

for link in list:
    print(link[1], "./flags_folder/" + link[0] + ".png")
    urlretrieve(link[1], "./flags_folder/" + link[0] + ".png")

print("FLAGS DOWNLOADED")
