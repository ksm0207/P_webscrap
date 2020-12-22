from flask import Flask
from flask import render_template  # html파일을 메인으로 보내기
from flask import request


app = Flask("SuperScrapper")  # 앱 이름 설정 / 는 root(웹사이트)를 의미함 google.com/ 구글루트 접속


@app.route("/")  # / 으로 접속했을떄 home 이라는 함수를 실행함
def home():
    return render_template(template_name_or_list="index.html")


@app.route("/report")
def report():
    location = request.args.get(  # index.html --> input 입력시 name argument을 가져옴
        "location"  # 사용자가 어떤 검색어를 입력하는지 알수있게된다
    )
    if location:
        if location is not None:
            print("검색 결과 : True")
        else:
            print("검색 결과 : False")
    # search_by : 템플릿에 데이터를 넘길때 사용하는 변수 , 이를 렌더링 작업이라고 부름
    return render_template(template_name_or_list="report.html", search_by=location)


app.run(debug=True)

# Python은 @를 찾아 어떤 접속요청이 들어오면 실행
# @ : 데코레이터 라고 부르며 아래에 있는 함수를 찾아 실행함
# @app.route("/<username>")  # /about 접속시 함수 실행 <> 부분은 placeholder
# def about_me(username):  # Flask : about_me 함수를 username 인자와 함께 호출하므로 route와 같게 작성함
# return f"Hello {username} how are you doing ?  "  # /'입력한값' 으로 리턴해준다

