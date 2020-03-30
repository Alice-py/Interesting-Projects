# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class SaveImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for pic_url in item['pic_url']:
            yield Request(url=pic_url)

    def file_path(self, request, response=None, info=None):
        # 重命名，避免默认保存到full文件夹
        dir_name = "img"
        # 因为图片没有名字就用url截取最后的字符串作为名字
        img_name = request.url.split('/')[-1]
        filename = u'{0}/{1}'.format(dir_name, img_name)
        return filename

