import json

import scrapy

from scrapy.loader import ItemLoader

from ..items import ImbankItem
from itemloaders.processors import TakeFirst


class ImbankSpider(scrapy.Spider):
	name = 'imbank'
	start_urls = ['https://www.imbank.com/api/collections/get/posts']

	def parse(self, response):
		data = json.loads(response.text)
		for post in data['entries']:
			title = post['title']
			description = post['content']
			date = post['publish_date']

			item = ItemLoader(item=ImbankItem(), response=response)
			item.default_output_processor = TakeFirst()
			item.add_value('title', title)
			item.add_value('description', description)
			item.add_value('date', date)

			yield item.load_item()
