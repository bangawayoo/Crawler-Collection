import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
import pandas as pd 
import re 

def crawler_(year, detailed=False):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; InteSl Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    cnt = 0 
    url_list = []
    temp_list = [] 
    main_url = 'https://movie.daum.net/boxoffice/yearly?year=' + str(year)
    url_prefix = 'https://movie.daum.net/'
    response = requests.get(main_url,headers=headers)
    
    def simple_crawl(response=response, temp_list=temp_list,main_url=main_url,cnt=cnt,url_list=url_list):

        body_table = bs(response.text,'lxml')
        poster_table = body_table.find_all('div',class_='wrap_movie')
        for poster in poster_table:
            url_list.append(poster.find('a',class_='name_movie #title')['href'])
            title = poster.find('a', class_='name_movie #title').text
            try:
                netizen_grade_table = poster.find('span',class_='wrap_grade grade_netizen').text
                netizen_grade = re.findall(r'[0-9]{2}',netizen_grade_table)
                netizen_grade = float(netizen_grade[0][1]+'.'+netizen_grade[1][1])
                critic_grade_table = poster.find('span',class_='wrap_grade grade_critic').text
                critic_grade_table = re.findall(r'[0-9]{2}', critic_grade_table)
                critic_grade = float(critic_grade_table[0][1] + '.'+critic_grade_table[1][1])
                open_date = poster.find('span',class_='info_state').text
                open_date = ''.join(re.findall(r'[0-9+.+]',open_date))
                temp_list.append([title,netizen_grade,critic_grade, open_date])
                cnt += 1
            except Exception as e :
                print(e,'Error at {} for {}'.format(cnt,title))
                temp_list.append([title,'NA','NA','NA'])
        return temp_list, url_list

    

    
    if response.status_code == 200:
        if detailed == True:
            temp_list,url_list = simple_crawl()
            df = pd.DataFrame(columns=['title','netizen_grade','critic_grade','open_date'],data = temp_list)
            print(len(df))
            print(len(url_list))
            df['url'] = url_list
            url_prefix='https://movie.daum.net'
            detailed_df = pd.DataFrame(columns= ['genere', 'audience_num', 'running_time','rated','director'])
            for idx,url in enumerate(url_list):
                url = url_prefix + url 
                sleep(randint(10,20))
                detailed_response = requests.get(url,headers=headers)
                body_table = bs(detailed_response.text,'lxml')
                try:
                    genere = body_table.find('dd',class_='txt_main').text
                except Exception as e :
                    print(e)
                    print('\n Genere: Error occured at {} for {}'.format(idx,url))
                    genere = 'NA'
                    
                try:
                    audience_num_url = 'https://movie.daum.net/moviedb/main/totalAudience.json?' + re.search(r'movieId=\d+',url).group()
                    audience_temp = requests.get(audience_num_url)
                    audience_num = re.search('totalAudience":"(\S+)"',audience_temp.text).group(1)
                except Exception as e:
                    print(e)
                    print("\n Audience: Error while finding totalAudience at {} for {}".format(idx,url))   
                try:
                    running_time_info = body_table.find_all('dd')[3].text
                    running_time = re.search(r'\d+',running_time_info).group(0)
                    rated = re.search(r', (\S+)',running_time_info).group(1)
                    director = body_table.find_all('dd')[4].text
                    director = director.replace('(감독)','')
                    director = re.search(r'[ㄱ-ㅣ가-힣\sㄱ-ㅣ가-힣]+',director).group()
                    director = re.sub('\\n|\\t','',director)
                except:
                    running_time,rated,director = 'NA','NA','NA'
                    print('Running Time,rated, director: Error occured at {} for {}'.format(idx,url))
                    
                detailed_df.loc[idx] = [genere, audience_num,running_time,rated,director]
            df = df.join(detailed_df)
        else:
            temp_list = simple_crawl()
            df = pd.DataFrame(columns=['title','netizen_grade','critic_grade','open_date'],data = temp_list)
            df['url'] = url_list
    return df

    