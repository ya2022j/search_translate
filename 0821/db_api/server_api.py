# -*- coding:utf-8 -*-

# 		<script src="https://cdn.staticfile.org/vue/2.7.0/vue.min.js"></script>
#  这里取输入框的内容然后再对接后端。应该是没有使用vue.只解决了路由的部分。
# 其实还是要用的。正常返回一个搜索的html。里面还是要请求搜索的内容的
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
from urllib.parse import quote

a1 = quote("同然") #%E5%90%8C%E7%84%B6
a2 = quote("通り") #%E9%80%9A%E3%82%8A


@app.route('/')
def api_index():

    return "api "

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
    response.headers["Content-Type"] = "application/json;charset=UTF-8"

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
    response.headers["Content-Type"] = "application/json;charset=UTF-8"

    return response




if __name__ == "__main__":
    app.run()