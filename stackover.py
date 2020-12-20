import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


# request를 만듭니다
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pagination)


# 페이지를 가져옵니다 (번호 가져오기)
def stack_get_jobs():
    last_page = get_last_page()
    return []


# job 출력하기

