from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
url = 'https://jacobsconnect.jacobs.com/welcome'
# url = 'https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre'
# driver.get(url)
# Give it a 5 tries
myElem = None
counter = 1
while myElem == None:
    driver.get(url)
    delay = 15 # seconds
    try:
        # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "card-columns")))
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "j-header-wrap")))
        print("Page is ready!")
    except TimeoutException:
        print(str(counter) + ". Loading took too much time!")
        if counter > 5:
            break
        counter += 1

with open("C:/Users/tbieleni/Downloads/reports.csv", 'r') as myfile:
    for url in myfile.readlines():
        driver.get(url)
        delay = 10 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'daily_activity_csv')))
            # print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        button = driver.find_element_by_id('daily_activity_csv') # find report button
        button.click() # export report

time.sleep(10)
driver.quit()

# Open report list:
with open("C:/Users/tbieleni/Downloads/links.txt", 'a') as myfile:
    for i in range(len(links)):
        myfile.write(links[i]+','+reports[i]+'\n')

with open("C:/Users/tbieleni/Downloads/reports.csv", 'a') as myfile:
    for i in range(len(reports)):
        myfile.write(reports[i]+'\n')
