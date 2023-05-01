import requests
import time
from bs4 import BeautifulSoup
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
#これがエラーをなくすコードです。ブラウザ制御コメントを非表示化しています
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
driver = webdriver.Chrome(options=options)  


url = 'https://www.nipponrentacar.co.jp/'
driver.get(url)
time.sleep(3)

fromStore = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div/form/div/div[2]/div[1]/div/div[1]/div/input[1]")

fromStore.click()
time.sleep(1)

store = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[14]/div/div/div/div/div/div[2]/div[1]/input")
time.sleep(1)

store.send_keys("恵比寿")
time.sleep(1)

search_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[14]/div/div/div/div/div/div[2]/div[1]/span[2]/a")
search_btn.click()
time.sleep(1)

store_selector = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[14]/div/div/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td/a")
time.sleep(1)

store_selector.click()
time.sleep(1)

####店舗選択処理の終了####

start_time = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div/form/div/div[2]/div[1]/div/div[2]/input")
start_time.click()
time.sleep(1)
date = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[13]/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/a")
date.click()
time.sleep(1)

kakutei = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[13]/div/div/div/div/div/div[2]/div/div[4]/div/a")
kakutei.click()
time.sleep(1)


time_selector = Select(driver.find_element(By.ID, "searchCalendarMenuTime"))
time_selector.select_by_index(27)
time.sleep(3)

kakutei.click()
time.sleep(1)

serach_vacancy_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div/form/div/div[2]/div[3]/p/a")
serach_vacancy_btn.click()

time.sleep(5)


result_url = driver.current_url
result_response = requests.get(result_url)
soup = BeautifulSoup(result_response.content, "html.parser")

list = soup.find_all(class_="ys0020-table-02-body selectChargeContents")

print(list)

