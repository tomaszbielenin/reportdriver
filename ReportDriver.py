# Add main page report
# Add try catch for report pages
# Add pages 2,3 from tool list

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

# UI option
driver = webdriver.Chrome()
url = 'https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/places'
myElem = None
counter = 1
while myElem == None:
    driver.get(url)
    delay = 15 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-browse-thumbnail')))
        print("Page is ready!")
    except TimeoutException:
        print(str(counter) + ". Loading took too much time!")
        if counter > 5:
            break
        counter += 1

# Here goes link scrapper
a = driver.find_elements_by_xpath("//h4/a")
links = []
for  l in a:
    links.append(l.get_attribute('href'))

# Loop through available pages and run report
for link in links: # [:3] set range for showcase
    driver.get(link)
    ca = driver.find_element_by_id("community-analytics")
    lnk = ca.get_attribute('href')
    driver.get(lnk) # go to report page
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'daily_activity_csv')))
        # print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    button = driver.find_element_by_id('daily_activity_csv') # find report button
    button.click() # export report

# driver.get("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/")
time.sleep(10)
driver.quit()

