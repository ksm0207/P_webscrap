import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import


# 스크래핑 할때 필수사항 3가지
# 1. 페이지를 가져올것
# 2. Request를 만들것
# 3. 출력할것을 추출하기

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

