# -*- coding: gbk -*-
import os
from flask import Flask, request, url_for, send_from_directory,render_template
from werkzeug.utils import secure_filename
from gym_malware.envs.utils.interface import test


ALLOWED_EXTENSIONS = set(['exe','dll','sys','EXE'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


temp={'���յȼ�': '��', '�����': ['GDI32.dll', 'USER32.dll', 'SHELL32.dll', 'WINMM.dll', 'KERNEL32.dll'], '�ڱ�': {'.text\x00\x00\x00': {'�����ַ': '0x00001000', '�����ַ': '0x00001000', '�����С': '0x0000d000', '�ڱ�����': '0x60000020', '�����С': '0x0000c6df'}, '.rsrc\x00\x00\x00': {'�����ַ': '0x000e6000', '�����ַ': '0x00016000', '�����С': '0x000dc000', '�ڱ�����': '0x40000040', '�����С': '0x000dbf00'}, '.rdata\x00\x00': {'�����ַ': '0x0000e000', '�����ַ': '0x0000e000', '�����С': '0x00003000', '�ڱ�����': '0x40000040', '�����С': '0x00002a02'}, '.data\x00\x00\x00': {'�����ַ': '0x00011000', '�����ַ': '0x00011000', '�����С': '0x00005000', '�ڱ�����': '0xc0000040', '�����С': '0x000d437c'}}, '�ļ�����': 't1.exe', '����ʱ��': '2012-02-18 15:19:17', 'SHA256': '28963f2d99d4b628b58798d60f3b8662ab41939ce2973d6444d34d39664b1572', 'SHA1': 'ecc350f3c0ddaddb622bee84cd0587eebb7937aa', 'PEID���': 'Armadillo v1.71', '������': '6.92%', 'data': {'multiengines': {'is_white': False, 'scan_date': '2020-05-04 08:22:43', 'malware_family': '', 'total2': 25, 'scans': {'NANO': 'safˮ���e', 'vbwebshell': 'saf�Ե�e', 'ESET': 'sa23fe', 'Avira': 'ˮ���������safe', 'Kaspersky': 'safe', 'Tencent': 'safe', 'Antiy': 'safe', 'JiangMin': 'safe', 'Avast': 'safe', 'Trustlook': 'safe', 'Rising': 'safe', 'Microsoft': 'safe', 'Baidu-China': 'safe', 'Kaiwei': 'safe', 'Kingsoft': 'safe', 'K7': 'safe', 'Baidu': 'safe', 'IKARUS': 'safe', 'Panda': 'safe', 'DrWeb': 'safe', 'Qihu360': 'safe', 'Sophos': 'safe', 'ClamAV': 'safe', 'AVG': 'safe', 'GDATA': 'safe'}, 'threat_level': 'clean', 'malware_type': '', 'positives': 0, 'total': 25}}, 'response_code': 0, '������': None, 'verbose_msg': 'OK', '�ļ���С': 991232, 'timee': '2020-05-07 11:31:17', 'MD5': '9b295e0cd111aaa1d5fe774226fc32e0'}

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            re=test(file.filename)
            #print(re)
            #re=temp
            os.remove(file.filename)
            #file_url = url_for('uploaded_file', filename=filename)
            #return html + '<br><img src=' + file_url + '>'
            return render_template('index3.html',data=re)
    return render_template('index1.html')
#
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             file_url = url_for('uploaded_file', filename=filename)
#             return html + '<br><img src=' + file_url + '>'
#     return html

@app.route('/api/',methods=['GET', 'POST'])
def testapi():
    if request.method == 'GET':
        print(request.args['apikey'])
    return "test"


@app.route('/test/')
def testt():

    r1={
        'age':18,
        'name':'cd'
    }
    return render_template('test.html',data=r1)


if __name__ == '__main__':
    app.run()





"""
# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template,request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from gym_malware.envs.utils.interface import test

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # print(request.method)
    # if request.method=='POST':
    #     return test()
    # else:
    #     print('no')
    print("@@@@")
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        print("qk1")
    else:
        file_url = None
        print("qk2")
        #return render_template('test.jpg')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()




# from flask import Flask, render_template
#
# app=Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("index.html",title='Home')
#
#
# app.run()
"""