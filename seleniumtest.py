from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

# https://stackoverflow.com/questions/45631715/downloading-with-chrome-headless-and-selenium
# Headless option
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://jacobsconnect.jacobs.com/groups/poland-innovation-council/")
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'group-analytics')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
driver.get("https://jacobsconnect.jacobs.com/groups/poland-innovation-council/group-reports.jspa?containerID=16796&containerType=700")
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'user_adoption_csv')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
button = driver.find_element_by_id('user_adoption_csv')
button.click()
print("I'm done")

# UI option
driver = webdriver.Chrome()
driver.get('https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/places')
delay = 30 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'group-analytics')))
    # print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

# Here goes link scrapper
a = driver.find_elements_by_xpath("//h4/a")
links = []
for  l in a:
    links.append(l.get_attribute('href'))
    
for link in links[:5]:
    driver.get(link)
    ca = driver.find_element_by_id("community-analytics")
    lnk = ca.get_attribute('href')
    driver.get(lnk) # go to report page
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'user_adoption_csv')))
        # print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    button = driver.find_element_by_id('daily_activity_csv') # find report button
    button.click() # export report



driver.get("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/scale-visual-management-system")
ca = driver.find_element_by_id("community-analytics")
link = ca.get_attribute('href')
driver.get(link) # go to report page
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'user_adoption_csv')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
button = driver.find_element_by_id('user_adoption_csv') # find report button
button.click() # export report

a = driver.find_elements_by_xpath("//h4/a")
for i in a:
    print(i.get_attribute('href'))

driver = webdriver.Chrome()
driver.get('https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/places')
thumbs = driver.find_elements_by_class_name('js-browse-thumbnail')
button = thumbs[0]
button.click()

button = driver.find_elements_by_id("community-analytics-tab")
button[0].click()

driver.get("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/delivering-in-a-different-world-diadw-menu")
import requests
from bs4 import BeautifulSoup
# page = requests.get("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/places")
page = requests.get("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/delivering-in-a-different-world-diadw-menu")
soup = BeautifulSoup(page.content, "lxml")
div = soup.find("div",attrs={"id":"j-browse-item-grid"})
li = div.find("ul").find_all("li")
soup = BeautifulSoup("https://jacobsconnect.jacobs.com/community/company/bldgs-infra/bi-europe/delivery-excellence/solution-centre/delivering-in-a-different-world-diadw-menu", 'html.parser')
ca = soup.find_all('a', id='community-analytics')
for div in soup.find_all('div'):
    print(div.get('id')) 