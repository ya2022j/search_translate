
# Flask设置允许跨域(Access to XMLHttpRequest 、CORS policy、Access-Control-Allow-Origin)

报错描述：

Access to XMLHttpRequest at 'http://******' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.



后台是flask，解决办法：需要设置flask允许跨域

Flask配Cors跨域,使用flask-cors包,并有两种方式

| 方式| 范围 | 特点 |
| :------| ------: | :------: |
| @cross_origin装饰器 | 单个路由- | 适用于配置特定的API接口 |
| CORS函数 | 配置全局API接口 | 适用于全局的API接口配置 |





```python
pip install flask-cors
```

```python


from flask import Flask
from flask_cors import cross_origin
 
app = Flask(__name__)
 
 
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    return 'hello world'
 
 
if __name__ == '__main__':
    app.run()

```

