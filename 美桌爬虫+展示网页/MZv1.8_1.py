"""
@Time       ：2019-2-2
@Author     ：Honeypot
@GitHub     : Alice-py
@e-mail     ：1104389956@qq.com
@version    : 1.8改动：添加图片删除模块（普通入口下载的图片部分不够清晰，添加过滤机制）,新增访问过于频繁bug修复    2019-6-28
                1.7改动：引入bs4模块，重构爬虫，高清壁纸过滤              2019-6-27
                    1.5改动：避免多次爬取触发网站反爬机制，修改报文头            2019-5-19
                        1.3改动：发现网站图片连接改动，修改正则表达式          2019-3-7
                         1.2改动：修复文件夹存在报错             2019-2-3（修复个bug以庆祝生日）
"""
import urllib.request
from bs4 import BeautifulSoup
import os


class MZBZ:
    def __init__(self, m_url):
        self.url = m_url

    def main_processing(self, url):
        req = urllib.request.Request(url=url)
        req.add_header(
            'User-Agent',
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
            "/73.0.3683.103 Safari/537.36")
        main_html_req = urllib.request.urlopen(req)
        main_html = main_html_req.read().decode('utf-8')
        main_txt = BeautifulSoup(main_html, features='html.parser').body
        main_html_req.close()
        return main_txt

    def main_html_urls(self):
        m_urls = []
        m_txt = self.main_processing(self.url)
        links = m_txt.find('div', {'class': 'pages'}).find_all('a')
        m_urls.append(self.url)
        for link in links:
            m_urls.append(link.get('href'))
        m_urls = list(set(m_urls))
        return m_urls

    def html_parsing_2(self, soup_txt, keyword):
        target_urls = []
        urls = soup_txt.find('div', {'class': 'tab_box'}).find_all('a')
        # 控制需求条件，如不需要可注销
        for url in urls:
            alt = url.get('alt')
            if keyword in alt:
                target_urls.append(url.get('href'))
        return target_urls

    def parsing_two(self, menu_url):
        # 解析目标模块，提取模块中的所有子链接（未包含本身）
        menu_list = []
        soup_html_3 = self.main_processing(menu_url)
        menu_urls = soup_html_3.find(
            'div', {'class': 'scroll-img-cont'}).find('ul').find_all('a')
        for menu_url in menu_urls:
            menu_list.append(menu_url.get('href'))
        return menu_list

    def target_pic(self, target_pic_url):
        target_pic_txt = self.main_processing(target_pic_url)
        target_pic_urls = target_pic_txt.find(
            'div', {'class': 'paper-down'}).find('a').get('href')
        return target_pic_urls

    def size_screening(self):
        path = './img/'
        pic_dir = os.listdir(path)
        m_pic_num = 0
        for pic in pic_dir:
            pic_size = os.path.getsize(path + pic)
            if pic_size < 1048576:
                m_pic_num += 1
                try:
                    os.remove(path + pic)
                except BaseException:
                    print('权限不够')
        print('小于1M的图片共', m_pic_num)
        return 0

    def main(self,keyword='',many_pic=999):
        try:
            os.makedirs('img')
        except BaseException:
            print('文件夹以存在或者权限不够')


        page = 0
        pic_num =0
        m_urls = self.main_html_urls()
        for m_url in m_urls:
            page += 1
            module = 0
            txt = self.main_processing(m_url)
            urls_2 = self.html_parsing_2(txt, keyword)
            for url_2 in urls_2:
                module += 1
                num = 0
                menu_urls_3 = self.parsing_two(url_2)
                for menu_url in menu_urls_3:
                    num += 1
                    pic_num+=1
                    down_url = self.target_pic(menu_url)
                    urllib.request.urlretrieve(
                        down_url, 'img/{0}_{1}_{2}.jpg'.format(page, module, num))
                    print(down_url, page, module, num, keyword + '主题')
                    if pic_num >= many_pic:
                        return 0

if __name__ == "__main__":
    main_url = r'http://www.win4000.com/zt/gaoqing.html'
    mz = MZBZ(main_url)
    print('美女、唯美、动漫、写真等')
    keyword = input('请输入主题（默认则不限制）：')
    many_pic = eval(input('请输入图片数量（默认则不限制）：'))
    mz.main(keyword,many_pic)
    ssg = input('是否需要筛选掉小于1M的图片(y/n)：')
    if ssg == 'y':
        mz.size_screening()  # 大小筛选机制
