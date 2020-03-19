import os


class CreateHtml2:
    def __init__(self):
        self.index_template = r'./static/py_html/index2.html'
        self.movies_dir = r'./static/Movie/普通/'
        self.movies_dir_dm = r'./static/Movie/动漫/'
        self.index_path = r'./templates/index2.html'

    def file_dir(self):
        movies_list = os.listdir(self.movies_dir)
        dms_list = os.listdir(self.movies_dir_dm)
        return movies_list, dms_list

    def html_head(self):
        head_list = []
        with open(self.index_template, 'r', encoding='utf-8') as hd:
            for link in hd.readlines()[:101]:
                head_list.append(link)
        # print(head_list)
        with open(self.index_path, 'w', encoding='utf-8') as ix:
            for link in head_list:
                ix.writelines(link)

    def html_menu(self, movie_name):
        menu_list = []
        for mp4_name in movie_name:
            mp4_name_s = mp4_name.strip('.mp4').strip(
                '.rmvb').strip('.avi').strip('.mkv')
            file_path = r"										<li><a href='.\Movie\普通\{0}' target='_blank'>" \
                        r"{1}</a></li>".format(mp4_name, mp4_name_s)
            menu_list.append(file_path)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in menu_list:
                ix.writelines(link)
                ix.write('\r\n')

    def html_center(self):
        center_list = []
        with open(self.index_template, 'r', encoding='utf-8') as hd:
            for link in hd.readlines()[101:107]:
                center_list.append(link)
        # print(center_list)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in center_list:
                ix.writelines(link)

    def html_dm(self, dms_name):
        dms_list = []
        for dm_name in dms_name:
            dm_name_s = dm_name.strip('.mp4').strip(
                '.rmvb').strip('.avi').strip('.mkv')
            # file_path = '										<li><a href=".\Movie\动' '漫\\' + \
            #     dm_name + r'" target="_blank">' + dm_name_s + r'</a></li>'
            file_path = r"										<li><a href='.\Movie\动漫\{0}' target='_blank'>" \
                        r"{1}<a></li>".format(dm_name, dm_name_s)

            dms_list.append(file_path)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in dms_list:
                ix.writelines(link)
                ix.write('\r\n')

    def html_buttom(self):
        bottom_list = []
        with open(self.index_template, 'r', encoding='utf-8') as hd:
            for link in hd.readlines()[109:]:
                bottom_list.append(link)
        # print(bottom_list)
        with open(self.index_path, 'a+', encoding='utf-8') as ix:
            for link in bottom_list:
                ix.writelines(link)

    def CH_main(self):
        movies_list, dm_list = self.file_dir()  # 拿到目录里面的所有文件名
        self.html_head()  # 写入头
        self.html_menu(movies_list)  # 写入普通电影名
        self.html_center()  # 写入中间代码
        self.html_dm(dm_list)     # 写入动漫电影
        self.html_buttom()  # 写入剩下代码
        return 'index2.html --- Done! '


if __name__ == '__main__':
    # 去掉/static,index_path加上一个.才可单独运行
    ch = CreateHtml2()
    ch.CH_main()
