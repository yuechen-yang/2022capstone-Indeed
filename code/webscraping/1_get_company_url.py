import pandas as pd

from bs4 import BeautifulSoup
import requests

import time

# import the url for the search result
FILE_PATH="not-delete-url.csv"
data=pd.read_csv(FILE_PATH)

# create a list to store all the scrape data
get_data=[]

# define a counter
i=1

# use loop to real every url and then get the url and company name
for index, rows in data[350:723].iterrows():
    current_url=rows['url']
    result=requests.get(current_url).text
    doc=BeautifulSoup(result,"html.parser")
    url_tag=doc.find(class_="css-18a7ohv-Link emf9s7v0")

    if url_tag==None: # there is no reached result
        get_data.append(["n/a", "n/a"])
    else:
        get_data.append([url_tag.get("href"),url_tag.div.get_text()])
    #print(url_tag.get("href"))
    #print(url_tag.div.get_text())
    time.sleep(5)
    i=i+1
    print(i-1)

re=pd.DataFrame(get_data)
re.to_csv("not-delete-name-2.csv")