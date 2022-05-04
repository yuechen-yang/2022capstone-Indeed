
import pandas as pd

from bs4 import BeautifulSoup
import requests

import time
import datetime

# The data need:
date_scraped=None
company=None
Overall=None
work_happiness=None
Achievement=None
Appreciation=None
Flexibility=None
Support=None
Purpose=None
Energy=None
Compensation=None
Learning=None
Inclusion=None
Management=None
Trust=None
Belonging=None
Satisfaction=None
Stress_free=None
Salary_satisfaction=None

# read excel file to get the url for every company
URL_FILE_PATH="SP500.xlsx"
URL_data=pd.read_excel(URL_FILE_PATH)

# read the excel that we want to store the data in the future
#RESULT_FILE_PATH="Indeed Company Temp.xlsx"
#result_data=pd.read_excel(RESULT_FILE_PATH)
result_data=[]

# several function to get the url
def reach_snapshot(short_url): # A function to get the snapshot URL
    total_url="https://www.indeed.com"+short_url
    return total_url

def reach_salaries(short_url): # A function to get the reviews URL
    total_url="https://www.indeed.com"+short_url+"/salaries"
    return total_url

def get_grade_str(temp):
    temp_ls=[]
    if temp==None or len(temp)==0:
        return temp_ls
    for grade_item in temp:
        m=grade_item['aria-label']
        temp_ls.append(m)
    return temp_ls

def get_category(sentence):
    ls=sentence.split(',')
    return ls[0]

def get_grade(sentence):
    ls=sentence.split(',')
    temp=ls[2]
    return temp.split('out')[0]

# get the date
date_scraped=datetime.datetime.now().strftime('%Y/%m/%d')

i=0

for index, row in URL_data.iterrows():
    result_ls=[]

    #get the url
    short_url=row["indeed_url"]
    if short_url=='n/a':
        # store n/a
        continue

    snapshot_url=reach_snapshot(short_url)
    salaries_url=reach_salaries(short_url)

    # scrape the data from snapshot
    snapshot_text = requests.get(snapshot_url).text
    doc_snap = BeautifulSoup(snapshot_text, "html.parser")
    time.sleep(3)

    # company
    temp=doc_snap.find("div",{"itemprop":"name"})
    company = temp.get_text()

    # Overall
    temp = doc_snap.find(class_="css-1n6k8zn e1wnkr790")
    if temp==None:
        temp = doc_snap.find(class_="css-htn3vt e1wnkr790")
        if temp==None:
            overall = "n/a"
        else:
            overall = temp.get_text()
    else:
        overall = temp.get_text()

    temp_ls_str=[]
    temp=doc_snap.findAll(class_="css-ljcq1m e37uo190")
    temp_ls_str=get_grade_str(temp)

    if len(temp_ls_str)==0:
        continue

    result_ls.append(company)
    result_ls.append(overall)

    for j in temp_ls_str:
        cat=get_category(j)
        grade=get_grade(j)
        result_ls.append(cat)
        result_ls.append(grade)

    print(result_ls)
    # scrape the data from snapshot
    salaries_text = requests.get(salaries_url).text
    sal_snap = BeautifulSoup(salaries_text, "html.parser")
    time.sleep(3)

    temp = sal_snap.find(class_="cmp-SalarySatisfactionSidebarWidgetPieChart-inside")
    if temp==None:
        Salary_satisfaction = None
    else:
        Salary_satisfaction = temp.get_text()

    print(Salary_satisfaction)
    result_ls.append(Salary_satisfaction)

    result = pd.DataFrame(result_ls)
    result.T.to_csv("salaries_satisfaction.csv", mode='a', index=False, header=False, encoding='utf-8_sig')

