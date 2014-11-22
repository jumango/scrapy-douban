# -*- coding: utf-8 -*-

# Scrapy settings for doubanimage project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'doubanimage'

SPIDER_MODULES = ['doubanimage.spiders']
NEWSPIDER_MODULE = 'doubanimage.spiders'
# ITEM_PIPELINES = {'doubanimage.pipelines.DoubanimagePipeline': 1}
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
        'doubanimage.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
    }

IMAGES_STORE = '/home/huyc/scrapy/doubanimage/images'
DOWNLOAD_DELAY = 1
COOKIES_ENABLES = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'
# USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'
# USER_AGENT = 'Mozilla/5.0 (compatible; YodaoBot/1.0;http://www.yodao.com/help/webmaster/spider/;)'