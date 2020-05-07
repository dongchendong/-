# 基于机器学习的PE文件检测系统
## 简介
本系统的核心是基于机器学习的PE文件检测。主要用到了PE文件的格式以及PE文件的特征提取方式，包括字节直方图、字节熵直方图、文本特征、文件信息、文件头、导入和导出表等。还用到了恶意程序检测模型GBDT，以及GBDT的参数优化和持久化，最后实现了使用GBDT进行恶意程序检测。本系统已部署在web服务器上，可以通过以下链接访问http://120.55.46.116/
## 核心文件及文件夹说明
### first.py
* 主要用到了flask框架，建立了相关的路由使得从前端收到的数据能得到有效处理
* 为用户访问本站API创建路由，调用了文件分析函数
### pefeatures.py
* 主要功能就是把PE文件转换成特征向量,PEFeatureExtractor以类的形式存在，提供了唯一的对外接口，用于把保存了PE文件的字节数组转换成特征
### Interface.py
* 该模块基于GBDT模型针对PE文件进行检测。Gym-Malware使用GBDT，在5万个黑样本和5万个白样本上学习，生成的模型保存为文件gradient_boosting.pkl。Interface直接加载该文件，然后对PE文件进行检测
### peinfor.py
* 该模块具体分析了PE结构，调用了外部API实现了获得多个杀毒引擎对该文件的扫描结果。同时生成json文件发送给前端
### userdb.txt 和 userdb2.txt
* 该文件需要配合peutils模块使用，文件中记录着‘壳’的特征信息，相当于壳的数据库
### 未完待续。。
## 本系统使用的python版本及第三方库版本
* python==3.5.
* certifi==2020.4.5.1
* chardet==3.0.4
* click==7.1.1
* cloudpickle==1.3.0
* Flask==1.1.2
* Flask-Uploads==0.2.1
* Flask-WTF==0.14.3
* future==0.18.2
* gym==0.17.1
* idna==2.9
* itsdangerous==1.1.0
* Jinja2==2.11.2
* keystone==0.9.1
* lief==0.7.0
* Markdown==3.2.1
* MarkupSafe==1.1.1
* numpy==1.18.3
* pefile==2019.4.18
* pyglet==1.5.0
* requests==2.23.0
* scikit-learn==0.18.1
* scipy==1.4.1
* six==1.14.0
* urllib3==1.25.9
* Werkzeug==1.0.1
* WTForms==2.3.1

## 本站API调用实例
    import requests

    url = 'http://127.0.0.1:5000/api'
    files = {'file': open('t1.exe', 'rb')}
    data = {'apikey': "123456"}

    response = requests.post(url, files=files, data=data)
    print(response.json())
如果正常，则会返回一大串json数据，如果返回的是`{code:0}`则可能的原因有
* 是apikey填写错误
* files文件或路径有问题
* 上传的不是exe文件，或是其他文件改后缀名导致
## 联系我们
本系统完全开源，如有需要可以在github上与我们互动，还可以加入我们的qq群，我们一起讨论哟！
