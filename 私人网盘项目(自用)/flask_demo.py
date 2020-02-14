from flask import Flask, url_for, make_response, render_template, request
import os

app = Flask(__name__, static_url_path='')


@app.route('/')
def index_main():
    # 将所有文件放置在static/中
    return render_template('index.html')


@app.route('/control/<path>')
def cmd(path):
    if path == '1':
        ts = "<html><body><h3>电脑将在30秒后自动关机</h3><a href='./2'>取消</a></body></html>"
        os.system('shutdown -s -t 30')
        return ts
    if path == '2':
        ts = "<html><body><h3>已取消关机</h3><a href='../'>返回主页</a></body></html>"
        os.system('shutdown -a')
        return ts
    return 'null'


@app.route('/login', methods=['POST', 'GET'])
def login():
    # post请求接收
    if request.method == 'POST':
        if request.form['say'] == 'h':
            return render_template('index2.html')
        else:
            return render_template('index.html')
    return render_template('index.html')
    # return render_template('test.html', error=error)  # , form=form,
    # title="Sign In"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=1)
