




import requests


res = requests.get("https://jsonplaceholder.typicode.com/todos")
print(res.text)


#  http://127.0.0.1:5000/get_list
# [
#   {
#     "Ctime": "2020-01-21 21:25:44",
#     "Name": "\u5954\u9a70",
#     "id": 1
#   },
#   {
#     "Ctime": "2020-01-20 21:25:44",
#     "Name": "\u5b9d\u9a6c",