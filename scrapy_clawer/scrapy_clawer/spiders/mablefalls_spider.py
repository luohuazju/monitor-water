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
        self.log(response)
        #tables = response.find_elements_by_css_selector('table.table-condensed')
        #tbody = tables[5].find_element_by_tag_name("tbody")
        #for row in tbody.find_elements_by_tag_name("tr"):
        #    cells = row.find_elements_by_tag_name("td")
        #    if (cells[0].text == 'Marble Falls (Starcke)'):
        #        print(cells[1].text)