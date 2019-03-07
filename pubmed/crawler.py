import selenium 
from random import randint
from time import sleep

browser.get(your_url) #'https://www.ncbi.nlm.nih.gov/pubmed/?term=obesity%2C+mice'

"""Choose advanced search options 
Code not needed if using default option.
This can also be done manually in your browser."""
abstract_only_button = browser.find_element_by_css_selector('#_simsearch > li > ul > li:nth-child(1) > a')
abstract_only_button.click()

url_list= []
title = []
""" Change display options to 100 papers"""
# Looping over 5 pages 
for page in range(5):
    sleep(randint(1,5)) #Randomly sleep for 1-5 seconds 
    temp_list = []
    if page == 0:
        a = browser.find_elements_by_class_name('rprt')
        for i in a:
            post = i.find_elements_by_tag_name('a')
            temp_list.append(post[0].get_attribute('href'))

        url_list.append(temp_list)
        next_button = browser.find_element_by_xpath('//*[@id="EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_Pager.Page"]')
        next_button.click()
        if True:
            continue
    else:
        a = browser.find_elements_by_class_name('rprt')
        temp_list = []
        for i in a:
            post = i.find_elements_by_tag_name('a')
            temp_list.append(post[0].get_attribute('href'))
        url_list.append(temp_list)
        next_button = browser.find_elements_by_xpath('//*[@id="EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_Pager.Page"]')
        next_button[2].click()
        if True:
            continue
        

# Flatten URL list to 1-D list
url_list = [item for sublist in url_list for item in sublist ]


#Requesting for URL of each paper 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


sleep(10) # Sleep for 10 seconds before requesting specific URL
df = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; InteSl Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
cnt = 0 
for idx, main_url in enumerate(url_list):
    response = requests.get(main_url,headers=headers)
    sleep(randint(20,30)) # Sleep 20-30 seconds
    if response.status_code == 200:
        body = bs(response.text,'lxml')
        try:
            abstract = body.find('div',class_='abstr')
            title = body.find('div', class_='rprt abstract').find('h1').text
            abstract = abstract.find('p').text
        except Exception as e:
            print('Error at {}'.format(idx))
            print(e)
            title = 'na'
            abstract = 'na'
        df.append([abstract,title])
		
		
# Save dataframe with ['abstract','title','URL']		
import pandas as pd

for j,i in enumerate(df):
    i.append(url_list[j])
output = pd.DataFrame(data=df, columns=['abstract','title','url'])
output.to_csv(output_dir)