import scrapy
from scrapy.loader import ItemLoader
from scrapy_clawer.items import WaterItem

class MablefallsSpider(scrapy.Spider):
    name = "mablefalls"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_clawer.middlewares.ChromeHeadlessMiddleware': 200
        },
        'ITEM_PIPELINES': {
            'scrapy_clawer.pipelines.RecordReleaseWaterPipeline': 100
        }
    }

    def start_requests(self):
        urls = [
            'https://hydromet.lcra.org/riverreport'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.xpath('//table[@class="table table-condensed table-striped"]')[4]
        rows = table.xpath("./tbody/tr")

        itemLoader = ItemLoader(item=WaterItem(), response=response)

        for row in rows:
            cells = row.xpath("./td/span/text()").extract()
            if (cells[0] == 'Marble Falls (Starcke)'):
                self.log(cells[1] + "|" + cells[3])
                itemLoader.add_value("releaseDate", cells[3])
                itemLoader.add_value("releaseString", cells[1])
                yield itemLoader.load_item()