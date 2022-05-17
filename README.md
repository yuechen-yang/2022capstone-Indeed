# 2022capstone
This is the repo for the 2022 capstone project

- In the code folder contains the code for this project, which include the "EDA", "eikon", "model", "web-scraping", and "statstics".

# Background
There are many aspects that can influence the employees’ emotions during working, such as whether they have good benefits and whether they have friendly working environment. Some companies are willing to invest to their people because they think if their employees have good emotions during workday, they will work more effectively, and finally help the companies make more profits. However, whether this is true or not, we don’t know. This is why I have the motivation question for this project: Do firms who invest in their people have better financial performance than those who don’t? My initial hypothesis is yes for this motivation question. But whether my initial hypothesis is right or not, I need to do more exploration on it.

# File
- code
  -- EDA
    --- get_heatmap.ipynb: data cleaning and 2 heatmap, which are group by season and group by year
  -- eikon
    --- final_get_detail_data.ipynb: get the data from refinitive
  --model
    ---combine_zero_shot.ipynb: combine the different chunk of zero-shot  result together
    ---new-zero-shot classification.ipynb: the zero shot classification model
    ---sentiment_analysis_add_try_catch.ipynb: the sentiment analysis model
  --statstics
    --- cross-section-ana.ipynb get the cross-section-analysis result and calculate the p-vale
  --webscraping


  0_search_company_url.py: get the company in the searching page of Indeed
  1_get_company_url.py: get the companies' main page in the Indeed
  2_get_indeed_company_data.py: get the companies' detail data
  3_get_indeed_review.py: scrape the reviews
  5_get_grade.py: get the grade of every company
