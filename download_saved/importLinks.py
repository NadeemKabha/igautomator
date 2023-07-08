from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def get_saved_links(userName:str,password:str):

# Open instagram and log-in
#   - Setup mobile mode to avoid captcha
    options = Options()
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/96.0.4664.45 Mobile Safari/537.36"
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)

#   - Install chrome driver
    service = Service(ChromeDriverManager().install())

#   - Start the session and open instagram
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.instagram.com/')
    time.sleep(3)

#   - Go to login page and log-in
    div_element = driver.find_element(By.XPATH,'//div[text()="Log in"]')
    div_element.click()
    time.sleep(3)
    elements=driver.find_elements(by=By.TAG_NAME, value= 'input')
    if  (elements[0].get_attribute("name")=='username' and elements[1].get_attribute("name")=='password'):
        userNameIn=elements[0]
        passwordIn=elements[1]
    else:
        raise Exception("Error parsing line 34")       
    try:
        userNameIn.send_keys(userName)
        passwordIn.send_keys(password)
        time.sleep(7)
        passwordIn.submit() 
        time.sleep(5)

    # Go to saved and import the reels links
        driver.get('https://www.instagram.com/terhalz/saved/')
        time.sleep(2)
        linkElements = driver.find_elements(By.XPATH,"//a[starts-with(@href, '/p/')]")
        links = [element.get_attribute("href") for element in linkElements]
        time.sleep(5)
        driver.close()
        
    except: 
        print("Error logging in")
        driver.close()

    return links