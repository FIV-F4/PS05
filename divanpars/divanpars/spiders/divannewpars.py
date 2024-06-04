import scrapy


class DivannewparsSpider(scrapy.Spider):

    name = "svet"
    allowed_domains = ["https://www.msveta.ru/"]
    start_urls = ["https://www.msveta.ru/catalog/lyustry/"]

    #name = "divannewpars"
    #allowed_domains = ["https://divan.ru"]
    #start_urls = ["https://www.divan.ru/sankt-peterburg/category/svetilniki"]

    def parse(self, response):
        svets = response.css("div.item_info")
        for svet in svets:
            yield {
                'name': svet.css("a.dark_link span::text").get(),
                'price': svet.css('div.price.font-bold span.price_value::text').get(),
                'url': svet.css("a").attrib["href"]

            }

    '''
        def parse(self, response):
        divans = response.css("div._Ud0k")
        for divan in divans:
            yield {
                'name': divan.css("div.lsooF span::text").get(),
                'price': divan.css("div.pY3d2 span::text").get(),
                'url': divan.css("a").attrib["href"]
            }
    '''
