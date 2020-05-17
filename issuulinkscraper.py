from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time





url = str(input("Give the user profile in issuu: "))


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options,executable_path=r'C:\Users\%%USER%%\Desktop\linkconverter\geckodriver.exe')
# driver = webdriver.Firefox(executable_path=r'C:\Users\%%USER%%\Desktop\linkconverter\geckodriver.exe')

driver.get(url)

time.sleep(3)

# accept all cookies button
acceptcookies = driver.find_element_by_id("CybotCookiebotDialogBodyButtonAccept")
time.sleep(2)
acceptcookies.click()
time.sleep(5)
print("Cookies Accepted!")

temp =  url.split("/")
# clicks the load more button to expand it
count = 0;
while True:
    try:
        
        loadMoreButton = driver.find_element_by_xpath("//button[contains(.,'Load more')]")
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
        count += 1
        if (count%10 == 0):
            print("Clicked 'Load more' " + str(count) + " times")
    except Exception as e:
        print(e)
        break

print("Expansion completed!")
print("Clicked 'Load more' " + str(count) + " times")

elems = driver.find_elements_by_class_name("trms-Publication-cover")

# puts links into a file
linkcount = 0
filename = temp[-1] + ".txt"
with open(filename, "w") as outputfile: 
    for elem in elems:
        # print(elem.get_attribute('href')) #debug
        outputfile.write(elem.get_attribute('href') + "\n")
        linkcount += 1

print("Parsed " + str(linkcount) + " links!" )
driver.close()
