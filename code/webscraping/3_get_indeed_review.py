import pandas as pd

from bs4 import BeautifulSoup
import requests

import time
import datetime

import math



# The data we need:
date_scraped=None
company=None
role=None
location=None
rating=None
review_title=None
review_text=None
review_date=None

# read excel file to get the url for every company
URL_FILE_PATH="SP500.xlsx"
URL_data=pd.read_excel(URL_FILE_PATH)

result_data=[]

# functions
# several function to get the url
def reach_reviews(short_url): # A function to get the reviews URL
    total_url="https://www.indeed.com"+short_url+"/reviews"
    return total_url

# get html scrap document:
def get_doc_page(review_url):
    review_text = requests.get(review_url).text
    doc_review = BeautifulSoup(review_text, "html.parser")
    # sleep
    time.sleep(5)
    return doc_review

# get the number of start review:
def get_start(current_page):
    temp=(current_page-1)*20
    return temp

# get the url to every page:
def get_page_url(short_url,start_review):
    page_url="https://www.indeed.com"+short_url+"/reviews?start="+str(start_review)
    print(page_url)
    return page_url

# company
def get_company(doc_review):
    temp = doc_review.find("div", {"itemprop": "name"})
    company = temp.get_text()
    return company

# get review section
def get_review_section(doc_review):
    review_section=doc_review.findAll("div", {"data-tn-entitytype": "reviewId"})
    return review_section

# role
def get_role(review_section,num):
    temp=review_section[num].div.next_sibling.div.span.a
    if temp==None:
        return "n/a"
    else:
        return review_section[num].div.next_sibling.div.span.a.text

# location
def get_location_date(review_section,num):
    temp= review_section[num].div.next_sibling.div.span.text
    return [temp.split("-")[-2].strip(),temp.split("-")[-1].strip()]

# rating
def get_rate(review_section,num):
    return review_section[num].div.div.meta['content']

# review_title
def get_review_title(review_section,num):
    return review_section[num].div.next_sibling.h2.text

# review_text
def get_review_text(review_section,num):
    temp=review_section[num].div.next_sibling.div.next_sibling
    # delete the /n and /r
    text_result=temp.text
    text_result=text_result.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")

    return text_result


'''
The first page has 21, and other has 20
'''
def get_num_of_page(reviews_number):# use the number of review to calculate the number of page:
    # change reviews_number to int
    page=1
    reviews_number=str(reviews_number)

    temp=""

    for i in reviews_number:
        if i!=",":
            temp=temp+i

    reviews_number=int(temp)
    if reviews_number<=21:
        return 1
    else:
        number=reviews_number-21
        temp=int(math.ceil(number/20.0))
        page=page+temp
        return page


# get the date
date_scraped=datetime.datetime.now().strftime('%Y/%m/%d')

# define a list to store the result
result=[]

company_num=0

# For every company:
for index, row in URL_data[0:3].iterrows():
    company_num=company_num+1
    #get the short url
    short_url=row["indeed_url"]
    if short_url=='n/a':
        # store n/a
        print(company_num)
        continue

    # change the short url to the long url:
    review_url = reach_reviews(short_url)

    #get the first review page
    doc_review = get_doc_page(review_url)

    # get the company
    company=get_company(doc_review)

    # get the total number of reviews:
    reviews_number = None
    temp = doc_review.find("span", {"class": "css-1cxc9zk e1wnkr790"})
    if temp!=None:
        temp_text=temp.get_text()
        if temp_text.split(" ")[0]=="Found":
            reviews_number = temp.text.split(" ")[1]
        elif temp_text.split(" ")[0]=="Showing":
            reviews_number = temp.text.split(" ")[2]
    else:
        reviews_number=0

    if reviews_number=="only":
        reviews_number=1

    # use the number of review to calculate the number of page:
    page=get_num_of_page(reviews_number)
    # based on the number of review: visit every page
    current_page=1

    while current_page<=page:
        result = []
        if current_page==1:
            # get the element
            review_section=get_review_section(doc_review)

            for num in range(1,len(review_section)):
                # role
                role=get_role(review_section,num)
                # location
                location=get_location_date(review_section,num)[0]
                # rating
                rating=get_rate(review_section,num)
                # review_title
                review_title=get_review_title(review_section,num)
                # review_text
                review_text=get_review_text(review_section,num)
                # review_date
                review_date = get_location_date(review_section, num)[1]

                result.append([date_scraped, company, role, location, rating, review_title, review_text])


        else:
            # get start review:
            start_review=get_start(current_page)
            page_url=get_page_url(short_url,start_review)
            # get doc
            doc_review=get_doc_page(page_url)
            # get the element
            review_section = get_review_section(doc_review)

            for num in range(1,len(review_section)):
                # role
                role=get_role(review_section,num)
                # location
                # rating
                rating=get_rate(review_section,num)
                # review_title
                review_title=get_review_title(review_section,num)
                # review_text
                review_text=get_review_text(review_section,num)
                # review_date
                result.append([date_scraped, company, role, location, rating, review_title, review_text,review_date])

        current_page=current_page+1

        print(str(company_num)+"****"+str(current_page-1))
        #save to the excel file
        result = pd.DataFrame(result)
        result.to_csv("review_test.csv", mode='a', index=False, header=False, encoding='utf-8_sig')

