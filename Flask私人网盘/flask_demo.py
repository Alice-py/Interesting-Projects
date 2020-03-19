# -*-coding:GBK -*-
"""
@Time       ��2020-2-26
@Author     ��Honeypot
@GitHub     : Alice-py
@e-mail     ��1104389956@qq.com
@version    : 1.0   ��ӿ���ģ��
                1.2     ����ģ���˹�����������Ѹ������
                    1.3     �޸�·����תʧ��BUG�����αװҳ�棬˽����վ��ֹ�Ƿ�����
                        1.4     ���Ӽ��±����ܣ����������ƣ���Ź��ܾ���ʵ�ֺ����������Ż�
"""
from flask import Flask, url_for, make_response, render_template, request, redirect, send_file
import os, time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from event_simulation import KM     # ģ����
# ˢ����ҳ
from static.auto_html import CreateHtml
from static.auto_html_2 import CreateHtml2

app = Flask(__name__, static_url_path='')
app.secret_key = 'lyb'
static_path = os.getcwd() + "\\static\\"


class LYB(FlaskForm):
    lyk = StringField('����:', validators=[DataRequired()])
    submit = SubmitField('�ύ')


def movies_dirs():
    three_route_path = ""
    files = os.listdir(static_path + 'Movies')
    files2 = os.listdir(static_path + 'Movie')
    for file in files:
        # ����⵽�ļ���ʱ��¼
        if '.' not in file:
            three_route_path += file + ","
    for file in files2:
        if '.' not in file:
            three_route_path += file + ","
    return three_route_path


# αװ��¼ҳ��
@app.route('/')
def login_wz():
    return render_template('login_wz.html')


# һ��·�ɴ���
@app.route('/l', methods=['GET', 'POST'])
def index_main():
    # �������ļ�������static/��
    lyb_form = LYB()
    if request.method == 'POST':
        ly_txt = request.form.get('lyk')
        ly_data = "{0}|{1}\n".format(time.strftime("%m.%d %H:%M", time.localtime()), ly_txt)
        with open("templates/lyb.dll", "a+", encoding="utf-8") as fp:
            fp.writelines(ly_data)

    with open('templates/lyb.dll', 'r', encoding='utf-8') as lyb_txt:
        # ��ȡ���±�
        lybs = lyb_txt.readlines()
        lyb = []
        for ly in lybs:
            lyb_dict = dict()
            ly = ly.strip().split("|")
            lyb_dict["time"] = ly[0]
            lyb_dict["data"] = ly[1]
            lyb.append(lyb_dict)
    return render_template('index.html', lyb=lyb, form=lyb_form)


# ����·�ɴ���
@app.route('/control/<path>')
def cmd(path):
    # ͨ��·�ɿ��Ƶ���ʵ�ֻ���Զ�ع��ܣ�����������dos��ִ�е�ָ����Դ���
    ts = 'null'
    if path == '1':
        # �ػ�
        ts = "<html><body><h3>���Խ���30����Զ��ػ�</h3><a href='./2'>ȡ��</a></body></html>"
        os.system('shutdown -s -t 30')
    elif path == '2':
        # ȡ���ػ�
        ts = "<html><body><h3>��ȡ���ػ�</h3><a href='../'>������ҳ</a></body></html>"
        os.system('shutdown -a')
    elif path == '3':
        # ����
        command = 'shutdown -r'
        ts = "<html><body><h3>" + command + \
             ">>�����ѱ�ִ��</h3><a href='../'>������ҳ</a></body></html>"
        os.system(command)
    elif path == '4':
        # �������տ�Զ��
        command = r'Q:\XRK\SunloginClient\SunloginClient.exe'
        ts = "<html><body><h3>���տ��ѿ���</h3><a href='../' >������һҳ</a></body></html>"
        os.system(command)
    elif path == '5':
        # ����
        command = r'static\sp.vbs'
        ts = "<html><body><h3>������</h3><a href='../' >������һҳ</a></body></html>"
        os.system(command)
    elif path == '6':
        # ��WiFi
        ts = KM().open_wifi()
    elif path == '7':
        # Ѹ����������
        ts = KM().thunder_res()

    return ts


# ��¼·�ɴ���
@app.route('/login', methods=['POST', 'GET'])
def login():
    # post�������
    if request.method == 'POST':
        if request.form['say'] == 'h':
            return render_template('index2.html')
        else:
            return render_template('index.html')
    return render_template('index.html')


# ����·�ɴ���
@app.route('/<any(Tools, ��ʱ, Movies, Movie,):path>/')
def two_path(path):
    files_path = static_path + path
    files = os.listdir(files_path)
    return render_template('dirs.html', path=path, files=files)


# ����·�ɴ���
@app.route(
    '/<any(Tools, ��ʱ, Movies, Movie,):path>/<any({0}):paths>/'.format(movies_dirs()))
def three_path(path, paths):
    files_path = static_path + path + '\\' + paths
    files = os.listdir(files_path)
    return render_template('dirs.html', path=path, files=files)


# �ļ�·�ɴ���,һ�㲻��Ҫ�����ã�����һ���ļ�������ļ�������
@app.route('/Movie/����/<dmclass>/')
def four_path(dmclass):
    files = os.listdir(static_path + "/Movie/����/" + dmclass)
    return render_template('dirs.html', path=dmclass, files=files)


if __name__ == '__main__':
    """��� ->������ҳ ->����Flask"""
    state = CreateHtml().CH_main()  # ���ڹ���·�������仯��auto_html.py��Ҫ��Ӧ·�������ı�
    states = CreateHtml2().CH_main()
    print("{0} {1}\n{0} {2}".format('>' * 6, state, states))
    app.run(host='0.0.0.0', port=80, debug=0)
