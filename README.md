# 2022capstone
This is the repo for the 2022 capstone project

- In the code folder contains the code for this project, which include the "EDA", "eikon", "model", "web-scraping", and "statstics".

# Background
There are many aspects that can influence the employees’ emotions during working, such as whether they have good benefits and whether they have friendly working environment. Some companies are willing to invest to their people because they think if their employees have good emotions during workday, they will work more effectively, and finally help the companies make more profits. However, whether this is true or not, we don’t know. This is why I have the motivation question for this project: Do firms who invest in their people have better financial performance than those who don’t? My initial hypothesis is yes for this motivation question. But whether my initial hypothesis is right or not, I need to do more exploration on it.

# Code
All the code are in the code folder:  
00_search_company_url.py: get the company in the searching page of Indeed  
01_get_company_url.py: get the companies' main page in the Indeed  
02_get_indeed_company_data.py: get the companies' detail data  
03_get_indeed_review.py: scrape the reviews  
04_get_grade.py: get the grade of every company   
05_get_finacial_data.ipynb: get the data from refinitive
10_get_heatmap.ipynb: data cleaning and 2 heatmap, which are group by season and group by year  
20_zero-shot classification.ipynb: the zero shot classification model   
21_sentiment_analysis.ipynb: the sentiment analysis model
22_combine_zero_shot.ipynb: combine the different chunk of zero-shot  result together   
30_cross-section-ana.ipynb get the cross-section-analysis result and calculate the p-vale

# Result:
The result are in the "documnet/Yuechen Yang Oral-slide.pdf"

# Data
the data are in the google drive folder: https://drive.google.com/drive/folders/1zU-xPrFs4NSlG2FFKNb0ufqLVpy9Flwq
