from flask import Flask, jsonify,request,make_response,render_template

from flask_cors import cross_origin



app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/todos')
@cross_origin()
def get_list():
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


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/2')
def get_list2():
    return render_template("index_.html")


@app.route('/3')
def de():
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run(debug=True)