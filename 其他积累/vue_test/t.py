from flask import Flask, jsonify,request,make_response,render_template

from flask_cors import cross_origin



app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/todos')
@cross_origin()
def get_list():

    data = [
    {
        "id": 1,
        "code": 9983,
        "name": "ファーストリテイリング",
        "type": "小売業",
        "weight": 0.1014,
        "last_price": 170.75,
        "change_v": -0.77,
        "change_r": "(-0.45%)"
    },
    {
        "id": 2,
        "code": 8035,
        "name": "東京エレクトロン",
        "type": "電気機器",
        "weight": 0.0582,
        "last_price": 170.0,
        "change_v": -0.5,
        "change_r": "(-0.3%)"
    },
    {
        "id": 3,
        "code": 9984,
        "name": "ソフトバンクグループ",
        "type": "通信",
        "weight": 0.0425,
        "last_price": 169.25,
        "change_v": -0.23,
        "change_r": "(-0.39%)"
    },
    {
        "id": 4,
        "code": 9433,
        "name": "ＫＤＤＩ",
        "type": "通信",
        "weight": 0.0326,
        "last_price": 168.5,
        "change_v": 0.04,
        "change_r": "(-0.81%)"
    },
    {
        "id": 5,
        "code": 6367,
        "name": "ダイキン工業",
        "type": "機械",
        "weight": 0.0294,
        "last_price": 167.75,
        "change_v": 0.31,
        "change_r": "(-0.123%)"
    },
    {
        "id": 6,
        "code": 6954,
        "name": "ファナック",
        "type": "電気機器",
        "weight": 0.0289,
        "last_price": 167.0,
        "change_v": 0.58,
        "change_r": "(-0.165%)"
    },
    {
        "id": 7,
        "code": 4543,
        "name": "テルモ",
        "type": "精密機器",
        "weight": 0.0229,
        "last_price": 166.25,
        "change_v": 0.85,
        "change_r": "(-0.207%)"
    },
    {
        "id": 8,
        "code": 4063,
        "name": "信越化学工業",
        "type": "化学",
        "weight": 0.0214,
        "last_price": 165.5,
        "change_v": 1.12,
        "change_r": "(-0.249%)"
    },
    {
        "id": 9,
        "code": 6857,
        "name": "アドバンテスト",
        "type": "電気機器",
        "weight": 0.0198,
        "last_price": 164.75,
        "change_v": 1.39,
        "change_r": "(-0.291%)"
    },
    {
        "id": 10,
        "code": 6098,
        "name": "リクルートホールディングス",
        "type": "サービス",
        "weight": 0.0188,
        "last_price": 164.0,
        "change_v": 1.66,
        "change_r": "(-0.333%)"
    },
    {
        "id": 11,
        "code": 6971,
        "name": "京セラ",
        "type": "電気機器",
        "weight": 0.0186,
        "last_price": 163.25,
        "change_v": 1.93,
        "change_r": "(-0.375%)"
    },
    {
        "id": 12,
        "code": 6762,
        "name": "ＴＤＫ",
        "type": "電気機器",
        "weight": 0.0158,
        "last_price": 162.5,
        "change_v": 2.2,
        "change_r": "(-0.417%)"
    },
    {
        "id": 13,
        "code": 6758,
        "name": "ソニーグループ",
        "type": "電気機器",
        "weight": 0.0148,
        "last_price": 161.75,
        "change_v": 2.47,
        "change_r": "(-0.459%)"
    },
    {
        "id": 14,
        "code": 7733,
        "name": "オリンパス",
        "type": "精密機器",
        "weight": 0.0142,
        "last_price": 161.0,
        "change_v": 2.74,
        "change_r": "(-0.501%)"
    },
    {
        "id": 15,
        "code": 4519,
        "name": "中外製薬",
        "type": "医薬品",
        "weight": 0.0142,
        "last_price": 160.25,
        "change_v": 3.01,
        "change_r": "(-0.543%)"
    },
    {
        "id": 16,
        "code": 2413,
        "name": "エムスリー",
        "type": "サービス",
        "weight": 0.014,
        "last_price": 159.5,
        "change_v": 3.28,
        "change_r": "(-0.585%)"
    },
    {
        "id": 17,
        "code": 7203,
        "name": "トヨタ自動車",
        "type": "自動車",
        "weight": 0.0135,
        "last_price": 158.75,
        "change_v": 3.55,
        "change_r": "(-0.627%)"
    },
    {
        "id": 18,
        "code": 4568,
        "name": "第一三共",
        "type": "医薬品",
        "weight": 0.0134,
        "last_price": 158.0,
        "change_v": 3.82,
        "change_r": "(-0.669%)"
    },
    {
        "id": 19,
        "code": 4503,
        "name": "アステラス製薬",
        "type": "医薬品",
        "weight": 0.0132,
        "last_price": 157.25,
        "change_v": 4.09,
        "change_r": "(-0.711%)"
    },
    {
        "id": 20,
        "code": 7832,
        "name": "バンダイナムコホールディングス",
        "type": "その他製造",
        "weight": 0.0131,
        "last_price": 156.5,
        "change_v": 4.36,
        "change_r": "(-0.753%)"
    },
    {
        "id": 21,
        "code": 9613,
        "name": "エヌ・ティ・ティ・データ",
        "type": "通信",
        "weight": 0.0127,
        "last_price": 155.75,
        "change_v": 4.63,
        "change_r": "(-0.795%)"
    },
    {
        "id": 22,
        "code": 9735,
        "name": "セコム",
        "type": "サービス",
        "weight": 0.0112,
        "last_price": 155.0,
        "change_v": 4.9,
        "change_r": "(-0.837%)"
    },
    {
        "id": 23,
        "code": 6988,
        "name": "日東電工",
        "type": "化学",
        "weight": 0.0108,
        "last_price": 154.25,
        "change_v": 5.17,
        "change_r": "(-0.879%)"
    },
    {
        "id": 24,
        "code": 2801,
        "name": "キッコーマン",
        "type": "食品",
        "weight": 0.0099,
        "last_price": 153.5,
        "change_v": 5.44,
        "change_r": "(-0.921%)"
    },
    {
        "id": 25,
        "code": 9766,
        "name": "コナミグループ",
        "type": "サービス",
        "weight": 0.0099,
        "last_price": 152.75,
        "change_v": 5.71,
        "change_r": "(-0.963%)"
    },
    {
        "id": 26,
        "code": 4704,
        "name": "トレンドマイクロ",
        "type": "サービス",
        "weight": 0.0097,
        "last_price": 152.0,
        "change_v": 5.98,
        "change_r": "(-0.1005%)"
    },
    {
        "id": 27,
        "code": 4901,
        "name": "富士フイルムホールディングス",
        "type": "化学",
        "weight": 0.0096,
        "last_price": 151.25,
        "change_v": 6.25,
        "change_r": "(-0.1047%)"
    },
    {
        "id": 28,
        "code": 6645,
        "name": "オムロン",
        "type": "電気機器",
        "weight": 0.0093,
        "last_price": 150.5,
        "change_v": 6.52,
        "change_r": "(-0.1089%)"
    },
    {
        "id": 29,
        "code": 6902,
        "name": "デンソー",
        "type": "電気機器",
        "weight": 0.0091,
        "last_price": 149.75,
        "change_v": 6.79,
        "change_r": "(-0.1131%)"
    },
    {
        "id": 30,
        "code": 4507,
        "name": "塩野義製薬",
        "type": "医薬品",
        "weight": 0.0086,
        "last_price": 149.0,
        "change_v": 7.06,
        "change_r": "(-0.1173%)"
    },
    {
        "id": 31,
        "code": 7267,
        "name": "本田技研工業",
        "type": "自動車",
        "weight": 0.0086,
        "last_price": 148.25,
        "change_v": 7.33,
        "change_r": "(-0.1215%)"
    },
    {
        "id": 32,
        "code": 4021,
        "name": "日産化学",
        "type": "化学",
        "weight": 0.0085,
        "last_price": 147.5,
        "change_v": 7.6,
        "change_r": "(-0.1257%)"
    },
    {
        "id": 33,
        "code": 6981,
        "name": "村田製作所",
        "type": "電気機器",
        "weight": 0.0078,
        "last_price": 146.75,
        "change_v": 7.87,
        "change_r": "(-0.1299%)"
    },
    {
        "id": 34,
        "code": 4523,
        "name": "エーザイ",
        "type": "医薬品",
        "weight": 0.0077,
        "last_price": 146.0,
        "change_v": 8.14,
        "change_r": "(-0.1341%)"
    },
    {
        "id": 35,
        "code": 3659,
        "name": "ネクソン",
        "type": "サービス",
        "weight": 0.0076,
        "last_price": 145.25,
        "change_v": 8.41,
        "change_r": "(-0.1383%)"
    },
    {
        "id": 36,
        "code": 7974,
        "name": "任天堂",
        "type": "サービス",
        "weight": 0.0075,
        "last_price": 144.5,
        "change_v": 8.68,
        "change_r": "(-0.1425%)"
    },
    {
        "id": 37,
        "code": 4452,
        "name": "花王",
        "type": "化学",
        "weight": 0.0073,
        "last_price": 143.75,
        "change_v": 8.95,
        "change_r": "(-0.1467%)"
    },
    {
        "id": 38,
        "code": 7951,
        "name": "ヤマハ",
        "type": "その他製造",
        "weight": 0.0071,
        "last_price": 143.0,
        "change_v": 9.22,
        "change_r": "(-0.1509%)"
    },
    {
        "id": 39,
        "code": 4911,
        "name": "資生堂",
        "type": "化学",
        "weight": 0.0069,
        "last_price": 142.25,
        "change_v": 9.49,
        "change_r": "(-0.1551%)"
    },
    {
        "id": 40,
        "code": 3382,
        "name": "セブン＆アイ・ホールディングス",
        "type": "小売業",
        "weight": 0.0069,
        "last_price": 141.5,
        "change_v": 9.76,
        "change_r": "(-0.1593%)"
    },
    {
        "id": 41,
        "code": 6861,
        "name": "キーエンス",
        "type": "電気機器",
        "weight": 0.0066,
        "last_price": 140.75,
        "change_v": 10.03,
        "change_r": "(-0.1635%)"
    },
    {
        "id": 42,
        "code": 5108,
        "name": "ブリヂストン",
        "type": "ゴム",
        "weight": 0.0066,
        "last_price": 140.0,
        "change_v": 10.3,
        "change_r": "(-0.1677%)"
    },
    {
        "id": 43,
        "code": 4578,
        "name": "大塚ホールディングス",
        "type": "医薬品",
        "weight": 0.006,
        "last_price": 139.25,
        "change_v": 10.57,
        "change_r": "(-0.1719%)"
    },
    {
        "id": 44,
        "code": 7751,
        "name": "キヤノン",
        "type": "電気機器",
        "weight": 0.006,
        "last_price": 138.5,
        "change_v": 10.84,
        "change_r": "(-0.1761%)"
    },
    {
        "id": 45,
        "code": 6976,
        "name": "太陽誘電",
        "type": "電気機器",
        "weight": 0.0059,
        "last_price": 137.75,
        "change_v": 11.11,
        "change_r": "(-0.1803%)"
    },
    {
        "id": 46,
        "code": 4324,
        "name": "電通グループ",
        "type": "サービス",
        "weight": 0.0059,
        "last_price": 137.0,
        "change_v": 11.38,
        "change_r": "(-0.1845%)"
    },
    {
        "id": 47,
        "code": 6506,
        "name": "安川電機",
        "type": "電気機器",
        "weight": 0.0058,
        "last_price": 136.25,
        "change_v": 11.65,
        "change_r": "(-0.1887%)"
    },
    {
        "id": 48,
        "code": 2502,
        "name": "アサヒグループホールディングス",
        "type": "食品",
        "weight": 0.0058,
        "last_price": 135.5,
        "change_v": 11.92,
        "change_r": "(-0.1929%)"
    },
    {
        "id": 49,
        "code": 8015,
        "name": "豊田通商",
        "type": "商社",
        "weight": 0.0057,
        "last_price": 134.75,
        "change_v": 12.19,
        "change_r": "(-0.1971%)"
    },
    {
        "id": 50,
        "code": 7269,
        "name": "スズキ",
        "type": "自動車",
        "weight": 0.0055,
        "last_price": 134.0,
        "change_v": 12.46,
        "change_r": "(-0.2013%)"
    },
    {
        "id": 51,
        "code": 6724,
        "name": "セイコーエプソン",
        "type": "電気機器",
        "weight": 0.005,
        "last_price": 133.25,
        "change_v": 12.73,
        "change_r": "(-0.2055%)"
    },
    {
        "id": 52,
        "code": 8058,
        "name": "三菱商事",
        "type": "商社",
        "weight": 0.005,
        "last_price": 132.5,
        "change_v": 13.0,
        "change_r": "(-0.2097%)"
    },
    {
        "id": 53,
        "code": 4502,
        "name": "武田薬品工業",
        "type": "医薬品",
        "weight": 0.005,
        "last_price": 131.75,
        "change_v": 13.27,
        "change_r": "(-0.2139%)"
    },
    {
        "id": 54,
        "code": 8766,
        "name": "東京海上ホールディングス",
        "type": "保険",
        "weight": 0.0049,
        "last_price": 131.0,
        "change_v": 13.54,
        "change_r": "(-0.2181%)"
    },
    {
        "id": 55,
        "code": 8001,
        "name": "伊藤忠商事",
        "type": "商社",
        "weight": 0.0049,
        "last_price": 130.25,
        "change_v": 13.81,
        "change_r": "(-0.2223%)"
    },
    {
        "id": 56,
        "code": 8830,
        "name": "住友不動産",
        "type": "不動産",
        "weight": 0.0046,
        "last_price": 129.5,
        "change_v": 14.08,
        "change_r": "(-0.2265%)"
    },
    {
        "id": 57,
        "code": 2802,
        "name": "味の素",
        "type": "食品",
        "weight": 0.0044,
        "last_price": 128.75,
        "change_v": 14.35,
        "change_r": "(-0.2307%)"
    },
    {
        "id": 58,
        "code": 1925,
        "name": "大和ハウス工業",
        "type": "建設",
        "weight": 0.0042,
        "last_price": 128.0,
        "change_v": 14.62,
        "change_r": "(-0.2349%)"
    },
    {
        "id": 59,
        "code": 4151,
        "name": "協和キリン",
        "type": "医薬品",
        "weight": 0.004,
        "last_price": 127.25,
        "change_v": 14.89,
        "change_r": "(-0.2391%)"
    },
    {
        "id": 60,
        "code": 6301,
        "name": "小松製作所",
        "type": "機械",
        "weight": 0.0038,
        "last_price": 126.5,
        "change_v": 15.16,
        "change_r": "(-0.2433%)"
    },
    {
        "id": 61,
        "code": 8801,
        "name": "三井不動産",
        "type": "不動産",
        "weight": 0.0038,
        "last_price": 125.75,
        "change_v": 15.43,
        "change_r": "(-0.2475%)"
    },
    {
        "id": 62,
        "code": 8031,
        "name": "三井物産",
        "type": "商社",
        "weight": 0.0037,
        "last_price": 125.0,
        "change_v": 15.7,
        "change_r": "(-0.2517%)"
    },
    {
        "id": 63,
        "code": 6305,
        "name": "日立建機",
        "type": "機械",
        "weight": 0.0037,
        "last_price": 124.25,
        "change_v": 15.97,
        "change_r": "(-0.2559%)"
    },
    {
        "id": 64,
        "code": 8267,
        "name": "イオン",
        "type": "小売業",
        "weight": 0.0034,
        "last_price": 123.5,
        "change_v": 16.24,
        "change_r": "(-0.2601%)"
    },
    {
        "id": 65,
        "code": 1721,
        "name": "コムシスホールディングス",
        "type": "建設",
        "weight": 0.0034,
        "last_price": 122.75,
        "change_v": 16.51,
        "change_r": "(-0.2643%)"
    },
    {
        "id": 66,
        "code": 7272,
        "name": "ヤマハ発動機",
        "type": "自動車",
        "weight": 0.0032,
        "last_price": 122.0,
        "change_v": 16.78,
        "change_r": "(-0.2685%)"
    },
    {
        "id": 67,
        "code": 8252,
        "name": "丸井グループ",
        "type": "小売業",
        "weight": 0.0031,
        "last_price": 121.25,
        "change_v": 17.05,
        "change_r": "(-0.2727%)"
    },
    {
        "id": 68,
        "code": 2914,
        "name": "日本たばこ産業",
        "type": "食品",
        "weight": 0.003,
        "last_price": 120.5,
        "change_v": 17.32,
        "change_r": "(-0.2769%)"
    },
    {
        "id": 69,
        "code": 6479,
        "name": "ミネベアミツミ",
        "type": "電気機器",
        "weight": 0.003,
        "last_price": 119.75,
        "change_v": 17.59,
        "change_r": "(-0.2811%)"
    },
    {
        "id": 70,
        "code": 8591,
        "name": "オリックス",
        "type": "その他金融",
        "weight": 0.003,
        "last_price": 119.0,
        "change_v": 17.86,
        "change_r": "(-0.2853%)"
    },
    {
        "id": 71,
        "code": 1928,
        "name": "積水ハウス",
        "type": "建設",
        "weight": 0.003,
        "last_price": 118.25,
        "change_v": 18.13,
        "change_r": "(-0.2895%)"
    },
    {
        "id": 72,
        "code": 6841,
        "name": "横河電機",
        "type": "電気機器",
        "weight": 0.003,
        "last_price": 117.5,
        "change_v": 18.4,
        "change_r": "(-0.2937%)"
    },
    {
        "id": 73,
        "code": 9064,
        "name": "ヤマトホールディングス",
        "type": "陸運",
        "weight": 0.0029,
        "last_price": 116.75,
        "change_v": 18.67,
        "change_r": "(-0.2979%)"
    },
    {
        "id": 74,
        "code": 7270,
        "name": "ＳＵＢＡＲＵ",
        "type": "自動車",
        "weight": 0.0029,
        "last_price": 116.0,
        "change_v": 18.94,
        "change_r": "(-0.3021%)"
    },
    {
        "id": 75,
        "code": 5332,
        "name": "ＴＯＴＯ",
        "type": "窯業",
        "weight": 0.0028,
        "last_price": 115.25,
        "change_v": 19.21,
        "change_r": "(-0.3063%)"
    },
    {
        "id": 76,
        "code": 6326,
        "name": "クボタ",
        "type": "機械",
        "weight": 0.0028,
        "last_price": 114.5,
        "change_v": 19.48,
        "change_r": "(-0.3105%)"
    },
    {
        "id": 77,
        "code": 2503,
        "name": "キリンホールディングス",
        "type": "食品",
        "weight": 0.0028,
        "last_price": 113.75,
        "change_v": 19.75,
        "change_r": "(-0.3147%)"
    },
    {
        "id": 78,
        "code": 8697,
        "name": "日本取引所グループ",
        "type": "その他金融",
        "weight": 0.0027,
        "last_price": 113.0,
        "change_v": 20.02,
        "change_r": "(-0.3189%)"
    },
    {
        "id": 79,
        "code": 5713,
        "name": "住友金属鉱山",
        "type": "非鉄・金属",
        "weight": 0.0027,
        "last_price": 112.25,
        "change_v": 20.29,
        "change_r": "(-0.3231%)"
    },
    {
        "id": 80,
        "code": 2282,
        "name": "日本ハム",
        "type": "食品",
        "weight": 0.0025,
        "last_price": 111.5,
        "change_v": 20.56,
        "change_r": "(-0.3273%)"
    },
    {
        "id": 81,
        "code": 8802,
        "name": "三菱地所",
        "type": "不動産",
        "weight": 0.0025,
        "last_price": 110.75,
        "change_v": 20.83,
        "change_r": "(-0.3315%)"
    },
    {
        "id": 82,
        "code": 5333,
        "name": "日本碍子",
        "type": "窯業",
        "weight": 0.0025,
        "last_price": 110.0,
        "change_v": 21.1,
        "change_r": "(-0.3357%)"
    },
    {
        "id": 83,
        "code": 7735,
        "name": "ＳＣＲＥＥＮホールディングス",
        "type": "電気機器",
        "weight": 0.0024,
        "last_price": 109.25,
        "change_v": 21.37,
        "change_r": "(-0.3399%)"
    },
    {
        "id": 84,
        "code": 8053,
        "name": "住友商事",
        "type": "商社",
        "weight": 0.0024,
        "last_price": 108.5,
        "change_v": 21.64,
        "change_r": "(-0.3441%)"
    },
    {
        "id": 85,
        "code": 6702,
        "name": "富士通",
        "type": "電気機器",
        "weight": 0.0023,
        "last_price": 107.75,
        "change_v": 21.91,
        "change_r": "(-0.3483%)"
    },
    {
        "id": 86,
        "code": 9009,
        "name": "京成電鉄",
        "type": "鉄道・バス",
        "weight": 0.0023,
        "last_price": 107.0,
        "change_v": 22.18,
        "change_r": "(-0.3525%)"
    },
    {
        "id": 87,
        "code": 9301,
        "name": "三菱倉庫",
        "type": "倉庫",
        "weight": 0.0022,
        "last_price": 106.25,
        "change_v": 22.45,
        "change_r": "(-0.3567%)"
    },
    {
        "id": 88,
        "code": 8253,
        "name": "クレディセゾン",
        "type": "その他金融",
        "weight": 0.0021,
        "last_price": 105.5,
        "change_v": 22.72,
        "change_r": "(-0.3609%)"
    },
    {
        "id": 89,
        "code": 2002,
        "name": "日清製粉グループ本社",
        "type": "食品",
        "weight": 0.0021,
        "last_price": 104.75,
        "change_v": 22.99,
        "change_r": "(-0.3651%)"
    },
    {
        "id": 90,
        "code": 1963,
        "name": "日揮ホールディングス",
        "type": "建設",
        "weight": 0.0021,
        "last_price": 104.0,
        "change_v": 23.26,
        "change_r": "(-0.3693%)"
    },
    {
        "id": 91,
        "code": 9022,
        "name": "東海旅客鉄道",
        "type": "鉄道・バス",
        "weight": 0.002,
        "last_price": 103.25,
        "change_v": 23.53,
        "change_r": "(-0.3735%)"
    },
    {
        "id": 92,
        "code": 9434,
        "name": "ソフトバンク",
        "type": "通信",
        "weight": 0.0019,
        "last_price": 102.5,
        "change_v": 23.8,
        "change_r": "(-0.3777%)"
    },
    {
        "id": 93,
        "code": 9432,
        "name": "日本電信電話",
        "type": "通信",
        "weight": 0.0019,
        "last_price": 101.75,
        "change_v": 24.07,
        "change_r": "(-0.3819%)"
    },
    {
        "id": 94,
        "code": 7731,
        "name": "ニコン",
        "type": "精密機器",
        "weight": 0.0019,
        "last_price": 101.0,
        "change_v": 24.34,
        "change_r": "(-0.3861%)"
    },
    {
        "id": 95,
        "code": 5802,
        "name": "住友電気工業",
        "type": "非鉄・金属",
        "weight": 0.0019,
        "last_price": 100.25,
        "change_v": 24.61,
        "change_r": "(-0.3903%)"
    },
    {
        "id": 96,
        "code": 7912,
        "name": "大日本印刷",
        "type": "その他製造",
        "weight": 0.0019,
        "last_price": 99.5,
        "change_v": 24.88,
        "change_r": "(-0.3945%)"
    },
    {
        "id": 97,
        "code": 6503,
        "name": "三菱電機",
        "type": "電気機器",
        "weight": 0.0018,
        "last_price": 98.75,
        "change_v": 25.15,
        "change_r": "(-0.3987%)"
    },
    {
        "id": 98,
        "code": 2269,
        "name": "明治ホールディングス",
        "type": "食品",
        "weight": 0.0018,
        "last_price": 98.0,
        "change_v": 25.42,
        "change_r": "(-0.4029%)"
    },
    {
        "id": 99,
        "code": 6770,
        "name": "アルプスアルパイン",
        "type": "電気機器",
        "weight": 0.0017,
        "last_price": 97.25,
        "change_v": 25.69,
        "change_r": "(-0.4071%)"
    },
    {
        "id": 100,
        "code": 5019,
        "name": "出光興産",
        "type": "石油",
        "weight": 0.0017,
        "last_price": 96.5,
        "change_v": 25.96,
        "change_r": "(-0.4113%)"
    },
    {
        "id": 101,
        "code": 6501,
        "name": "日立製作所",
        "type": "電気機器",
        "weight": 0.0017,
        "last_price": 95.75,
        "change_v": 26.23,
        "change_r": "(-0.4155%)"
    },
    {
        "id": 102,
        "code": 8725,
        "name": "ＭＳ＆ＡＤインシュアランスグループホールディングス",
        "type": "保険",
        "weight": 0.0016,
        "last_price": 95.0,
        "change_v": 26.5,
        "change_r": "(-0.4197%)"
    },
    {
        "id": 103,
        "code": 6952,
        "name": "カシオ計算機",
        "type": "電気機器",
        "weight": 0.0016,
        "last_price": 94.25,
        "change_v": 26.77,
        "change_r": "(-0.4239%)"
    },
    {
        "id": 104,
        "code": 8002,
        "name": "丸紅",
        "type": "商社",
        "weight": 0.0016,
        "last_price": 93.5,
        "change_v": 27.04,
        "change_r": "(-0.4281%)"
    },
    {
        "id": 105,
        "code": 6504,
        "name": "富士電機",
        "type": "電気機器",
        "weight": 0.0015,
        "last_price": 92.75,
        "change_v": 27.31,
        "change_r": "(-0.4323%)"
    },
    {
        "id": 106,
        "code": 2871,
        "name": "ニチレイ",
        "type": "食品",
        "weight": 0.0015,
        "last_price": 92.0,
        "change_v": 27.58,
        "change_r": "(-0.4365%)"
    },
    {
        "id": 107,
        "code": 8630,
        "name": "ＳＯＭＰＯホールディングス",
        "type": "保険",
        "weight": 0.0015,
        "last_price": 91.25,
        "change_v": 27.85,
        "change_r": "(-0.4407%)"
    },
    {
        "id": 108,
        "code": 7911,
        "name": "凸版印刷",
        "type": "その他製造",
        "weight": 0.0014,
        "last_price": 90.5,
        "change_v": 28.12,
        "change_r": "(-0.4449%)"
    },
    {
        "id": 109,
        "code": 6752,
        "name": "パナソニックホールディングス",
        "type": "電気機器",
        "weight": 0.0014,
        "last_price": 89.75,
        "change_v": 28.39,
        "change_r": "(-0.4491%)"
    },
    {
        "id": 110,
        "code": 9104,
        "name": "商船三井",
        "type": "海運",
        "weight": 0.0014,
        "last_price": 89.0,
        "change_v": 28.66,
        "change_r": "(-0.4533%)"
    },
    {
        "id": 111,
        "code": 2531,
        "name": "宝ホールディングス",
        "type": "食品",
        "weight": 0.0014,
        "last_price": 88.25,
        "change_v": 28.93,
        "change_r": "(-0.4575%)"
    },
    {
        "id": 112,
        "code": 3405,
        "name": "クラレ",
        "type": "化学",
        "weight": 0.0013,
        "last_price": 87.5,
        "change_v": 29.2,
        "change_r": "(-0.4617%)"
    },
    {
        "id": 113,
        "code": 5301,
        "name": "東海カーボン",
        "type": "窯業",
        "weight": 0.0013,
        "last_price": 86.75,
        "change_v": 29.47,
        "change_r": "(-0.4659%)"
    },
    {
        "id": 114,
        "code": 6113,
        "name": "アマダ",
        "type": "機械",
        "weight": 0.0013,
        "last_price": 86.0,
        "change_v": 29.74,
        "change_r": "(-0.4701%)"
    },
    {
        "id": 115,
        "code": 3407,
        "name": "旭化成",
        "type": "化学",
        "weight": 0.0013,
        "last_price": 85.25,
        "change_v": 30.01,
        "change_r": "(-0.4743%)"
    },
    {
        "id": 116,
        "code": 6753,
        "name": "シャープ",
        "type": "電気機器",
        "weight": 0.0013,
        "last_price": 84.5,
        "change_v": 30.28,
        "change_r": "(-0.4785%)"
    },
    {
        "id": 117,
        "code": 7752,
        "name": "リコー",
        "type": "電気機器",
        "weight": 0.0013,
        "last_price": 83.75,
        "change_v": 30.55,
        "change_r": "(-0.4827%)"
    },
    {
        "id": 118,
        "code": 3099,
        "name": "三越伊勢丹ホールディングス",
        "type": "小売業",
        "weight": 0.0013,
        "last_price": 83.0,
        "change_v": 30.82,
        "change_r": "(-0.4869%)"
    },
    {
        "id": 119,
        "code": 4751,
        "name": "サイバーエージェント",
        "type": "サービス",
        "weight": 0.0013,
        "last_price": 82.25,
        "change_v": 31.09,
        "change_r": "(-0.4911%)"
    },
    {
        "id": 120,
        "code": 6103,
        "name": "オークマ",
        "type": "機械",
        "weight": 0.0013,
        "last_price": 81.5,
        "change_v": 31.36,
        "change_r": "(-0.4953%)"
    },
    {
        "id": 121,
        "code": 9101,
        "name": "日本郵船",
        "type": "海運",
        "weight": 0.0013,
        "last_price": 80.75,
        "change_v": 31.63,
        "change_r": "(-0.4995%)"
    },
    {
        "id": 122,
        "code": 4506,
        "name": "住友ファーマ",
        "type": "医薬品",
        "weight": 0.0013,
        "last_price": 80.0,
        "change_v": 31.9,
        "change_r": "(-0.5037%)"
    },
    {
        "id": 123,
        "code": 6361,
        "name": "荏原製作所",
        "type": "機械",
        "weight": 0.0013,
        "last_price": 79.25,
        "change_v": 32.17,
        "change_r": "(-0.5079%)"
    },
    {
        "id": 124,
        "code": 9008,
        "name": "京王電鉄",
        "type": "鉄道・バス",
        "weight": 0.0013,
        "last_price": 78.5,
        "change_v": 32.44,
        "change_r": "(-0.5121%)"
    },
    {
        "id": 125,
        "code": 6473,
        "name": "ジェイテクト",
        "type": "機械",
        "weight": 0.0012,
        "last_price": 77.75,
        "change_v": 32.71,
        "change_r": "(-0.5163%)"
    },
    {
        "id": 126,
        "code": 8804,
        "name": "東京建物",
        "type": "不動産",
        "weight": 0.0012,
        "last_price": 77.0,
        "change_v": 32.98,
        "change_r": "(-0.5205%)"
    },
    {
        "id": 127,
        "code": 9107,
        "name": "川崎汽船",
        "type": "海運",
        "weight": 0.0012,
        "last_price": 76.25,
        "change_v": 33.25,
        "change_r": "(-0.5247%)"
    },
    {
        "id": 128,
        "code": 1802,
        "name": "大林組",
        "type": "建設",
        "weight": 0.0012,
        "last_price": 75.5,
        "change_v": 33.52,
        "change_r": "(-0.5289%)"
    },
    {
        "id": 129,
        "code": 5101,
        "name": "横浜ゴム",
        "type": "ゴム",
        "weight": 0.0012,
        "last_price": 74.75,
        "change_v": 33.79,
        "change_r": "(-0.5331%)"
    },
    {
        "id": 130,
        "code": 5201,
        "name": "ＡＧＣ",
        "type": "窯業",
        "weight": 0.0012,
        "last_price": 74.0,
        "change_v": 34.06,
        "change_r": "(-0.5373%)"
    },
    {
        "id": 131,
        "code": 5714,
        "name": "ＤＯＷＡホールディングス",
        "type": "非鉄・金属",
        "weight": 0.0012,
        "last_price": 73.25,
        "change_v": 34.33,
        "change_r": "(-0.5415%)"
    },
    {
        "id": 132,
        "code": 6178,
        "name": "日本郵政",
        "type": "サービス",
        "weight": 0.0012,
        "last_price": 72.5,
        "change_v": 34.6,
        "change_r": "(-0.5457%)"
    },
    {
        "id": 133,
        "code": 9007,
        "name": "小田急電鉄",
        "type": "鉄道・バス",
        "weight": 0.0012,
        "last_price": 71.75,
        "change_v": 34.87,
        "change_r": "(-0.5499%)"
    },
    {
        "id": 134,
        "code": 4042,
        "name": "東ソー",
        "type": "化学",
        "weight": 0.0011,
        "last_price": 71.0,
        "change_v": 35.14,
        "change_r": "(-0.5541%)"
    },
    {
        "id": 135,
        "code": 1801,
        "name": "大成建設",
        "type": "建設",
        "weight": 0.0011,
        "last_price": 70.25,
        "change_v": 35.41,
        "change_r": "(-0.5583%)"
    },
    {
        "id": 136,
        "code": 9005,
        "name": "東急",
        "type": "鉄道・バス",
        "weight": 0.001,
        "last_price": 69.5,
        "change_v": 35.68,
        "change_r": "(-0.5625%)"
    },
    {
        "id": 137,
        "code": 8355,
        "name": "静岡銀行",
        "type": "銀行",
        "weight": 0.001,
        "last_price": 68.75,
        "change_v": 35.95,
        "change_r": "(-0.5667%)"
    },
    {
        "id": 138,
        "code": 8628,
        "name": "松井証券",
        "type": "証券",
        "weight": 0.001,
        "last_price": 68.0,
        "change_v": 36.22,
        "change_r": "(-0.5709%)"
    },
    {
        "id": 139,
        "code": 5803,
        "name": "フジクラ",
        "type": "非鉄・金属",
        "weight": 0.001,
        "last_price": 67.25,
        "change_v": 36.49,
        "change_r": "(-0.5751%)"
    },
    {
        "id": 140,
        "code": 5214,
        "name": "日本電気硝子",
        "type": "窯業",
        "weight": 0.001,
        "last_price": 66.5,
        "change_v": 36.76,
        "change_r": "(-0.5793%)"
    },
    {
        "id": 141,
        "code": 9147,
        "name": "ＮＩＰＰＯＮＥＸＰＲＥＳＳホールディングス",
        "type": "陸運",
        "weight": 0.001,
        "last_price": 65.75,
        "change_v": 37.03,
        "change_r": "(-0.5835%)"
    },
    {
        "id": 142,
        "code": 1812,
        "name": "鹿島建設",
        "type": "建設",
        "weight": 0.001,
        "last_price": 65.0,
        "change_v": 37.3,
        "change_r": "(-0.5877%)"
    },
    {
        "id": 143,
        "code": 1803,
        "name": "清水建設",
        "type": "建設",
        "weight": 0.001,
        "last_price": 64.25,
        "change_v": 37.57,
        "change_r": "(-0.5919%)"
    },
    {
        "id": 144,
        "code": 8306,
        "name": "三菱ＵＦＪフィナンシャル・グループ",
        "type": "銀行",
        "weight": 0.0009,
        "last_price": 63.5,
        "change_v": 37.84,
        "change_r": "(-0.5961%)"
    },
    {
        "id": 145,
        "code": 6471,
        "name": "日本精工",
        "type": "機械",
        "weight": 0.0009,
        "last_price": 62.75,
        "change_v": 38.11,
        "change_r": "(-0.6003%)"
    },
    {
        "id": 146,
        "code": 8331,
        "name": "千葉銀行",
        "type": "銀行",
        "weight": 0.0009,
        "last_price": 62.0,
        "change_v": 38.38,
        "change_r": "(-0.6045%)"
    },
    {
        "id": 147,
        "code": 3402,
        "name": "東レ",
        "type": "繊維",
        "weight": 0.0009,
        "last_price": 61.25,
        "change_v": 38.65,
        "change_r": "(-0.6087%)"
    },
    {
        "id": 148,
        "code": 7202,
        "name": "いすゞ自動車",
        "type": "自動車",
        "weight": 0.0009,
        "last_price": 60.5,
        "change_v": 38.92,
        "change_r": "(-0.6129%)"
    },
    {
        "id": 149,
        "code": 3289,
        "name": "東急不動産ホールディングス",
        "type": "不動産",
        "weight": 0.0009,
        "last_price": 59.75,
        "change_v": 39.19,
        "change_r": "(-0.6171%)"
    },
    {
        "id": 150,
        "code": 8233,
        "name": "高島屋",
        "type": "小売業",
        "weight": 0.0009,
        "last_price": 59.0,
        "change_v": 39.46,
        "change_r": "(-0.6213%)"
    },
    {
        "id": 151,
        "code": 9020,
        "name": "東日本旅客鉄道",
        "type": "鉄道・バス",
        "weight": 0.0009,
        "last_price": 58.25,
        "change_v": 39.73,
        "change_r": "(-0.6255%)"
    },
    {
        "id": 152,
        "code": 4061,
        "name": "デンカ",
        "type": "化学",
        "weight": 0.0009,
        "last_price": 57.5,
        "change_v": 40.0,
        "change_r": "(-0.6297%)"
    },
    {
        "id": 153,
        "code": 7205,
        "name": "日野自動車",
        "type": "自動車",
        "weight": 0.0009,
        "last_price": 56.75,
        "change_v": 40.27,
        "change_r": "(-0.6339%)"
    },
    {
        "id": 154,
        "code": 4755,
        "name": "楽天グループ",
        "type": "サービス",
        "weight": 0.0008,
        "last_price": 56.0,
        "change_v": 40.54,
        "change_r": "(-0.6381%)"
    },
    {
        "id": 155,
        "code": 9001,
        "name": "東武鉄道",
        "type": "鉄道・バス",
        "weight": 0.0008,
        "last_price": 55.25,
        "change_v": 40.81,
        "change_r": "(-0.6423%)"
    },
    {
        "id": 156,
        "code": 5631,
        "name": "日本製鋼所",
        "type": "機械",
        "weight": 0.0008,
        "last_price": 54.5,
        "change_v": 41.08,
        "change_r": "(-0.6465%)"
    },
    {
        "id": 157,
        "code": 8601,
        "name": "大和証券グループ本社",
        "type": "証券",
        "weight": 0.0008,
        "last_price": 53.75,
        "change_v": 41.35,
        "change_r": "(-0.6507%)"
    },
    {
        "id": 158,
        "code": 6302,
        "name": "住友重機械工業",
        "type": "機械",
        "weight": 0.0008,
        "last_price": 53.0,
        "change_v": 41.62,
        "change_r": "(-0.6549%)"
    },
    {
        "id": 159,
        "code": 1605,
        "name": "ＩＮＰＥＸ",
        "type": "鉱業",
        "weight": 0.0008,
        "last_price": 52.25,
        "change_v": 41.89,
        "change_r": "(-0.6591%)"
    },
    {
        "id": 160,
        "code": 1332,
        "name": "日本水産",
        "type": "水産",
        "weight": 0.0008,
        "last_price": 51.5,
        "change_v": 42.16,
        "change_r": "(-0.6633%)"
    },
    {
        "id": 161,
        "code": 2501,
        "name": "サッポロホールディングス",
        "type": "食品",
        "weight": 0.0008,
        "last_price": 50.75,
        "change_v": 42.43,
        "change_r": "(-0.6675%)"
    },
    {
        "id": 162,
        "code": 2432,
        "name": "ディー・エヌ・エー",
        "type": "サービス",
        "weight": 0.0007,
        "last_price": 50.0,
        "change_v": 42.7,
        "change_r": "(-0.6717%)"
    },
    {
        "id": 163,
        "code": 7762,
        "name": "シチズン時計",
        "type": "精密機器",
        "weight": 0.0007,
        "last_price": 49.25,
        "change_v": 42.97,
        "change_r": "(-0.6759%)"
    },
    {
        "id": 164,
        "code": 3086,
        "name": "Ｊ．フロントリテイリング",
        "type": "小売業",
        "weight": 0.0007,
        "last_price": 48.5,
        "change_v": 43.24,
        "change_r": "(-0.6801%)"
    },
    {
        "id": 165,
        "code": 4183,
        "name": "三井化学",
        "type": "化学",
        "weight": 0.0007,
        "last_price": 47.75,
        "change_v": 43.51,
        "change_r": "(-0.6843%)"
    },
    {
        "id": 166,
        "code": 3861,
        "name": "王子ホールディングス",
        "type": "パルプ・紙",
        "weight": 0.0007,
        "last_price": 47.0,
        "change_v": 43.78,
        "change_r": "(-0.6885%)"
    },
    {
        "id": 167,
        "code": 9602,
        "name": "東宝",
        "type": "サービス",
        "weight": 0.0007,
        "last_price": 46.25,
        "change_v": 44.05,
        "change_r": "(-0.6927%)"
    },
    {
        "id": 168,
        "code": 4005,
        "name": "住友化学",
        "type": "化学",
        "weight": 0.0007,
        "last_price": 45.5,
        "change_v": 44.32,
        "change_r": "(-0.6969%)"
    },
    {
        "id": 169,
        "code": 9531,
        "name": "東京瓦斯",
        "type": "ガス",
        "weight": 0.0007,
        "last_price": 44.75,
        "change_v": 44.59,
        "change_r": "(-0.7011%)"
    },
    {
        "id": 170,
        "code": 5020,
        "name": "ＥＮＥＯＳホールディングス",
        "type": "石油",
        "weight": 0.0006,
        "last_price": 44.0,
        "change_v": 44.86,
        "change_r": "(-0.7053%)"
    },
    {
        "id": 171,
        "code": 8604,
        "name": "野村ホールディングス",
        "type": "証券",
        "weight": 0.0006,
        "last_price": 43.25,
        "change_v": 45.13,
        "change_r": "(-0.7095%)"
    },
    {
        "id": 172,
        "code": 7201,
        "name": "日産自動車",
        "type": "自動車",
        "weight": 0.0006,
        "last_price": 42.5,
        "change_v": 45.4,
        "change_r": "(-0.7137%)"
    },
    {
        "id": 173,
        "code": 7011,
        "name": "三菱重工業",
        "type": "機械",
        "weight": 0.0006,
        "last_price": 41.75,
        "change_v": 45.67,
        "change_r": "(-0.7179%)"
    },
    {
        "id": 174,
        "code": 6701,
        "name": "日本電気",
        "type": "電気機器",
        "weight": 0.0006,
        "last_price": 41.0,
        "change_v": 45.94,
        "change_r": "(-0.7221%)"
    },
    {
        "id": 175,
        "code": 9021,
        "name": "西日本旅客鉄道",
        "type": "鉄道・バス",
        "weight": 0.0006,
        "last_price": 40.25,
        "change_v": 46.21,
        "change_r": "(-0.7263%)"
    },
    {
        "id": 176,
        "code": 6674,
        "name": "ジーエス・ユアサコーポレーション",
        "type": "電気機器",
        "weight": 0.0006,
        "last_price": 39.5,
        "change_v": 46.48,
        "change_r": "(-0.7305%)"
    },
    {
        "id": 177,
        "code": 9532,
        "name": "大阪瓦斯",
        "type": "ガス",
        "weight": 0.0006,
        "last_price": 38.75,
        "change_v": 46.75,
        "change_r": "(-0.7347%)"
    },
    {
        "id": 178,
        "code": 4902,
        "name": "コニカミノルタ",
        "type": "精密機器",
        "weight": 0.0006,
        "last_price": 38.0,
        "change_v": 47.02,
        "change_r": "(-0.7389%)"
    },
    {
        "id": 179,
        "code": 8354,
        "name": "ふくおかフィナンシャルグループ",
        "type": "銀行",
        "weight": 0.0006,
        "last_price": 37.25,
        "change_v": 47.29,
        "change_r": "(-0.7431%)"
    },
    {
        "id": 180,
        "code": 7186,
        "name": "コンコルディア・フィナンシャルグループ",
        "type": "銀行",
        "weight": 0.0006,
        "last_price": 36.5,
        "change_v": 47.56,
        "change_r": "(-0.7473%)"
    },
    {
        "id": 181,
        "code": 8309,
        "name": "三井住友トラスト・ホールディングス",
        "type": "銀行",
        "weight": 0.0006,
        "last_price": 35.75,
        "change_v": 47.83,
        "change_r": "(-0.7515%)"
    },
    {
        "id": 182,
        "code": 8316,
        "name": "三井住友フィナンシャルグループ",
        "type": "銀行",
        "weight": 0.0005,
        "last_price": 35.0,
        "change_v": 48.1,
        "change_r": "(-0.7557%)"
    },
    {
        "id": 183,
        "code": 4188,
        "name": "三菱ケミカルグループ",
        "type": "化学",
        "weight": 0.0005,
        "last_price": 34.25,
        "change_v": 48.37,
        "change_r": "(-0.7599%)"
    },
    {
        "id": 184,
        "code": 4043,
        "name": "トクヤマ",
        "type": "化学",
        "weight": 0.0005,
        "last_price": 33.5,
        "change_v": 48.64,
        "change_r": "(-0.7641%)"
    },
    {
        "id": 185,
        "code": 5232,
        "name": "住友大阪セメント",
        "type": "窯業",
        "weight": 0.0004,
        "last_price": 32.75,
        "change_v": 48.91,
        "change_r": "(-0.7683%)"
    },
    {
        "id": 186,
        "code": 7013,
        "name": "ＩＨＩ",
        "type": "機械",
        "weight": 0.0004,
        "last_price": 32.0,
        "change_v": 49.18,
        "change_r": "(-0.7725%)"
    },
    {
        "id": 187,
        "code": 1808,
        "name": "長谷工コーポレーション",
        "type": "建設",
        "weight": 0.0004,
        "last_price": 31.25,
        "change_v": 49.45,
        "change_r": "(-0.7767%)"
    },
    {
        "id": 188,
        "code": 5706,
        "name": "三井金属鉱業",
        "type": "非鉄・金属",
        "weight": 0.0004,
        "last_price": 30.5,
        "change_v": 49.72,
        "change_r": "(-0.7809%)"
    },
    {
        "id": 189,
        "code": 8795,
        "name": "Ｔ＆Ｄホールディングス",
        "type": "保険",
        "weight": 0.0004,
        "last_price": 29.75,
        "change_v": 49.99,
        "change_r": "(-0.7851%)"
    },
    {
        "id": 190,
        "code": 3401,
        "name": "帝人",
        "type": "繊維",
        "weight": 0.0004,
        "last_price": 29.0,
        "change_v": 50.26,
        "change_r": "(-0.7893%)"
    },
    {
        "id": 191,
        "code": 8304,
        "name": "あおぞら銀行",
        "type": "銀行",
        "weight": 0.0004,
        "last_price": 28.25,
        "change_v": 50.53,
        "change_r": "(-0.7935%)"
    },
    {
        "id": 192,
        "code": 7012,
        "name": "川崎重工業",
        "type": "造船",
        "weight": 0.0003,
        "last_price": 27.5,
        "change_v": 50.8,
        "change_r": "(-0.7977%)"
    },
    {
        "id": 193,
        "code": 1333,
        "name": "マルハニチロ",
        "type": "水産",
        "weight": 0.0003,
        "last_price": 26.75,
        "change_v": 51.07,
        "change_r": "(-0.8019%)"
    },
    {
        "id": 194,
        "code": 5541,
        "name": "大平洋金属",
        "type": "鉄鋼",
        "weight": 0.0003,
        "last_price": 26.0,
        "change_v": 51.34,
        "change_r": "(-0.8061%)"
    },
    {
        "id": 195,
        "code": 9202,
        "name": "ＡＮＡホールディングス",
        "type": "空運",
        "weight": 0.0003,
        "last_price": 25.25,
        "change_v": 51.61,
        "change_r": "(-0.8103%)"
    },
    {
        "id": 196,
        "code": 4631,
        "name": "ＤＩＣ",
        "type": "化学",
        "weight": 0.0003,
        "last_price": 24.5,
        "change_v": 51.88,
        "change_r": "(-0.8145%)"
    },
    {
        "id": 197,
        "code": 6472,
        "name": "ＮＴＮ",
        "type": "機械",
        "weight": 0.0003,
        "last_price": 23.75,
        "change_v": 52.15,
        "change_r": "(-0.8187%)"
    },
    {
        "id": 198,
        "code": 5801,
        "name": "古河電気工業",
        "type": "非鉄・金属",
        "weight": 0.0003,
        "last_price": 23.0,
        "change_v": 52.42,
        "change_r": "(-0.8229%)"
    },
    {
        "id": 199,
        "code": 8750,
        "name": "第一生命ホールディングス",
        "type": "保険",
        "weight": 0.0003,
        "last_price": 22.25,
        "change_v": 52.69,
        "change_r": "(-0.8271%)"
    },
    {
        "id": 200,
        "code": 7261,
        "name": "マツダ",
        "type": "自動車",
        "weight": 0.0003,
        "last_price": 21.5,
        "change_v": 52.96,
        "change_r": "(-0.8313%)"
    },
    {
        "id": 201,
        "code": 4004,
        "name": "昭和電工",
        "type": "化学",
        "weight": 0.0003,
        "last_price": 20.75,
        "change_v": 53.23,
        "change_r": "(-0.8355%)"
    },
    {
        "id": 202,
        "code": 5707,
        "name": "東邦亜鉛",
        "type": "非鉄・金属",
        "weight": 0.0003,
        "last_price": 20.0,
        "change_v": 53.5,
        "change_r": "(-0.8397%)"
    },
    {
        "id": 203,
        "code": 4208,
        "name": "ＵＢＥ",
        "type": "化学",
        "weight": 0.0003,
        "last_price": 19.25,
        "change_v": 53.77,
        "change_r": "(-0.8439%)"
    },
    {
        "id": 204,
        "code": 2768,
        "name": "双日",
        "type": "商社",
        "weight": 0.0003,
        "last_price": 18.5,
        "change_v": 54.04,
        "change_r": "(-0.8481%)"
    },
    {
        "id": 205,
        "code": 5711,
        "name": "三菱マテリアル",
        "type": "非鉄・金属",
        "weight": 0.0003,
        "last_price": 17.75,
        "change_v": 54.31,
        "change_r": "(-0.8523%)"
    },
    {
        "id": 206,
        "code": 5233,
        "name": "太平洋セメント",
        "type": "窯業",
        "weight": 0.0003,
        "last_price": 17.0,
        "change_v": 54.58,
        "change_r": "(-0.8565%)"
    },
    {
        "id": 207,
        "code": 5401,
        "name": "日本製鉄",
        "type": "鉄鋼",
        "weight": 0.0002,
        "last_price": 16.25,
        "change_v": 54.85,
        "change_r": "(-0.8607%)"
    },
    {
        "id": 208,
        "code": 4689,
        "name": "Ｚホールディングス",
        "type": "サービス",
        "weight": 0.0002,
        "last_price": 15.5,
        "change_v": 55.12,
        "change_r": "(-0.8649%)"
    },
    {
        "id": 209,
        "code": 3436,
        "name": "ＳＵＭＣＯ",
        "type": "非鉄・金属",
        "weight": 0.0002,
        "last_price": 14.75,
        "change_v": 55.39,
        "change_r": "(-0.8691%)"
    },
    {
        "id": 210,
        "code": 7004,
        "name": "日立造船",
        "type": "機械",
        "weight": 0.0002,
        "last_price": 14.0,
        "change_v": 55.66,
        "change_r": "(-0.8733%)"
    },
    {
        "id": 211,
        "code": 5703,
        "name": "日本軽金属ホールディングス",
        "type": "非鉄・金属",
        "weight": 0.0002,
        "last_price": 13.25,
        "change_v": 55.93,
        "change_r": "(-0.8775%)"
    },
    {
        "id": 212,
        "code": 8411,
        "name": "みずほフィナンシャルグループ",
        "type": "銀行",
        "weight": 0.0002,
        "last_price": 12.5,
        "change_v": 56.2,
        "change_r": "(-0.8817%)"
    },
    {
        "id": 213,
        "code": 5411,
        "name": "ＪＦＥホールディングス",
        "type": "鉄鋼",
        "weight": 0.0002,
        "last_price": 11.75,
        "change_v": 56.47,
        "change_r": "(-0.8859%)"
    },
    {
        "id": 214,
        "code": 9502,
        "name": "中部電力",
        "type": "電力",
        "weight": 0.0002,
        "last_price": 11.0,
        "change_v": 56.74,
        "change_r": "(-0.8901%)"
    },
    {
        "id": 215,
        "code": 9503,
        "name": "関西電力",
        "type": "電力",
        "weight": 0.0002,
        "last_price": 10.25,
        "change_v": 57.01,
        "change_r": "(-0.8943%)"
    },
    {
        "id": 216,
        "code": 3101,
        "name": "東洋紡",
        "type": "繊維",
        "weight": 0.0001,
        "last_price": 9.5,
        "change_v": 57.28,
        "change_r": "(-0.8985%)"
    },
    {
        "id": 217,
        "code": 3863,
        "name": "日本製紙",
        "type": "パルプ・紙",
        "weight": 0.0001,
        "last_price": 8.75,
        "change_v": 57.55,
        "change_r": "(-0.9027%)"
    },
    {
        "id": 218,
        "code": 6703,
        "name": "沖電気工業",
        "type": "電気機器",
        "weight": 0.0001,
        "last_price": 8.0,
        "change_v": 57.82,
        "change_r": "(-0.9069%)"
    },
    {
        "id": 219,
        "code": 5406,
        "name": "神戸製鋼所",
        "type": "鉄鋼",
        "weight": 0.0001,
        "last_price": 7.25,
        "change_v": 58.09,
        "change_r": "(-0.9111%)"
    },
    {
        "id": 220,
        "code": 9501,
        "name": "東京電力ホールディングス",
        "type": "電力",
        "weight": 0.0001,
        "last_price": 6.5,
        "change_v": 58.36,
        "change_r": "(-0.9153%)"
    },
    {
        "id": 221,
        "code": 8308,
        "name": "りそなホールディングス",
        "type": "銀行",
        "weight": 0.0001,
        "last_price": 5.75,
        "change_v": 58.63,
        "change_r": "(-0.9195%)"
    },
    {
        "id": 222,
        "code": 7211,
        "name": "三菱自動車工業",
        "type": "自動車",
        "weight": 0.0001,
        "last_price": 5.0,
        "change_v": 58.9,
        "change_r": "(-0.9237%)"
    },
    {
        "id": 223,
        "code": 5202,
        "name": "日本板硝子",
        "type": "窯業",
        "weight": 0.0,
        "last_price": 4.25,
        "change_v": 59.17,
        "change_r": "(-0.9279%)"
    },
    {
        "id": 224,
        "code": 7003,
        "name": "三井Ｅ＆Ｓホールディングス",
        "type": "造船",
        "weight": 0.0,
        "last_price": 3.5,
        "change_v": 59.44,
        "change_r": "(-0.9321%)"
    },
    {
        "id": 225,
        "code": 3103,
        "name": "ユニチカ",
        "type": "繊維",
        "weight": 0.0,
        "last_price": 2.75,
        "change_v": 59.71,
        "change_r": "(-0.9363%)"
    }
]

    response = make_response(jsonify(data))
    # response.headers["Content-Type"] = "application/json;charset=UTF-8"

    return response


@app.route('/')
def get_list1():
    return render_template("index.html")

@app.route('/d')
def get_list12():
    return render_template("dd.html")


if __name__ == '__main__':
    app.run(debug=True)