# 必須於window環境執行
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os


s = Service('chromedriver.exe')
browser = webdriver.Chrome(service=s)

url = 'https://quizlet.com/zh-tw'
browser.get(url)
buttons = browser.find_elements(By.TAG_NAME, 'button')
buttons[11].click()  # 登入

Account = 'pucsimst@gmail.com'
Password = 'pu123456'

forms = browser.find_elements(By.TAG_NAME, 'form')
inputs = forms[2].find_elements(By.TAG_NAME, 'input')
inputs[0].send_keys(Account)  # 輸入表單資料
inputs[1].send_keys(Password)  # 輸入表單資料
login = forms[2].find_element(By.TAG_NAME, 'button')
login.click()
time.sleep(3)


soup = BeautifulSoup(browser.page_source, 'html.parser')
cards = soup.find_all('div', {'class', 'UIBaseCardHeader-title'})
print("\n ================== 近期學習集 ==================")
for i in range(len(cards)):
    card = cards[i].find('h4')
    print("(%d)" % (i+1), card.text)

# 暂停執行,以免彈出视窗消失
os.system("pause")
