from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os

#launch url
url = "https://libertyvf.tv/series/"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

#After opening the url above, Selenium clicks the specific series link

python_button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div[2]/a")
python_button.click()

soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 0 #counter

for link in soup_level1.find_all('a', id=re.compile("//a[@class=num_'episode']")):
    
    #Selenium visits each episode page
    python_button = driver.find_element_by_class_name("//a[@class=num_'episode']" + str(x) )
    python_button.click() #click link
    
    #Selenium hands of the source of the specific episode page to Beautiful Soup
    soup_level2=BeautifulSoup(driver.page_source, 'lxml')

    #Beautiful Soup grabs the HTML div on the page
    soup_level2.find_all("div", {"class": "divstreaming"})[0]
    
    #Ask Selenium to click the back button
    driver.execute_script("window.history.go(-1)") 
    
    #increment the counter variable before starting the loop over
    x += 1

#end the Selenium browser session
driver.quit()
