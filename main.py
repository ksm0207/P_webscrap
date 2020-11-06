import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import

spans = []


# indeed html을 가져옵니다
indeed = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# 데이터를 추출할 변수를 만들어 줍니다
indeed_soup = BeautifulSoup(indeed.text, "html.parser")

# div 요소에 class 명이 pagination 으로 작성 된 것을 찾습니다
pagination = indeed_soup.find("div", {"class": "pagination"})


# find_all() 으로 모든 <a> 요소를 찾은다음 리스트[]로 반환합니다
pages = pagination.find_all("a")


# for 반복문 시작
for page in pages:
    spans.append(page.find("span"))


span = spans[0:-1]
print(span)
