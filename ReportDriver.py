# x Add main page report
# x Add try except for report pages
# Add 'if not exist create download folder'
# Add purge download folder
# Add fail log
# How to modify download folder
# Headless option

#Get ready:

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import os

# Creates dowload path:
downloadPath = 'C:\\Users\\tbieleni\\Downloads\\JCReports'
if not os.path.exists(downloadPath):
    os.makedirs(downloadPath, exist_ok=True)

# Purges old files:
for f in os.listdir(downloadPath):
    os.remove(downloadPath+'\\'+f)

# UI option

#  Sets download path for Chrome
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : downloadPath}
options.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(chrome_options=options, executable_path=CHROMEDRIVER_PATH)
# chrome_options = webdriver.ChromeOptions()
# prefs = {'download.default_directory' : 'C:/Users/tbieleni/Downloads/JCReports'}
# chrome_options.add_experimental_option('prefs', prefs)

# Starts AU Chrome
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
url = 'https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre'
# url = 'https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/places'
driver.get(url)
links = [url]

# Give it a 5 tries
myElem = None
counter = 1
while myElem == None:
    driver.get(url)
    delay = 15 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "widgetIframe2484049")))
        print("Page is ready!")
    except TimeoutException:
        print(str(counter) + ". Loading took too much time!")
        if counter > 5:
            break
        counter += 1

# Get Solutions frame and solution links
f = driver.switch_to_frame('widgetIframe2484049')
a = driver.find_elements_by_xpath("//div[@id='solution-name']/a")
# a = driver.find_elements_by_xpath("//h4/a")
# links = []
for  e in a:
    links.append(e.get_attribute('href'))

# Loop through available pages and run report
reports = []
for l in links: # [:3] set range for showcase
    driver.get(l)
    ca = driver.find_element_by_id("community-analytics")
    lnk = ca.get_attribute('href')
    reports.append(lnk)

for r in reports: # [:5]
    driver.get(r) # go to report page
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'daily_activity_csv')))
        # print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    button = driver.find_element_by_id('daily_activity_csv') # find report button
    button.click() # export report

driver.get("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/")
# time.sleep(10)
# driver.quit()

