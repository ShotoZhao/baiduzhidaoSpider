# baiduzhidaoSpider
百度知道
## Preface
* this is a project about crawling data from zhidao.baidu.com. though baiduzhidao is not a very authoritative community, it is quite interesting to get some scattered knowledge or so-called experience. as we know, truth is quite unattainable especially personal experience. this project will help you to establish a databse of baiduzhidao, containing questions, best answers, other answers and other related items such as number of thumbup, post time, author and so on.

## Denpendencies
1. this project is based on python2.7 scrapy frame in windows system. python3.x may bring some unpredictable mistakes.
1. **redis** is used to remove duplicates, so **redis database** and **scrapy-redis** module for python2.7 are must be installed.
1. for persistent storage of data, **mongo database** is required.

## Usage
1. download this project, and put it into your IDE. (e.g.Pycharm)
1. firstly, you need modify **setting.py** in REDIS_HOST and REDIS_PORT. if you use local redise database, default is ok.
1. the same as the first step, modify  **redis_tomongo.py** in host, port, database, name, sheet name.
1. in the cmd, type into "scrapy crawl zhidaospider". and run redis_tomongo.py. data will be automatically stored in mongodb.

## PS
* this project is a primary edition, you can add new items in it and impove details.
* ***if you like this project, please star it, thanks.***
