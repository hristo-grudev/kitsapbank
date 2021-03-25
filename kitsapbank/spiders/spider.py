import scrapy

from scrapy.loader import ItemLoader

from ..items import KitsapbankItem
from itemloaders.processors import TakeFirst


class KitsapbankSpider(scrapy.Spider):
	name = 'kitsapbank'
	start_urls = ['https://www.kitsapbank.com/about-us/news/']

	def parse(self, response):
		post_links = response.xpath('//a[@class="more"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="more next-link"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h2/text()').get()
		description = response.xpath('//div[@class="rtecontent"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="details"]/text()').get()

		item = ItemLoader(item=KitsapbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
