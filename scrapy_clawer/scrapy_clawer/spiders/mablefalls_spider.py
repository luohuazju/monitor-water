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
        tables = response.xpath('//table[@class="table table-condensed table-striped"]')
        #self.log(tables)
        tbody = tables[5].xpath("//tbody")
        #self.log(tbody)
        for row in tbody.xpath("//tr"):
            #self.log(row)
            cells = row.xpath("//td//span//text()").extract()
            #self.log(cells)
            for cell in cells:
                #self.log("cell=" + cell + "=")
                if (cell == 'Marble Falls (Starcke)'):
                    self.log("find the result")