from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

keywords = "CFD, CAE, Thermal, fluid, simulation, heat"
service = Service(executable_path="chromedriver.exe")

# Set Chrome options for headless mode
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://jobs.man-es.com/go/us_Job-Portal/4382201/")

try:
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    # Click on the "Accept All Cookies" button
    accept_cookies_button.click()
except Exception as e:
    print("Could not find or click on the 'Accept All Cookies' button:", e)


#city_dropdown = driver.find_element(By.ID, "optionsFacetsDD_city")
#city_select = Select(city_dropdown)
#city_select.select_by_value("Zürich")

#fct_dropdown = driver.find_element(By.ID, "optionsFacetsDD_customfield2")
#fct_select = Select(fct_dropdown)
#fct_select.select_by_value("Engineering")
input_keywords = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "keywordsearch-q.columnized-search")))
input_keywords.clear()
input_keywords.send_keys(keywords + Keys.ENTER)

#jobs = driver.find_elements(By.CLASS_NAME, "jobTitle-link.fontcolora880bb1b")

#jobs = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "jobTitle-link.fontcolora880bb1b")))
try:
    jobs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.jobTitle-link.fontcolora880bb1b"))
    )
    
    # Extract and print job titles
    for job in jobs:
        title = job.text.strip()
        if title:
            print(title)

except Exception as e:
    print("Failed to find job elements:", e)


time.sleep(10) 
driver.quit()