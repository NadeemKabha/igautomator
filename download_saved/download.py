from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
import time

def download_reels(videoLib,urls,i=0):
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    for reel_url in urls:
         
        driver.get(reel_url)
        time.sleep(5)
        elements = driver.find_elements(By.TAG_NAME, "video")

        try:
            vid_url = elements[-1].get_attribute("src")
            print(f'Downloading {i}.mp4')
            urllib.request.urlretrieve(vid_url, f"{videoLib}/{i}.mp4")
            i+=1
        except:
            print("Error downloading video")
        time.sleep(2)        
    
    driver.quit()

    return i
