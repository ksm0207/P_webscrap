import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import


LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    # indeed html을 가져옵니다
    indeed = requests.get(URL)

    # 데이터를 추출할 변수를 만들어 줍니다
    indeed_soup = BeautifulSoup(indeed.text, "html.parser")

    # div 요소에 class 명이 pagination 으로 작성 된 것을 찾습니다
    pagination = indeed_soup.find("div", {"class": "pagination"})

    # find_all() 으로 모든 <a> 요소를 찾은다음 리스트[]로 반환합니다
    links = pagination.find_all("a")

    pages = []
    # for 반복문 시작
    for link in links[:-3]:
        pages.append(int(link.string))

    # 페이지에서 가장 큰 숫자를 나타냅니다
    max_page = pages[-1]

    # 페이지에서 가장 큰 숫자를 반환합니다
    return max_page


def extract_job(html):  # html = extract_indeed_jobs() result 인자를 받고 정보를 추출합니다
    # html 인자를 받고 extract_indeed_jobs 의 request 한 결과를 출력합니다 
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})     # 회사이름 가져오기
    company_anchor = company.find("a")  # Company 에서 soup 으로 부터 찾은 결과 저장
    # 회사 이름에 <a> 없는곳이 있는지 체크해주기
    if company_anchor is not None:
        # 회사에 링크가 있다면 <a> String 출력
        company = str(company_anchor.string)  # strip() 공백제거
    else:
        # 링크가 없으면 아래 것 을 출력
        company = str(company.string)
    company = company.strip()
    
    # 장소 가져오기
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]  # [data-rc-loc] 은 div 안에 있는 attribute 에 접근합니다
    # 페이지 지원링크 (id 값) 가져오기
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?jk{job_id}"}


def extract_indeed_jobs(last_pages):
    jobs = []   # extract_job() 함수로 부터 반환된 값을 배열에 넣습니다
    for page in range(last_pages):  # last_page = 18
        print(f"스크랩핑 페이지 수 : {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            # extract_job() 함수 호출 후 결과를 출력합니다
            job = extract_job(result)
            # extract_job -->  company or title 결과를 배열로 저장합니다
            jobs.append(job)
    return jobs

