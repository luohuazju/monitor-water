import scrapy

class MablefallSpider(scrapy.Spider):

    name = "mablefall"

    def start_requests(self):
        urls = [
            'https://hydromet.lcra.org/riverreport'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mablefall-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)