"""
@Time       ：2020-4-3
@Author     ：Honeypot
@GitHub     : Alice-py
@e-mail     ：1104389956@qq.com
@version    :  1.1  添加图片大小筛选机制      2020-4-3
                1.0   自动化生成图片网站，可配合本人美桌爬虫模块使用       2019-6-29

"""
import os
import random


class CreateHtml:
    def __init__(self):
        self.index_path = r'./index.html'
        self.head_path = r'./py_html/index_head.html'
        self.bac_path = r'./py_html/index_body_bac.html'
        self.center_path = r'./py_html/index_center.html'
        self.bottom_path = r'./py_html/index_bottom.html'
        self.img_path = r'./img'

    def file_dir(self):
        file_list = os.listdir(self.img_path)
        return file_list

    def html_head(self):
        head_list = []
        with open(self.head_path, 'r', encoding='utf-8') as hd:
            for link in hd:
                head_list.append(link)
        with open(self.index_path, 'w', encoding='utf-8') as ix:

            for link in head_list:
                ix.writelines(link)

    def html_background(self, random_pic):
        body_list = []
        with open(self.bac_path, 'r', encoding='utf-8') as hd:
            for link in hd:
                body_list.append(link)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            body_back = '<body background = "img/' + random_pic + \
                        '" witch = "2000" height = "1000" style = " background-repeat:no-repeat ;' + '\n'
            ix.writelines(body_back)
            for link in body_list:
                ix.writelines(link)

    def write_html_one(self, file_list):
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for file in file_list:
                ix.writelines('         <div class ="swiper-slide">' + '\n')
                ix.writelines(
                    '             <img src="img/' +
                    file +
                    '" alt ="轮播图">' +
                    '\n')
                ix.writelines('         </div>' + '\n')

    def html_center(self):
        center_list = []
        with open(self.center_path, 'r', encoding='utf-8') as cr:
            for link in cr:
                center_list.append(link)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in center_list:
                ix.writelines(link)

    def html_bottom(self):
        bottom_list = []
        with open(self.bottom_path, 'r', encoding='utf-8') as bm:
            for link in bm:
                bottom_list.append(link)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in bottom_list:
                ix.writelines(link)

    def size_screening(self):
        path = './img/'
        pic_dir = os.listdir(path)
        m_pic_num = 0
        for pic in pic_dir:
            pic_size = os.path.getsize(path + pic)
            # if pic_size < 1048576:    # 1M=1048576字节
            if pic_size < 204800:
                m_pic_num += 1
                try:
                    os.remove(path + pic)
                except BaseException:
                    print('权限不够')
        print('小于200KB的图片共', m_pic_num)
        return 0

    def CH_main(self):
        self.size_screening()  # 筛选大小
        file_list = self.file_dir()
        self.html_head()
        bac = file_list[random.randint(0, len(file_list) - 1)]
        self.html_background(bac)
        self.write_html_one(file_list)
        self.html_center()
        self.write_html_one(file_list)
        self.html_bottom()



if __name__ == '__main__':
    ch = CreateHtml()
    ch.CH_main()
