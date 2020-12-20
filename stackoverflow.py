import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"  # 페이지 이동할때 sort=i 값을 받으면서 이동함

# 스크래핑 할때 필수사항 3가지
# 1. 페이지를 가져올것
# 2. Request를 만들것
# 3. 출력할것을 추출하기


# request를 만듭니다
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pages)


# 페이지를 가져옵니다 (번호 가져오기)
def stack_get_jobs():
    last_page = get_last_page()
    
    return []


# job 출력하기


