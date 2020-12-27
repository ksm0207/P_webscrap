import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import


# 스크래핑 할때 필수사항 3가지
# 1. 페이지를 가져올것
# 2. Request를 만들것
# 3. 출력할것을 추출하기

LIMIT = 50


# URL에 Request 보내기
def get_last_page(url):  # location 인자로부터 결과를 찾는다
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)  # 마지막 페이지 숫자 가져오기 (next 제거)
    # extract_jobs 의 인자는 정수형이고 range()는 Integer를 사용하므로
    # 형변환 시켜야함 현재는 string을 반환중
    return int(last_page)


# 일자리 가져오기
def extract_job(html):  # html 인자는 result 를 받음
    title = html.find("div", {"class": "grid--cell fl1"}).find("h2").find("a")["title"]
    company, location = html.find(
        "h3", {"class": "fc-black-700 fs-body1 mb4"}
    ).find_all(
        "span", recursive=False
    )  # recursive = 전부 가져오는것을 방지함
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-")
    # job id 가져오기 (URL)
    job_id = html["data-jobid"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}",
    }


# job 출력하기 indeed.py extract_indeed_jobs() 참고
def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"SOF : 스크랩핑 페이지 수 : {page}")
        result = requests.get(f"{url}&pg={page +1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def stack_get_jobs(location):  # Step 1 location 인자를 get_last_page()로 보내진다,
    url = f"https://stackoverflow.com/jobs?q={location}&sort=i"  # location : URL에서 넘어온 어떤거든 될수있음
    last_page = get_last_page(url)  # 웹사이트 URL에서 오고있는것.
    jobs = extract_jobs(last_page, url)
    return jobs


##############################################################################


def i_get_last_page(url):
    # indeed html을 가져옵니다
    indeed = requests.get(url)

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


def i_extract_job(html):  # html = extract_indeed_jobs() result 인자를 받고 정보를 추출합니다
    # html 인자를 받고 extract_indeed_jobs 의 request 한 결과를 출력합니다
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})  # 회사이름 가져오기
    company_anchor = company.find("a")  # Company 에서 soup 으로 부터 찾은 결과 저장

    # 회사 이름에 <a> 없는곳이 있는지 체크해주기

    if company:  # company attribute를 찾을수 없을때 찾아주는 조건문 추가
        company_anchor = company.find("a")  # 결과가 저장되지 않으면 실행되지 않음
        if company_anchor is not None:
            # 회사에 링크가 있다면 <a> String 출력
            company = str(company_anchor.string)  # strip() 공백제거
        else:
            # 링크가 없으면 아래 것 을 출력
            company = str(company.string)
        company = company.strip()
    else:
        company = None

    # 장소 가져오기
    location = html.find("div", {"class": "recJobLoc"})[
        "data-rc-loc"
    ]  # [data-rc-loc] 은 div 안에 있는 attribute 에 접근합니다
    # 페이지 지원링크 (id 값) 가져오기
    job_id = html["data-jk"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://www.indeed.com/viewjob?jk{job_id}",
    }


def extract_indeed_jobs(last_pages, i_url):
    jobs = []  # extract_job() 함수로 부터 반환된 값을 배열에 넣습니다
    for page in range(last_pages):  # last_page = 18
        print(f"스크랩핑 페이지 수 : {page}")
        result = requests.get(f"{i_url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            # extract_job() 함수 호출 후 결과를 출력합니다
            job = i_extract_job(result)
            # extract_job -->  company or title 결과를 배열로 저장합니다
            jobs.append(job)
    return jobs


# main.py --> indeed.py 합치기
def get_jobs(location):
    i_url = f"https://www.indeed.com/jobs?q={location}&limit={LIMIT}"
    print(i_url)

    # 페이지의 가장 큰 숫자는 18을 나타냅니다
    max_indeed_pages = i_get_last_page(i_url)
    # 페이지의 가장 큰 숫자를 받아 18번동안 작동합니다
    jobs = extract_indeed_jobs(max_indeed_pages, i_url)

    return jobs
