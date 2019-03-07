from psaw import PushshiftAPI
import psaw

import datetime as dt
import pandas as pd
from time import sleep
from random import randint
from utils import *

def get_submission(start, before,search_term= None,subreddit='tea', filter=False):
    def date_changer(date):
        year = str(date)[:4]
        month = str(date)[4:6]
        day = str(date)[6:8]
        return int(dt.datetime(int(year),int(month),int(day)).timestamp())
    
    start_epoch = date_changer(start)
    before_epoch = date_changer(before)
    api = PushshiftAPI()
    gen = api.search_submissions(after=start_epoch, before=before_epoch, subreddit = subreddit, q= search_term)
    
    df= pd.DataFrame(columns=['ID','title','body','author','URL','num_comments','date'])
    for idx, g in enumerate(gen):
            temp_date = time.strftime('%Y-%m-%d', time.localtime(g.created_utc))
            if idx % 100 == 0:
                print('Crawling post {}'.format(idx))
            try :
                text = g.selftext
            except:
                text = 'NA'
            df.loc[idx] = [g.id, g.title, text, g.author,g.full_link, g.num_comments, temp_date]
    
    if filter:
		cnt =0
		temp_idx = []
		for idx, a in enumerate(list(df['title'])):
			if 'green' in a or 'green' in df['body'].iloc[idx]:
				temp_idx.append(idx)
				cnt += 1
		print('Relevant posts: {} out of {}'.format(cnt,len(df))
		corrected_df = df.iloc[temp_idx]
		return correct_df

    return df 

def get_comments(sub_df):
	comment_df =pd.DataFrame(columns=['id','body','date','link_id','parent_id']) 
	df_idx = 0
	sub_id = list(sub_df['ID'])
	for cnt,a in enumerate(sub_id):  
		id_list = api._get_submission_comment_ids(a)
		print('Crawling : ' + 'submission '+ str(cnt+1))
		try:
			for idx, id_ in enumerate(id_list):
				if len(id_list) > 10 : 
					print('----------------Crawled {} out of {}'.format(idx+1,len(id_list)))
				url ='https://api.pushshift.io/reddit/comment/search?ids='
				url +=str(id_)
				res = requests.get(url).json()
				temp = '{'+str(res['data'])[2:-2]+'}'
				temp_dict= ast.literal_eval(temp)
				temp_date = time.strftime('%Y-%m-%d', time.localtime(temp_dict['created_utc']))
				comment_df.loc[df_idx] = [temp_dict['id'],temp_dict['body'],temp_date, temp_dict['link_id'], temp_dict['parent_id']]
				df_idx +=1
		except Exception as e:
			save_as_json(comment_df,'wagyu/comment_'+str(df_idx))
			log_cnt = cnt
			print('-------------------Interrupted at submission {} comment {}'.format(cnt+1,idx+1))
			print(e)
			break 
	save_as_json(comment_df,'comments_'+str(df_idx))
	return comment_df 