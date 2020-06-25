# -*- coding: utf-8 -*-

# Scrapy settings for tt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tt'

SPIDER_MODULES = ['tt.spiders']
NEWSPIDER_MODULE = 'tt.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tt (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
'content-type': 'application/json',
'date': 'Thu, 25 Jun 2020 02:57:07 GMT',
'eagleid': '7587a8cb15930538267338202e',
'server': 'Tengine',
'server-timing': 'inner; dur=1200, tt_agw; dur=1200',
'server-timing': 'cdn-cache;desc=MISS,edge;dur=0,origin;dur=1236',
'set-cookie': 'tt_webid=6842114000470377991; Domain=.toutiao.com; expires=Wed, 23-Sep-2020 10:57:07 GMT; Max-Age=7804800; Path=/',
'status': '200',
'timing-allow-origin': '*',
'vary': 'Accept-Encoding',
'via': 'cache3.cn139[1236,0]',
'x-agw-info': '_gAou5nbvR3_xepnLpxmWzwJAB_sTP9B_2K3EOoQOCDRtV142EyASKUpebVWLob1S7J44gZJBD5AY3RFBsukVSu6fJ-LH97ijNitAsQy905mUOxkmEzYQBpxSBGQ9hDiGSywb7_QPizZL2CtXytLPtHkg_7pJRYjq-0decaw7B-bn8m5hw==',
'x-trans-level': '0',
'x-tt-logid': '202006251057060100120271451E4D431E',
'x-tt-trace-host': '01b47a400d1a3eccb96463814c9abf557ce4d5a70768549d95422265289a1b395f15f572233a08ae5e0666e6307b997c3ca7ce2108e5375b7aa3e778491f7364a99ccf7248147b5fc455c2044dbdfe392771778b0a4c9d4163084e083f99b264a3',
'x-tt-trace-tag': 'id=3;cdn-cache=miss',
'x_tt_logid': '202006251057060100120271451E4D431E'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tt.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tt.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tt.pipelines.TtPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
