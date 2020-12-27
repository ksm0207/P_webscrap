from flask import Flask
from flask import render_template  # html파일을 메인으로 보내기
from flask import request
from flask import redirect
from flask import send_file
from scrapper import stack_get_jobs
from exporter import save_to_file

app = Flask(__name__)

db = {}  # 가짜 DB를 만들었고 현재는 비어있음


@app.route("/")  # / 으로 접속했을떄 home 이라는 함수를 실행함
def home():
    return render_template(template_name_or_list="index.html")


@app.route("/report")
def report():
    location = request.args.get(  # index.html --> input 입력시 name argument을 가져옴
        "location"  # 사용자가 어떤 검색어를 입력하는지 알수있게된다
    )
    if location:  # location 값은 존재할때 실행
        location = location.lower()
        from_db = db.get(location)  # location 값을 db에 있는지 찾아줌
        if from_db:  # 만약 from_db 값이 존재 하면 get_ready는 from_db 가 되지만 값이없으면 None 이므로 실행 X
            get_ready = from_db
        else:  # Step 1 stack_get_jobs URL로부터 location을 받는다
            get_ready = stack_get_jobs(location)  # location 값이 None 이면 찾기위한 크롤링 시작
            db[location] = get_ready  # 크롤링 종료후 데이터 저장
    else:
        return redirect("/")  # /report 으로만 접속시 홈 으로 리다이렉트

    # search_by : 템플릿에 데이터를 넘길때 사용하는 변수 , 이를 렌더링 작업이라고 부름
    return render_template(
        template_name_or_list="report.html",
        search_by=location,
        results_number=len(get_ready),
        jobs=get_ready,
    )


# URL 에서 넘어온 단어를 보내기 및 체크
@app.route("/export")
def export():
    try:
        location = request.args.get("location")
        if not location:  # location 에 해당하는 jobs 값이 존재하지 않으면 raise 발생
            print("값이 제대로 전달되지 않았습니다")
            raise Exception()
        location = location.lower()
        jobs = db.get(location)  # location 으로 jobs를 Fake DB에서 찾음
        if not jobs:  # jobs 가 존재하지 않으면 예외발생
            print("Do not exist DB")
            raise Exception()
        save_to_file(jobs)  # 존재하면 csv 파일 저장
        return send_file("jobs.csv", as_attachment=True)
    except Exception as e:
        print(e)
        return redirect("/")  # 값이 None일때 리다이렉트


# Python은 @를 찾아 어떤 접속요청이 들어오면 실행
# @ : 데코레이터 라고 부르며 아래에 있는 함수를 찾아 실행함
# @app.route("/<username>")  # /about 접속시 함수 실행 <> 부분은 placeholder
# def about_me(username):  # Flask : about_me 함수를 username 인자와 함께 호출하므로 route와 같게 작성함
# return f"Hello {username} how are you doing ?  "  # /'입력한값' 으로 리턴해준다


if __name__ == "__main__":
    app.run(debug=True)
else:
    print(__name__)
