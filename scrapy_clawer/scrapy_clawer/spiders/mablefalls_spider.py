import scrapy

class MablefallsSpider(scrapy.Spider):
    name = "mablefalls"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_clawer.middlewares.ChromeHeadlessMiddleware': 200
        }
        #'ITEM_PIPELINES': {
        #    'price_crawler.pipelines.wmPostProductPipeline': 100
        #}
    }

    def start_requests(self):
        urls = [
            'https://hydromet.lcra.org/riverreport'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("--------------###############################")
        table = response.xpath('//table[@class="table table-condensed table-striped"]')[4]
        #self.log(table)
        rows = table.xpath("./tbody/tr")
        #self.log(rows)
        for row in rows:
        #    self.log(row)
            cells = row.xpath("./td/span/text()").extract()
            #self.log(cells[0])
            if (cells[0] == 'Marble Falls (Starcke)'):
                self.log(cells[1] + "|" + cells[3])