import pandas as pd

from bs4 import BeautifulSoup
import requests

import time
import datetime

# The data need:
date_scraped=None
company=None
work_happiness_1=None
overall=None
reviews=None
salaries=None
jobs=None
Q_and_A=None
Photos=None
first_category=None
second_category=None
third_category=None
ceo=None
ceo_approval=None
founded=None
company_size=None
revenue=None
industry=None
job_cat_1_name=None
job_cat_1_num=None
job_cat_2_name=None
job_cat_2_num=None
job_cat_3_name=None
job_cat_3_num=None
job_cat_4_name=None
job_cat_4_num=None
job_cat_5_name=None
job_cat_5_num=None
Rating_2018=None
Rating_2019=None
Rating_2020=None
Rating_2021=None
Rating_2022=None
Work_and_Life_Balance=None
Compensation_and_Benefits=None
Job_Security_and_Advancement=None
Management=None
Culture=None
People_viewed_1=None
People_viewed_2=None
People_viewed_3=None
People_viewed_4=None

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

def reach_reviews(short_url): # A function to get the reviews URL
    total_url="https://www.indeed.com"+short_url+"/reviews"
    return total_url

# get the date
date_scraped=datetime.datetime.now().strftime('%Y/%m/%d')

i=0

for index, row in URL_data[0:3].iterrows():
    #get the url
    short_url=row["indeed_url"]
    if short_url=='n/a':
        # store n/a
        continue

    snapshot_url=reach_snapshot(short_url)
    review_url=reach_reviews(short_url)

    # scrape the data from snapshot
    snapshot_text = requests.get(snapshot_url).text
    doc_snap = BeautifulSoup(snapshot_text, "html.parser")

    # company
    temp=doc_snap.find("div",{"itemprop":"name"})
    company = temp.get_text()

    # work_happiness_1: css-dzahvu e1wnkr790
    temp=doc_snap.find(class_="css-dzahvu e1wnkr790")
    if temp==None:
        work_happiness_1="n/a"
    else:
        work_happiness_1 = temp.get_text()

    # overall : css-1n6k8zn e1wnkr790
    temp = doc_snap.find(class_="css-1n6k8zn e1wnkr790")
    if temp==None:
        overall="n/a"
    else:
        overall = temp.get_text()

    # salaries: css-r228jg eu4oa1w0
    temp = doc_snap.find("li",{"data-tn-element":"salaries-tab"})
    if temp.a.div == None:
        salaries="n/a"
    else:
        salaries = temp.a.div.get_text()

    # jobs: css-r228jg eu4oa1w0
    temp = doc_snap.find("li",{"data-tn-element":"jobs-tab"})
    if temp.a.div == None:
        jobs="n/a"
    else:
        jobs = temp.a.div.get_text()

    # Q_and_A
    temp = doc_snap.find("li",{"data-tn-element":"qna-tab"})
    if temp.a.div == None:
        Q_and_A="n/a"
    else:
        Q_and_A = temp.a.div.get_text()

    # Photos
    temp = doc_snap.find("li",{"data-tn-element":"photos-tab"})
    if temp.a.div == None:
        Photos="n/a"
    else:
        Photos = temp.a.div.get_text()

    # get three categories
    temp = doc_snap.findAll("div", {"class": "css-19akx1r e1wnkr790"})
    # first_category
    if temp!=None and len(temp)>=1:
        first_category = temp[0].get_text()
    else:
        first_category="n/a"

    # second_category
    if temp!=None and len(temp)>=2:
        second_category = temp[1].get_text()
    else:
        second_category="n/a"

    # third_category
    if temp!=None and len(temp)>=3:
        third_category = temp[2].get_text()
    else:
        third_category="n/a"

    # ceo
    temp = doc_snap.find("div", {"data-testid": "CeoWidget-title"})
    if temp==None:
        ceo='n/a'
    else:
        temp = temp.div.next_sibling
        ceo = temp.span.get_text()

    # ceo_approval
    temp = doc_snap.find("span", {"class": "css-4oitjw e1wnkr790"})
    if temp==None:
        ceo_approval='n/a'
    else:
        ceo_approval = temp.get_text()

    # founded
    temp = doc_snap.find("li", {"data-testid": "companyInfo-founded"})
    if temp==None:
        founded='n/a'
    else:
        temp = temp.div.next_sibling
        founded = temp.get_text()

    # company_size
    temp = doc_snap.find("li", {"data-testid": "companyInfo-employee"})
    if temp==None:
        company_size='n/a'
    else:
        company_size = temp.div.next_sibling.div.span.get_text()

    # revenue
    temp = doc_snap.find("li", {"data-testid": "companyInfo-revenue"})
    if temp==None:
        revenue='n/a'
    else:
        revenue = temp.div.next_sibling.div.span.get_text()

    # industry
    temp = doc_snap.find("li", {"data-testid": "companyInfo-industry"})
    if temp==None:
        industry='n/a'
    else:
        industry = temp.div.next_sibling.get_text()

    # find all 5 categories
    temp = doc_snap.findAll("div", {"class": "css-14dbjst e37uo190"})
    #1
    if temp!=None and len(temp)>=1:
        job_cat_1_name=temp[0].a.div.p.get_text()
        job_cat_1_num = temp[0].a.div.p.next_sibling.get_text().split(" ")[0]
    else:
        job_cat_1_name="n/a"
        job_cat_1_num="n/a"
    #2
    if temp!=None and len(temp)>=2:
        job_cat_2_name=temp[1].a.div.p.get_text()
        job_cat_2_num = temp[1].a.div.p.next_sibling.get_text().split(" ")[0]
    else:
        job_cat_2_name="n/a"
        job_cat_2_num="n/a"
    #3
    if temp!=None and len(temp)>=3:
        job_cat_3_name=temp[2].a.div.p.get_text()
        job_cat_3_num = temp[2].a.div.p.next_sibling.get_text().split(" ")[0]
    else:
        job_cat_3_name="n/a"
        job_cat_3_num="n/a"
    #4
    if temp!=None and len(temp)>=4:
        job_cat_4_name=temp[3].a.div.p.get_text()
        job_cat_4_num = temp[3].a.div.p.next_sibling.get_text().split(" ")[0]
    else:
        job_cat_4_name="n/a"
        job_cat_4_num="n/a"
    #5
    if temp!=None and len(temp)>=5:
        job_cat_5_name=temp[4].a.div.p.get_text()
        job_cat_5_num = temp[4].a.div.p.next_sibling.get_text().split(" ")[0]
    else:
        job_cat_5_name="n/a"
        job_cat_5_num="n/a"

    # get rating for 4 years:
    temp = doc_snap.findAll("g", {"class": "css-a50thi eu4oa1w0"})
    #2021
    if temp !=None and len(temp)>=1:
        Rating_2021=round(float(temp[-1].text),2)
    else:
        Rating_2021="n/a"
    #2020
    if temp !=None and len(temp)>=2:
        Rating_2020=round(float(temp[-2].text),2)
    else:
        Rating_2020="n/a"
    #2019
    if temp !=None and len(temp)>=3:
        Rating_2019=round(float(temp[-3].text),2)
    else:
        Rating_2019="n/a"
    #2018
    if temp !=None and len(temp)>=4:
        Rating_2018=round(float(temp[-4].text),2)
    else:
        Rating_2018="n/a"

    #2022
    temp = doc_snap.find("g", {"class": "css-je7s01 eu4oa1w0"})
    if temp !=None and len(temp)>=4:
        Rating_2022=round(float(temp.text), 2)
    else:
        Rating_2022="n/a"

    # get the 5 categories
    temp = doc_snap.findAll("span", {"class": "css-1qdoj65 e1wnkr790"})

    # Work_and_Life_Balance
    if temp!=None and len(temp)>=1:
        Work_and_Life_Balance=temp[0].get_text()
    else:
        Work_and_Life_Balance='n/a'

    # Compensation_and_Benefits
    if temp!=None and len(temp)>=2:
        Compensation_and_Benefits=temp[1].get_text()
    else:
        Compensation_and_Benefits='n/a'

    # Job_Security_and_Advancement
    if temp!=None and len(temp)>=3:
        Job_Security_and_Advancement=temp[2].get_text()
    else:
        Job_Security_and_Advancement='n/a'

    # Management
    if temp!=None and len(temp)>=4:
        Management=temp[3].get_text()
    else:
        Management='n/a'

    # Culture
    if temp!=None and len(temp)>=5:
        Culture=temp[4].get_text()
    else:
        Culture='n/a'

    # get people also viewed
    temp = doc_snap.findAll("div", {"class": "css-p7qhch eu4oa1w0"})

    # People_viewed_1
    if temp !=None and len(temp)>=1:
        People_viewed_1 =temp[0].get_text()
    else:
        People_viewed_1='n/a'

    # People_viewed_2
    if temp !=None and len(temp)>=2:
        People_viewed_2 =temp[1].get_text()
    else:
        People_viewed_2='n/a'

    # People_viewed_3
    if temp !=None and len(temp)>=3:
        People_viewed_3 =temp[2].get_text()
    else:
        People_viewed_3='n/a'

    # People_viewed_4
    if temp !=None and len(temp)>=4:
        People_viewed_4 =temp[3].get_text()
    else:
        People_viewed_4='n/a'


    # go to review section to get the number of review:
    reviews = None
    review_text = requests.get(review_url).text
    doc_review = BeautifulSoup(review_text, "html.parser")

    temp = doc_review.find("a", {"data-tn-element": "reviews-viewAllLink"})
    if temp !=None:
        reviews=temp.text.split(" ")[2]
    else:
        reviews='n/a'

    time.sleep(5)

    i=i+1
    print(i)

    # store in the dataframe
    #result_data.loc["date scraped",index]=date_scraped
    #result_data.loc["company", index] = company
    #result_data.loc["work happiness 1", index] = work_happiness_1
    temp_result=[date_scraped,company,work_happiness_1,overall,reviews,salaries,jobs,Q_and_A,Photos,first_category,second_category,third_category,ceo,ceo_approval,founded,company_size,revenue,industry,job_cat_1_name,job_cat_1_num,job_cat_2_name,job_cat_2_num,job_cat_3_name,job_cat_3_num,job_cat_4_name,job_cat_4_num,job_cat_5_name,job_cat_5_num,Rating_2018,Rating_2019,Rating_2020,Rating_2021,Rating_2022,Work_and_Life_Balance,Compensation_and_Benefits,Job_Security_and_Advancement,Management,Culture,People_viewed_1,People_viewed_2,People_viewed_3,People_viewed_4]

    result=pd.DataFrame(temp_result)
    result=pd.DataFrame(result.values.T)
    result.to_csv("123.csv",mode='a',index=False,header=False,encoding='utf-8')




