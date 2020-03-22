import os
import re


class RName:
    def __init__(self, dir_path, movie_name=''):
        self.i = 1
        self.dir_path = dir_path
        self.movie_name = movie_name

    def change_name(self, source_name):

        suffix = os.path.splitext(self.dir_path + source_name)[1]  # 判断后缀

        try:
            big_num = r'S[0-9]+E[0-9]+'  # 保留S*E*
            blues_z = re.compile(big_num)
            blues = blues_z.findall(source_name)[0]
        except BaseException:
            small_num = r's[0-9]+e[0-9]+'  # 保留s*e*
            blues_z = re.compile(small_num)
            blues = blues_z.findall(source_name)[0]

        New_name = self.movie_name + '_' + blues + suffix
        return New_name

    def rname(self):
        file_names = os.listdir(self.dir_path)
        for file_name in file_names:
            New_name = self.change_name(file_name)
            if (New_name != file_name):
                os.rename(self.dir_path + file_name, self.dir_path + New_name)
            print("原:", file_name, '  ', "改为：", New_name)


if __name__ == '__main__':
    print(">>> 仅支持snen格式的剧集，为人人影视而制")
    dir_path = input('文件夹路径：') + '\\'
    movie_name = input('保留电影名：')
    rn = RName(dir_path, movie_name)
    rn.rname()
