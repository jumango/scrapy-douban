# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem



class DoubanimagePipeline(ImagesPipeline):
#     def process_item(self, item, spider):
#         return item
    def get_media_requests(self, item, info):
        print '********************item[image_urls]: ',item['image_urls']
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
    def file_path(self, request, response=None, info=None):
        ## start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, scrapy.Request):
            _warn()
            url = request 
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        ## end of deprecation warning block

#         image_guid = hashlib.sha1(url).hexdigest()  # change to request.url after deprecation
        image_name = request.url.split('/')[-1]
        return 'full/%s' % (image_name)
