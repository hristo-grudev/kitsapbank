BOT_NAME = 'kitsapbank'

SPIDER_MODULES = ['kitsapbank.spiders']
NEWSPIDER_MODULE = 'kitsapbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'kitsapbank.pipelines.KitsapbankPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
