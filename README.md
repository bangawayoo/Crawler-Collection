# Crawler-Collection (Reddit, PubMed, Daum Movie)

This project includes collection of crawlers for _light-use_ purposes. 
As of now, it is intended to run on interactive IDE such as Jupyter Notebook rather than command prompt as it provides 
minimal debugging info.

## What it does :

__Reddit__: 
* Crawls submissions (posts) of a certain subreddit with query keyword
* Crawls comments of the particular submissions 
  
__PubMed__:
* Crawls URL of papers on certain search result
* Crawls information of the paper, including the abstract (by requesting the url) 

[__Daum Movie__](http://movie.daum.net):
* Crawls URL and other basic information of movies listed in Top 50 box office 
* Crawls [total audience, director, running time, etc] of each movies (by requesting the url)

### Start here if:
* You would like to crawl __Reddit__ and...

   _you have a specific subreddit in mind_  
   _you would like to get posts as well as their comments_
 
 * You would like to crawl __PubMed__ and... 
 
   _you have a specific search query_
   _you may want to specify advanced search options such as 'Article types', 'Text availability'_
   _you want the abstact_
 
 * You would like to crawl __Daum Movie__ and (다음 영화를 크롤하고 싶으면서) .. 
 
   _박스오피스 년도 별로 영화 정보를 저장하고 싶다_
  

