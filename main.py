import requests
from bs4 import BeautifulSoup  # 데이터를 추출하기 위해 import


# indeed html을 가져옵니다
indeed = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# 데이터를 추출할 변수를 만들어 줍니다
indeed_soup = BeautifulSoup(indeed.text, "html.parser")

# div 요소에 class 명이 pagination 으로 작성 된 것을 찾습니다
pagination = indeed_soup.find("div", {"class": "pagination"})


# find_all() 으로 모든 <a> 요소를 찾은다음 리스트[]로 반환합니다
links = pagination.find_all("a")

pages = []
# for 반복문 시작
for link in links[:-1]:
    pages.append(int(link.string))


max_page = pages[-1]

print(max_page)
