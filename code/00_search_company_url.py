import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

import time

# import the driver
Driver_path="D:\workspace\chromedriver.exe"
driver=webdriver.Chrome(Driver_path)

# read excel file "SP500"
FILE_PATH="../data/SP500.xlsx"
data=pd.read_excel(FILE_PATH)
temp_data=data[["obs","comnam","indeed_url","indeed_name"]]

# clean the file
# delete INC or CORP
'''
for index, row in temp_data.iterrows():
    temp_name=row["comnam"]
    if "INC" in temp_name:
        temp_data.loc[index,"comnam"]=temp_name.split("INC")[0]
    elif "CORP" in temp_name:
        temp_data.loc[index,"comnam"] = temp_name.split("CORP")[0]
'''

# start searching from this URL
SEARCH_URL="https://www.indeed.com/companies"
driver.get(SEARCH_URL)

# search for every company and save the url to a list:
current_url=[]
i=1

# max: 0-723
for index, row in temp_data[350:723].iterrows():
    #get company name
    company_name=row["comnam"]

    # id for search box: use-uid-1-Input
    search = driver.find_element(By.ID, "use-uid-1-Input")

    #CLEAN THE PREVIOUS INPUT
    while search.get_attribute("value")!= "":
        search.send_keys(Keys.BACK_SPACE);

    search.send_keys(company_name)
    search.send_keys(Keys.RETURN)
    current_url.append(driver.current_url)

    time.sleep(3)
    print(i)
    i=i+1

print(current_url)
temp_dataFrame=pd.DataFrame(current_url)
temp_dataFrame.to_csv("temp-not-delete-url-2.csv")


'''

# beautiful soup
current_url=driver.current_url

driver.quit()


result=requests.get(current_url).text
doc=BeautifulSoup(result,"html.parser")
url_tag=doc.find(class_="css-18a7ohv-Link emf9s7v0")
print(url_tag.get("href"))
print(url_tag.div.get_text())



print("*********************finish*****************")



'''

