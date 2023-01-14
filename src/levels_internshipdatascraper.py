from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import os

#please install selenium via pip
#also do this -> pip install webdriver-manager

# Options and Setting Chromium Driver
# options = Options()
#options.headless = True # Doesnt open window

url = "https://www.levels.fyi/internships/"
#DRIVER_PATH = input("fuck butt: ")
#driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
#from selenium import webdriver

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    print("please install selenium via pip \n")
    print("also do this -> pip install webdriver-manager \n")
    print("please look at docs to make sure all of the dependencies are properly downloaded")
    exit()
# Scraping
driver.get(url)

# Waits for page to load and retrieves the table
table = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.ID,"internships-table"))

# Goes through each entry and prints the name 
# Edge case tr not holding a name but is an advert (hence try catch)

# this creates a text file in both linux/Mac computers and Windows Computers
try:
    subprocess.run("touch internshipdata.txt", shell=True)
except:
    subprocess.run("touch internshipdata.txt", shell=False)
karp = open("internshipdata.txt", "w")


# Goes through each entry and adds name to text file
# Edge case tr not holding a name but is an advert (hence try catch)
for entry in table.find_elements(By.TAG_NAME, "tr"):
    try:
        tmp = entry.find_element(By.TAG_NAME,"h6").text
        print(tmp)
        karp.write(tmp)
        karp.write('\n')
        #subprocess.run([["echo"], [tmp]]) #, [">>"], [" internshipdata.txt"]])
    except:
        print("Failure")
        continue
karp.close()
driver.quit()
