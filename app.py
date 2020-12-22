from flask import Flask

app = Flask("SuperScrapper")  # 앱 이름 설정 / 는 root(웹사이트)를 의미함 google.com/ 구글루트 접속


@app.route("/")  # / 으로 접속했을떄 home 이라는 함수를 실행함
def home():
    return "Hello"


# Python은 @를 찾아 어떤 접속요청이 들어오면 실행
# @ : 데코레이터 라고 부르며 아래에 있는 함수를 찾아 실행함
@app.route("/about")  # /about 접속시 함수 실행
def about_me():
    return "About"


app.run()
