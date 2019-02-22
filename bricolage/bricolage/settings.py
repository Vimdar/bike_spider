# -*- coding: utf-8 -*-

# Scrapy settings for bricolage project
# from datetime import datetime as dt
# import pytz
#
# CURRENT_TZ = pytz.timezone('Europe/Sofia')
# TIME_NOW = dt.now(CURRENT_TZ)
BOT_NAME = 'bricolage'

SPIDER_MODULES = ['bricolage.spiders']
NEWSPIDER_MODULE = 'bricolage.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
USER_AGENT_AJAX = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
STORE_API_URL = ('https://mr-bricolage.bg/store-pickup/', '/pointOfServices')
SESSION_VARS = ('ROUTEID=.node0; __utmc=149670890; __utmz=149670890.1550237784.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1550237784084.987200092; cb-enabled=enabled;',
                '__utma=149670890.1836262783.1550237784.1550750610.1550757367.21; __utmt=1; __utmb=149670890.7.10.1550757367'
                )
API_HEADERS = {'Cookie': '',
               'Origin': 'https://mr-bricolage.bg',
               'Accept-Encoding': 'gzip, deflate, br',
               'accept-language': 'en-US,en;q=0.9',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'accept': '*/*',
               'Referer': '',
               'x-requested-with': 'XMLHttpRequest',
               'Connection': 'keep-alive'
               }
API_DATA = 'locationQuery=&cartPage=false&entryNumber=0&latitude=42.6641056&longitude=23.3233149&CSRFToken='
LOG_LEVEL = 'INFO'
FEED_FORMAT = 'jsonlines'
# DOWNLOAD_DELAY = 0.7
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# # cache for 1 day
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 60*60*24
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'bricolage.pipelines.BricolagePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False
