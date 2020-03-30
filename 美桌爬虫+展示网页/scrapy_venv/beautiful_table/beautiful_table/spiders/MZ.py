# -*- coding: utf-8 -*-
"""
@Time       ：2019-2-2
@Author     ：Honeypot
@GitHub     : Alice-py
@e-mail     ：1104389956@qq.com
@version    : 2.0改动：使用Scrapy完全重写此爬虫         202-3-30
                1.8改动：添加图片删除模块（普通入口下载的图片部分不够清晰，添加过滤机制）,新增访问过于频繁bug修复    2019-6-28
                    1.7改动：引入bs4模块，重构爬虫，高清壁纸过滤              2019-6-27
                        1.5改动：避免多次爬取触发网站反爬机制，修改报文头            2019-5-19
                            1.3改动：发现网站图片连接改动，修改正则表达式          2019-3-7
                                1.2改动：修复文件夹存在报错             2019-2-3（修复个bug以庆祝生日）
"""
from beautiful_table.items import BeautifulTableItem
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

count = 0


class MzSpider(CrawlSpider):
    name = 'MZ'
    allowed_domains = ['win4000.com']
    print(
        r"""
                            (`.         ,-,
                            ` `.    ,;' /
                             `.  ,'/ .'
                   Honeypot   `. X /.'
                    .-;--''--.._` ` (
                  .'            /   `
                 ,           ` '   Q '
                 ,         ,   `._    \
              ,.|         '     `-.;_'     
              :  . `  ;    `  ` --,.._;
               ' `    ,   )   .'
                  `._ ,  '   /_
                     ; ,''-,;' ``-
                      ``-..__``--`
        """
    )
    print(">>> 可供选择：1.动漫，2.写真，3.小清新   ---默认动漫")
    # start_url_class = input(">>> 请输入编号：")
    # if start_url_class == "1":
    #     url_link = "http://www.win4000.com/zt/dongman.html"
    # elif start_url_class == "2":
    #     url_link = "http://www.win4000.com/zt/xinggan.html"
    # elif start_url_class == "3":
    #     url_link = "http://www.win4000.com/zt/xiaoqingxin.html"
    # else:
    #     url_link = "http://www.win4000.com/zt/dongman.html"
    url_link = "http://www.win4000.com/zt/dongman.html"
    start_urls = [url_link]  # 入口是动漫，如果想要其他请自行更换
    rules = (
        Rule(LinkExtractor(allow=r"http://www.win4000.com/.+/.+_[0-9].html", restrict_xpaths="//div[@class='pages']"),
             callback=None, follow=True),  # 获取页
        Rule(LinkExtractor(allow=r"http://www.win4000.com/wallpaper_detail_[0-9]+.html",
                           restrict_xpaths="//div[@class='list_cont Left_list_cont  Left_list_cont1']//a"),
             callback="get_pic_url", follow=True),  # 获取合集

        # http://pic1.win4000.com/wallpaper/2020-03-26/5e7c4c5e5d14c.jpg
        # Rule(LinkExtractor(allow="http://pic1.win4000.com/.+.jpg", restrict_xpaths="//img[@class='pic-large']"),
        #      callback="down_pic", follow=False)
    )

    def get_pic_url(self, response):
        # rule已拿到了每一个合集
        # 现在获取合集的每一张图片url

        pic_url_n = response.xpath("//ul[@id='scroll']//li/a/@href").getall()  # 获取每一个合集的每一张，是一个列表
        for new_url in pic_url_n:
            yield Request(url=new_url, callback=self.down_pic)
        # with open("view.txt", "a+", encoding="utf-8") as fp:
        #     fp.writelines(pic_url_n + "\n")

    def down_pic(self, response):
        global count
        # 计数
        count += 1
        if count >= 30:
            self.crawler.engine.close_spider(self)

        pic_down_url = response.xpath("//img[@class='pic-large']/@src").get()
        # 再将图片传递给下载器
        item = BeautifulTableItem()
        pic_down_list = []
        pic_down_list.append(pic_down_url)
        item["pic_url"] = pic_down_list
        yield item
