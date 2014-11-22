from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy
from scrapy.utils.url import urljoin_rfc
from doubanimage.items import DoubanimageItem

class imageSpider(CrawlSpider):
    name = 'doubanimage'
    allowed_domains=["site.douban.com"]
    start_urls=["http://site.douban.com/106875/widget/public_album/291894/"]
    urlset = set()
    
    rules=[
        Rule(SgmlLinkExtractor(allow=(r'/106875/widget/public_album/291894/\?start=\d+.*')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'http://site.douban.com/106875/widget/public_album/291894/photo/\d+')),callback="parse_urls"),      
    ]
    
    def parse_urls(self,response):
        urls = response.xpath("//div[@class='phoinfo']/a/@href").extract()
        for url in urls:
            if url not in self.urlset:
                self.urlset.add(url)
                url = url + 'photos'
                yield scrapy.Request(url = url, callback = self.parse_sub, dont_filter = True)
#                 yield scrapy.Request(url = url, callback = self.parse_sub)
    def parse_sub(self,response):
        album_url = response.xpath("//a[@class='album_photo']/@href").extract()
        item = DoubanimageItem()
        for url in album_url:
            item['father_url'] = url
            yield scrapy.Request(url = url, callback = self.parse_album, meta = {'item':item}, dont_filter = True)
#             yield scrapy.Request(url = url, callback = self.parse_album)
    def parse_album(self,response):
        item = response.meta['item']
        img_urls = map(lambda url:url.replace('thumb','photo'),response.xpath("//a[@class='photolst_photo']/img/@src").extract())
        title = response.xpath("//div[@class='photolst clearfix']//div[@class='pl']/text()").extract()
        item['image_urls'] = img_urls
        return item
        
        