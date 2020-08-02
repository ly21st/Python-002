# -*- coding: utf-8 -*-

from maoyanmovie.proxyip import get_proxyips

# Scrapy settings for maoyanmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyanmovie'

SPIDER_MODULES = ['maoyanmovie.spiders']
NEWSPIDER_MODULE = 'maoyanmovie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maoyanmovie (+http://www.yourdomain.com)'
USER_AGENT = 'proxyspider (+http://www.maoyan.com)'

# USER_AGENT_LIST=[
# 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]
# import random
# USER_AGENT = random.choice(USER_AGENT_LIST)

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
  'Cookie': '__mta=188595735.1596003996934.1596004390619.1596004406053.5; uuid_n_v=v1; uuid=7260C220D16411EAAACFDFD33042EC97B2EF7A5441344248BDDDC19E315CBA49; _csrf=9d45504ed9e3361d5056c6d215be8ea754964b0b1e42bcd13e7a8ab0b9f8f30d; _lxsdk_cuid=173994053acc8-020a36b62d5632-4353761-e1000-173994053ac39; _lxsdk=7260C220D16411EAAACFDFD33042EC97B2EF7A5441344248BDDDC19E315CBA49; mojo-uuid=8b149714ccf0239177fce53b2348b89a; mojo-session-id={"id":"11ee7c39badc95549b5e4e148ea15b9f","time":1596093586096}; lt=wSSu0PUdb1Ok_3eHoCOZzjEcp2kAAAAAOQsAAEh0dKqRRcSSmo6GU3Cb2SMtk-BzzbYKhUmFLk6jZChQbjTcCWGjmosdc5Pg0nnc1A; lt.sig=P-QWrEW82cRBKUoRB8zjzDw7KX4; mojo-trace-id=6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1596003996,1596095324,1596095337; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596095337; __mta=188595735.1596003996934.1596004406053.1596095337780.6; _lxsdk_s=1739e975b34-248-127-5d9%7C%7C12'}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyanmovie.middlewares.MaoyanmovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyanmovie.middlewares.MaoyanmovieDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'maoyanmovie.middlewares.MaoyanmovieDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'maoyanmovie.middlewares.RandomHttpProxyMiddleware': 400,
}

HTTP_PROXY_LIST = [
    #  'http://52.179.231.206:80',
    #  'http://95.0.194.241:9090',
]
HTTP_PROXY_LIST.extend(get_proxyips())

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'maoyanmovie.pipelines.MaoyanmoviePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
