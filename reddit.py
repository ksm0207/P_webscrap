import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}
url = "https://www.reddit.com/r/django/top/?t=month"


def main():
    get_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(get_request.text, "html.parser")
    pages = soup.find("div", {"class": "rpBJOHq2PR60pnwJlUyP0"})
    data = pages

    return data


def get_reddit(html):
    title = html.find("h3")
    point = html.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"})
    go_url = html.find("a")["href"]

    title = title.get_text(strip=True)
    point = point.get_text(strip=True)
    go_url = go_url

    return {"title": title, "point": point, "link": go_url}


def reddit(get):

    scrap = []

    for page in get:
        print("스크래핑 중 ...")
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})
        for result in results:
            suc_data = get_reddit(result)
            scrap.append(suc_data)
    return scrap


def call_reddit():
    page = main()
    get_page = reddit(page)

    return get_page

