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
# DOWNLOAD_DELAY = 0.7
LOG_LEVEL = 'INFO'
FEED_FORMAT = 'jsonlines'
# FEED_URI = '/home/dimitarva/ws/browsewave/bricolage/tmp/output.json'
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
