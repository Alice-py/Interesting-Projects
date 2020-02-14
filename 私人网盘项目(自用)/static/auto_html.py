"""
@Time       ：2020-1-30
@Author     ：Honeypot
@GitHub     : Alice-py
@e-mail     ：1104389956@qq.com
@version    : 1.0   自动化生成图片网站，可配合本人美桌爬虫模块使用
                1.2     删除1.0，自动生成电影网站，配合自用的页面做成简易私人网盘(反正DIY舒服)
                    1.3     增加Tools列表
"""
import os


class CreateHtml:
    def __init__(self):
        self.index_template = r'./py_html/index.html'
        self.movies_dir = r'./Movies/'
        self.tools_dir = r'./Tools/'
        self.index_path = r'../templates/index.html'

    def file_dir(self):
        movies_list = os.listdir(self.movies_dir)
        tools_list = os.listdir(self.tools_dir)
        return movies_list, tools_list

    def html_head(self):
        head_list = []
        with open(self.index_template, 'r', encoding='utf-8') as hd:
            for link in hd.readlines()[:95]:
                head_list.append(link)
        with open(self.index_path, 'w', encoding='utf-8') as ix:
            for link in head_list:
                ix.writelines(link)


    def html_menu(self, movie_name):
        menu_list = []
        for mp4_name in movie_name:
            mp4_name_s = mp4_name.strip('.mp4').strip(
                '.rmvb').strip('.avi').strip('.mkv')
            file_path = r'										<li><a href=".\Movies\\' + mp4_name + \
                r'" target="_blank">' + mp4_name_s + r'</a></li>'
            menu_list.append(file_path)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in menu_list:
                ix.write('\r\n')
                ix.writelines(link)
            ix.write('\r\n')

    def html_center(self):
        center_list = []
        with open(self.index_template, 'r', encoding='utf-8') as hd:
            for link in hd.readlines()[97:103]:
                center_list.append(link)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in center_list:
                ix.writelines(link)

    def html_tools(self, tools_name):
        tools_list = []

        for tool_name in tools_name:
            tool_name_s = tool_name.strip('.exe')
            file_path = r'										<div class="agile_activity_row"><div class="agile_' \
                        r'activity_img"><div class= "agile_activity_sub"><h5><a href=".\Tools\\' + tool_name + r'">'\
                        + tool_name_s + r'</a></h5></div></div><div class="clear"> </div></div>'
            tools_list.append(file_path)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in tools_list:
                ix.write('\r\n')
                ix.writelines(link)
            ix.write('\r\n')

    def html_buttom(self):
        bottom_list = []
        with open(self.index_template, 'r', encoding='utf-8') as hd:
            for link in hd.readlines()[105:]:
                bottom_list.append(link)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in bottom_list:
                ix.writelines(link)


    def CH_main(self):
        movies_list, tools_list = self.file_dir()  # 拿到目录里面的所有文件名
        self.html_head()  # 写入头
        self.html_menu(movies_list)  # 写入电影名
        self.html_center()  # 写入中间代码
        self.html_tools(tools_list)  # 写入工具
        self.html_buttom()  # 写入剩下代码


if __name__ == '__main__':
    ch = CreateHtml()
    ch.CH_main()
