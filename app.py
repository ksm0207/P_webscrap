from flask import Flask
from flask import render_template  # html파일을 메인으로 보내기

app = Flask("SuperScrapper")  # 앱 이름 설정 / 는 root(웹사이트)를 의미함 google.com/ 구글루트 접속


@app.route("/")  # / 으로 접속했을떄 home 이라는 함수를 실행함
def home():
    return render_template(template_name_or_list="index.html")


app.run(debug=True)

# Python은 @를 찾아 어떤 접속요청이 들어오면 실행
# @ : 데코레이터 라고 부르며 아래에 있는 함수를 찾아 실행함
# @app.route("/<username>")  # /about 접속시 함수 실행 <> 부분은 placeholder
# def about_me(username):  # Flask : about_me 함수를 username 인자와 함께 호출하므로 route와 같게 작성함
# return f"Hello {username} how are you doing ?  "  # /'입력한값' 으로 리턴해준다

