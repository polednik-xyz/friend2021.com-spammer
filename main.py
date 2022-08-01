
import requests
url = "https://api.truefalse.site/d20/addentry"

data = {
"key": "1",
"name": "", ## username
"quizid": "", ##quiz id in url
"score": "20", ## quiz score cannot go above 20
}
while True:
    r = requests.post(url, data=data).text
    print("sent! if no response then patched or bad quizid")
    print(r)

