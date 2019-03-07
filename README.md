# Crawler-Collection (Reddit, PubMed, Daum Movie)

This project includes collection of crawlers for _light-use_ purposes. 
As of now, it is intended to run on interactive IDE such as Jupyter Notebook rather than command prompt as it provides 
minimal debugging info. 

If you are new to crawling and is unsure where to start, please see below ('Start here if') to check if my crawler can crawl the information you want. If you think it would be useful please feel free to use my crawler.

On the other hand, if you know what you are doing, this project may be a helpful starting point to building your own crawler that satisfies your requirements :) 


## What it does :

__Reddit__: 
* Crawls submissions (posts) of a certain subreddit with query keyword
* Crawls comments of those particular submissions 
  
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
 
 * 다음 영화로 부터 아래 하고 싶다면 (If you are non-Korean, and you would like to crawl this website for any reason. This does..): 
 
   _박스오피스 년도 별로 영화 정보를 저장하고 싶다_ (_Crawls basic info. about Top 50 movies every year and URL_)  
   _영화의 러닝타임, 감독, 평점 등을 저장하고 싶다_ (_running time, director, ratings, etc_) 
  
## Getting Started 

All modules make use of beautifulsoup and pandas. You can download them using pip.
```bash
pip install beautifulsoup4
pip install pandas
```


_For Reddit crawler_, I psaw which is a wrapper for searching Reddit by pushshift.io API. Please refer to the documentation before using it as it provides very diverse and convenient features. 
 * [psaw Github](https://github.com/dmarx/psaw)
 * [Pushshift API](https://github.com/pushshift/api)
 
 For installing psaw, use 
 ```bash
pip install psaw
```

_For PubMed crawler_ only, selenium library is required. For installing it, use pip. For installing your browser driver, refer [here](https://pypi.org/project/selenium/)
```bash
pip install selenium
```

## Usage (To be updated)
### Reddit
### PubMed
### Daum Movie
