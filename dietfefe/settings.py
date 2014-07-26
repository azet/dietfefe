# -*- coding: utf-8 -*-

# Scrapy settings for dietfefe project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dietfefe'

SPIDER_MODULES   = ['dietfefe.spiders']
NEWSPIDER_MODULE = 'dietfefe.spiders'

ITEM_PIPELINES = {
        'dietfefe.pipelines.DuplicatesPipeline': 200,
        'dietfefe.pipelines.JsonExportPipeline': 100,
}

FEED_EXPORTERS_BASE = {
        'json': 'scrapy.contrib.exporter.JsonItemExporter',
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'scrapy'
