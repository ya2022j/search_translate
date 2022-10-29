
#  fronttend

# 		<script src="https://cdn.staticfile.org/vue/2.7.0/vue.min.js"></script>
#  这里取输入框的内容然后再对接后端。应该是没有使用vue.只解决了路由的部分。
# 其实还是要用的。正常返回一个搜索的html。里面还是要请求搜索的内容的
import time
import os
import shutil
from flask import Flask, jsonify,request,make_response,render_template

from flask_cors import cross_origin


import os
app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False




#
@app.route('/同然')
@cross_origin()
def api1():
    df = {}
    df["furinaga_word"] = "<h3><ruby>同然<rp>(</rp><rt>どうぜん</rt><rp>)</rp></ruby></h3>"
    df["words_format"] = "名・形动"
    df["words_meanings"] = "<br>（和……）一样；（简直跟）……一样，等于……。（同じであること。同様。）<br><br>"
    # df["example_ja"] = [,,]
    # df["example_translate"] = [,,]
    df["df_example"]= [
     ["これでは<ruby>失敗<rp>(</rp><rt>しっぱい</rt><rp>)</rp></ruby>も<ruby>同然<rp>(</rp><rt>どうぜん</rt><rp>)</rp></ruby>だ","那样就等于失败了。"],
     ["あいつは<ruby>獣<rp>(</rp><rt>しし</rt><rp>)</rp></ruby>も<ruby>同然<rp>(</rp><rt>どうぜん</rt><rp>)</rp></ruby>だ","他简直和野兽一样。"],
     ["ただも<ruby>同然<rp>(</rp><rt>どうぜん</rt><rp>)</rp></ruby>の<ruby>値段<rp>(</rp><rt>ねだん</rt><rp>)</rp></ruby>","等于白给〔奉送〕的价钱。"],
    ]

    response = make_response(jsonify(df))
    # response.headers["Content-Type"] = "application/json;charset=UTF-8"

    return response


@app.route('/通り')
@cross_origin()
def api2():
    df = {}
    df["furinaga_word"] = "<h3><ruby>通<rp>(</rp><rt>とお</rt><rp>)</rp></ruby>り</h3>"
    df["words_format"] = "名・接尾・助数詞"
    df["words_meanings"] = "<br>&nbsp;&nbsp;人や車のとおるところ。道路。往来。「にぎやかな—」<br>&nbsp;&nbsp;人や車が行ったり来たりすること。通行。ゆきき。往来。「車の—が激しい道」<br><br>"
    # df["example_ja"] = [,,]
    # df["example_translate"] = [,,]
    df["df_example"]= [
        ["<ruby>君<rp>(</rp><rt>きみ</rt><rp>)</rp></ruby>の<ruby>考<rp>(</rp><rt>かんが</rt><rp>)</rp></ruby>え<ruby>通<rp>(</rp><rt>どお</rt><rp>)</rp></ruby>りにしたまえ","하고 싶은 대로 하세요, 하고 싶은 대로 하세요."],
        ["<ruby>予想<rp>(</rp><rt>よそう</rt><rp>)</rp></ruby><ruby>通<rp>(</rp><rt>どお</rt><rp>)</rp></ruby>りの<ruby>結果<rp>(</rp><rt>けっか</rt><rp>)</rp></ruby>が<ruby>出<rp>(</rp><rt>で</rt><rp>)</rp></ruby>た","결과는 예상대로였습니다."],
        ["<ruby>代表<rp>(</rp><rt>だいひょう</rt><rp>)</rp></ruby><ruby>団<rp>(</rp><rt>だん</rt><rp>)</rp></ruby>は<ruby>予定<rp>(</rp><rt>よてい</rt><rp>)</rp></ruby><ruby>通<rp>(</rp><rt>どお</rt><rp>)</rp></ruby>りきょう<ruby>東京<rp>(</rp><rt>とうきょう</rt><rp>)</rp></ruby>に<ruby>到着<rp>(</rp><rt>とうちゃく</rt><rp>)</rp></ruby>した","대표단은 예정대로 오늘 도쿄에 도착했다."],
        ["<ruby>期日<rp>(</rp><rt>きじつ</rt><rp>)</rp></ruby><ruby>通<rp>(</rp><rt>どお</rt><rp>)</rp></ruby>り<ruby>任務<rp>(</rp><rt>にんむ</rt><rp>)</rp></ruby>を<ruby>完成<rp>(</rp><rt>かんせい</rt><rp>)</rp></ruby>する","기일대로 임무를 완성한다"]
    ]

    response = make_response(jsonify(df))
    # response.headers["Content-Type"] = "application/json;charset=UTF-8"

    return response

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
    replace_text = content
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
        new_html = os.path.join(os.path.join(os.getcwd(), "templates"), "{0}.html".format(content))
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
    if len(kw) == 0:
        return render_template("homepage.html")
    elif kw not in ("同然","通り"):
        return render_template("homepage.html")
    else:
        # 1. search_module.html  templates
        # 2.
        if os.path.exists(os.path.join(os.path.join(os.getcwd(),"templates"),"{0}.html".format(kw))):
            return render_template("{0}.html".format(kw))
        else:
            add_search_html("search_module.html", kw)
            return render_template("{0}.html".format(kw))
            # replace  -->"search_module.html"    'http://127.0.0.1:5000/todos'

if __name__ == "__main__":
    app.run()


