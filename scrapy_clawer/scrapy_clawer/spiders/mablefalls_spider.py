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
        tables = response.css('table.table-condensed')
        tbody = tables[5].xpath("tbody")
        for row in tbody.xpath("tr"):
            self.log(row.text)
            #cells = row.xpath("td")
            #if (cells[0].text == 'Marble Falls (Starcke)'):
            #    print(cells[1].text)