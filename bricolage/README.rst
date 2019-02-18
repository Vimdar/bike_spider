Bricolage spider
===========================
-Simple Scrapy project for crawling mr. Bricolage bike section
with interchangable arguments for xpath selection.
-Stores data in chosen json file.

Repository
~~~~~~~~~~
https://github.com/Vimdar/bike_spider)

Installation
------------
-Clone project (if not already), setup requirements
-No pip install setup included for this project.

Usage
~~~~~~~~~~
run from project directory with command scrapy crawl and arguments you need f. ex.:
scrapy crawl bike_spider
-a start_urls='https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=0&priceValue='
-a pagination_xpath="(//li[@class='pagination-next'])[1]/a"
-a item_xpath="//div[@class='product']/div/a[not(@class)]"
-a title_xpath="(//h1)[1]/text()"
-a img_xpath="(//div[@class='owl-item active'])[1]/div/img/@src"
-a price_xpath="//p[@class='price']/text()"
-a description_xpath="//div[@id='profile']/div/p/text()"
-s 'absolute/path/to/store/output/data/file.name'

Can be run via curl to your scrapyd api with chosen arguments as well.
