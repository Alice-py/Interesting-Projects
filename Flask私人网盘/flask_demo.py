# -*-coding:GBK -*-
"""
@Time       ：2020-2-26
@Author     ：Honeypot
@GitHub     : Alice-py
@e-mail     ：1104389956@qq.com
@version    : 1.0   添加控制模块
                1.2     新增模拟人工操作，重启迅雷任务
                    1.3     修复路由跳转失败BUG，添加伪装页面，私人网站防止非法访问
                        1.4     增加记事本功能，还不算完善，大概功能均已实现后续将持续优化
"""
from flask import Flask, url_for, make_response, render_template, request, redirect, send_file
import os, time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from event_simulation import KM     # 模拟点击
# 刷新网页
from static.auto_html import CreateHtml
from static.auto_html_2 import CreateHtml2

app = Flask(__name__, static_url_path='')
app.secret_key = 'lyb'
static_path = os.getcwd() + "\\static\\"


class LYB(FlaskForm):
    lyk = StringField('留言:', validators=[DataRequired()])
    submit = SubmitField('提交')


def movies_dirs():
    three_route_path = ""
    files = os.listdir(static_path + 'Movies')
    files2 = os.listdir(static_path + 'Movie')
    for file in files:
        # 当检测到文件夹时记录
        if '.' not in file:
            three_route_path += file + ","
    for file in files2:
        if '.' not in file:
            three_route_path += file + ","
    return three_route_path


# 伪装登录页面
@app.route('/')
def login_wz():
    return render_template('login_wz.html')


# 一层路由处理
@app.route('/l', methods=['GET', 'POST'])
def index_main():
    # 将所有文件放置在static/中
    lyb_form = LYB()
    if request.method == 'POST':
        ly_txt = request.form.get('lyk')
        ly_data = "{0}|{1}\n".format(time.strftime("%m.%d %H:%M", time.localtime()), ly_txt)
        with open("templates/lyb.dll", "a+", encoding="utf-8") as fp:
            fp.writelines(ly_data)

    with open('templates/lyb.dll', 'r', encoding='utf-8') as lyb_txt:
        # 获取记事本
        lybs = lyb_txt.readlines()
        lyb = []
        for ly in lybs:
            lyb_dict = dict()
            ly = ly.strip().split("|")
            lyb_dict["time"] = ly[0]
            lyb_dict["data"] = ly[1]
            lyb.append(lyb_dict)
    return render_template('index.html', lyb=lyb, form=lyb_form)


# 控制路由处理
@app.route('/control/<path>')
def cmd(path):
    # 通过路由控制电脑实现基础远控功能，本质上所有dos可执行的指令都可以处理
    ts = 'null'
    if path == '1':
        # 关机
        ts = "<html><body><h3>电脑将在30秒后自动关机</h3><a href='./2'>取消</a></body></html>"
        os.system('shutdown -s -t 30')
    elif path == '2':
        # 取消关机
        ts = "<html><body><h3>已取消关机</h3><a href='../'>返回主页</a></body></html>"
        os.system('shutdown -a')
    elif path == '3':
        # 重启
        command = 'shutdown -r'
        ts = "<html><body><h3>" + command + \
             ">>命令已被执行</h3><a href='../'>返回主页</a></body></html>"
        os.system(command)
    elif path == '4':
        # 开启向日葵远控
        command = r'Q:\XRK\SunloginClient\SunloginClient.exe'
        ts = "<html><body><h3>向日葵已开启</h3><a href='../' >返回上一页</a></body></html>"
        os.system(command)
    elif path == '5':
        # 锁屏
        command = r'static\sp.vbs'
        ts = "<html><body><h3>已锁屏</h3><a href='../' >返回上一页</a></body></html>"
        os.system(command)
    elif path == '6':
        # 打开WiFi
        ts = KM().open_wifi()
    elif path == '7':
        # 迅雷任务重启
        ts = KM().thunder_res()

    return ts


# 登录路由处理
@app.route('/login', methods=['POST', 'GET'])
def login():
    # post请求接收
    if request.method == 'POST':
        if request.form['say'] == 'h':
            return render_template('index2.html')
        else:
            return render_template('index.html')
    return render_template('index.html')


# 二层路由处理
@app.route('/<any(Tools, 临时, Movies, Movie,):path>/')
def two_path(path):
    files_path = static_path + path
    files = os.listdir(files_path)
    return render_template('dirs.html', path=path, files=files)


# 三层路由处理
@app.route(
    '/<any(Tools, 临时, Movies, Movie,):path>/<any({0}):paths>/'.format(movies_dirs()))
def three_path(path, paths):
    files_path = static_path + path + '\\' + paths
    files = os.listdir(files_path)
    return render_template('dirs.html', path=path, files=files)


# 四级路由处理,一般不需要，备用，还差一个文件夹与非文件夹区分
@app.route('/Movie/动漫/<dmclass>/')
def four_path(dmclass):
    files = os.listdir(static_path + "/Movie/动漫/" + dmclass)
    return render_template('dirs.html', path=dmclass, files=files)


if __name__ == '__main__':
    """入口 ->生成网页 ->运行Flask"""
    state = CreateHtml().CH_main()  # 由于工作路径发生变化，auto_html.py需要对应路径因发生改变
    states = CreateHtml2().CH_main()
    print("{0} {1}\n{0} {2}".format('>' * 6, state, states))
    app.run(host='0.0.0.0', port=80, debug=0)
