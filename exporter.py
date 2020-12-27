import csv


def save_to_file(jobs):

    file = open("jobs.csv", mode="w", encoding="UTF-8")  # 파일 오픈
    # open() 함수를 사용할때 mode는 반드시 설정해줘야함
    # mode는  파일을 읽기형식 혹은 쓰기로 열수도있지만 w로 설정하면 쓰기로 설정한것

    # title , company , location , link 엑셀에 넣기작업 1
    writer = csv.writer(file)  # writer : 어떤 파일에 쓰기를 할건지 지정할것
    writer.writerow(["title", "company", "location", "link"])  # Csv 리스트 형식 추가
    for job in jobs:
        # jobs에 있는 각 job을 가지고 row에 작성후 job이 가진 값의 리스트를 row로 가져오기
        writer.writerow(list(job.values()))
    return
