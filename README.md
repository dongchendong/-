# 基于机器学习的PE文件检测系统
## 简介
本系统的核心是基于机器学习的PE文件检测。主要用到了PE文件的格式以及PE文件的特征提取方式，包括字节直方图、字节熵直方图、文本特征、文件信息、文件头、导入和导出表等。还用到了恶意程序检测模型GBDT，以及GBDT的参数优化和持久化，最后实现了使用GBDT进行恶意程序检测。本系统已部署在web服务器上，可以通过以下链接访问http://120.55.46.116/
## API调用实例
    import requests

    url = 'http://127.0.0.1:5000/api'
    files = {'file': open('t1.exe', 'rb')}
    data = {'apikey': "123456"}

    response = requests.post(url, files=files, data=data)
    print(response.json())
