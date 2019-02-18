from scrapy.spiders import Spider
import pprint as pp
from datetime import datetime as dt
from urllib.parse import urlparse
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from bricolage.items import VeloItem
from scrapy import selector
import re
from lxml.html import fromstring as fs


class BikeSpider(Spider):
    name = 'bike_spider'

    def __init__(self, **kwargs):
        kwargs = {k: v for k, v in kwargs.items()}
        self.logger.info(u'Spider arguments:\n{}'.format(pp.pformat(kwargs)))
        Spider.__init__(self, **kwargs)

        self.start_urls = kwargs['start_urls'].split(';')
        if 'allowed_domains' in kwargs and kwargs['allowed_domains'] is not None:
            self.allowed_domains = kwargs['allowed_domains'].split(';')
        else:
            self.allowed_domains = []
            for url in self.start_urls:
                parsed_url = urlparse(url)
                self.allowed_domains.append(parsed_url.hostname)

        self.pagination_xpath = kwargs['pagination_xpath']
        self.item_xpath = kwargs['item_xpath']
        self.title_xpath = kwargs['title_xpath']
        self.img_xpath = kwargs['img_xpath']
        self.price_xpath = kwargs['price_xpath']
        self.price_regex = re.compile("\d+\,\d+")
        self.description_xpath = kwargs['description_xpath']

    def parse(self, response):
        if self.pagination_xpath is not None:
            lext = LinkExtractor(restrict_xpaths=(self.pagination_xpath))
            next = lext.extract_links(response)
            meta = {'dont_redirect': True}
            for link in next:
                yield Request(
                    link.url,
                    self.parse,
                    meta=meta,
                )
        crawl_date = dt.now()
        links = response.xpath(self.item_xpath).extract()
        for link in links:
            inner = fs(link)
            url = response.urljoin(inner.xpath('//a/@href')[0])
            img = inner.xpath('//img/@src')[0]
            title = inner.xpath('//a/@title')[0]
            meta = {
                'link': url,
                'crawl_date': crawl_date,
                'img': img,
                'title': title
            }
            yield Request(
                url,
                callback=self.parse_item,
                meta=meta
            )

    def parse_item(self, response):
        item = VeloItem(
            url=response.url,
            crawl_date=response.meta['crawl_date'],
            image_url=response.meta['img'],
            title=response.meta['title']
        )
        hxs = selector.Selector(response, type='html')
        item['price'] = self.get_decimal_price(''.join(hxs.xpath(self.price_xpath).extract()))
        item['description'] = ' '.join(hxs.xpath(self.description_xpath).extract())
        if not item['image_url']:
            item['image_url'] = ''.join(hxs.xpath(self.img_xpath).extract())
        if not item['title']:
            item['title'] = ''.join(hxs.xpath(self.title_xpath).extract())
        yield item

    def get_decimal_price(self, price):
        return re.findall(self.price_regex, price)[0]
# scrapy crawl bike_spider -a start_urls='https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=0&priceValue=' -a pagination_xpath="(//li[@class='pagination-next'])[1]/a" -a item_xpath="//div[@class='product']/div/a[not(@class)]" -a title_xpath="(//h1)[1]/text()" -a img_xpath="(//div[@class='owl-item active'])[1]/div/img/@src" -a price_xpath="//p[@class='price']/text()" -a description_xpath="//div[@id='profile']/div/p/text()"
