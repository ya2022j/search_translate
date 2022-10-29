# -*- coding:utf-8 -*-

# 		<script src="https://cdn.staticfile.org/vue/2.7.0/vue.min.js"></script>
#  这里取输入框的内容然后再对接后端。应该是没有使用vue.只解决了路由的部分。
# 其实还是要用的。正常返回一个搜索的html。里面还是要请求搜索的内容的

# python3 ..../%E7%9B%B8%E5%86%8C/ 把乱码部分改为汉字。编码。
# https://www.cnblogs.com/helloxiaoyu/p/8779700.html
import time
import os
import shutil
from flask import Flask, jsonify,request,make_response,render_template

from flask_cors import cross_origin


import os
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False

CORS(app,supports_credentials=True)


from urllib.parse import quote,unquote




@app.route("/")
def index():
    return  render_template("homepage.html")


#  /login?next=/  -----> url_for('login', next='/')
# /search?utf8=✓  -----> url_for('search', utf8='✓')








def copyfile(oldfilename, newfilename):
    shutil.copy(oldfilename, newfilename)





def add_search_html(jsfile,content):
    # 创建一个变量并存储我们要搜索的文本
    search_text = "modules"
    # 创建一个变量并存储我们要添加的文本

    replace_text = content # 要把输出内容解码

    print("replace_text----->",replace_text)
    # 使用 open() 函数以只读模式打开我们的文本文件
    with open(jsfile, 'r', encoding='UTF-8') as file:
        # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
        data = file.read()
        # 使用 replace() 函数搜索和替换文本
        data = data.replace(search_text, replace_text)
    # 以只写模式打开我们的文本文件以写入替换的内容
    with open(jsfile, 'w', encoding='UTF-8') as file:
        # 在我们的文本文件中写入替换的数据
        file.write(data)
    # 打印文本已替换
    print("文本已替换")
    # 文本最后还要还原成  ja_content
    # 创建一个变量并存储我们要搜索的文本
    search_text = content
    # 创建一个变量并存储我们要添加的文本
    replace_text = "modules"
    # 使用 open() 函数以只读模式打开我们的文本文件
    with open(jsfile, 'r', encoding='UTF-8') as file:
        # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
        data = file.read()

        # 使用 replace() 函数搜索和替换文本
        data = data.replace(search_text, replace_text)


        # 把修改后的html文件放到templates文件夹中，同时更换名称
        new_html = os.path.join(os.path.join(os.getcwd(), "templates"), "{0}.html".format(search_text))
        # cp -i 原文件 目的路径/重命名文件  linux  os.system("cp -i search_module.html  {0}".format(new_html))
        copyfile("search_module.html", new_html)



        time.sleep(0.1)
    # 以只写模式打开我们的文本文件以写入替换的内容
    with open(jsfile, 'w', encoding='UTF-8') as file:
        # 在我们的文本文件中写入替换的数据
        file.write(data)
    print("文本恢复")



@app.route("/search")
def index1():
    # http://127.0.0.1:5000/search?utf8=%E2%9C%93&keyword=asdf
    kw = request.args.get("keyword")
    kw = unquote(kw)

    print("kw----->",kw)
    if len(kw) == 0:
        return render_template("homepage.html")
    elif kw not in ("同然","通り"):
        return render_template("homepage.html")
    else:
        # 1. search_module.html  templates
        # 2.
        if os.path.exists(os.path.join(os.path.join(os.getcwd(),"templates"),"{0}.html".format(quote(kw)))):
            return render_template("{0}.html".format(quote(kw)))
        else:
            add_search_html("search_module.html", quote(kw))
            return render_template("{0}.html".format(quote(kw)))
            # replace  -->"search_module.html"    'http://127.0.0.1:5000/todos'

if __name__ == "__main__":
    app.run(port=8002)


