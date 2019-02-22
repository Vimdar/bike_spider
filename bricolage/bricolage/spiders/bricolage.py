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
import requests
import json
from scrapy.utils.project import get_project_settings


class BikeSpider(Spider):
    name = 'bike_spider'

    def __init__(self, **kwargs):
        kwargs = {k: v for k, v in kwargs.items()}
        self.logger.info(u'Spider arguments:\n{}'.format(pp.pformat(kwargs)))
        Spider.__init__(self, **kwargs)
        self.settings = get_project_settings()

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
        csrf_token = self.get_csrf_token(response)
        jsession_id = response.headers.getlist('Set-Cookie')[0].decode('utf-8').split(';')[0]
        for link in links:
            inner = fs(link)
            url = response.urljoin(inner.xpath('//a/@href')[0])
            img = inner.xpath('//img/@src')[0]
            title = inner.xpath('//a/@title')[0]
            meta = {
                'link': url,
                'crawl_date': crawl_date,
                'img': img,
                'title': title,
                'csrf_token': csrf_token,
                'jsession_id': jsession_id,
            }
            yield Request(
                url,
                callback=self.parse_item,
                meta=meta
            )

    def parse_item(self, response):
        numb = response.url.split('/')[-1]
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
        store_data = self.get_store_supply_data(numb,
                                                response.meta['jsession_id'],
                                                response.url,
                                                response.meta['csrf_token'],
                                                )
        item['stores'] = store_data
        yield item

    def get_decimal_price(self, price):
        return re.findall(self.price_regex, price)[0]

    def get_store_supply_data(self, numb, jsession_id, referer, csrf_token):
        # WORKAROUND: simulating the ajax call to the API that the site makes
        # to obtain the store supply data
        # since it's resource cheaper than setting up and maintaining
        # some rendering engine (splash, selenium, etc.)
        # for this purpose we'll make a call to the API for every item we find
        # -url contains the product id
        # -headers will be enriched with the session cookie and referer to
        # the item page
        # request data has to contain csrf token set for our session
        api_call_url = self.settings['STORE_API_URL'][0] + numb + self.settings['STORE_API_URL'][1]

        headers = self.settings['API_HEADERS']
        headers['Cookie'] = jsession_id + '; ' + self.settings['SESSION_VARS'][0] \
            + ' ' + jsession_id + '; ' + self.settings['SESSION_VARS'][1]
        headers['Referer'] = referer

        api_data_call = self.settings['API_DATA'] + csrf_token

        req = requests.post(url=api_call_url, headers=headers, data=api_data_call)
        try:
            json_data = json.loads(req.content)
            store_data = json_data['data']
        except ValueError:  # JSONDecodeError inherits from ValueError
            return 'Error while getting store_data'
        return store_data

    def get_csrf_token(self, response):
        return response.xpath("//input[@name='CSRFToken']/@value").extract()[0]
