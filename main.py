import requests
from bs4 import BeautifulSoup

# indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")
indeed_result = requests.get(
    "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%EA%B0%9C%EB%B0%9C%EC%9E%90&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all("a")
spans = []

for page in pages:
    spans.append(page.find("span"))

spans = spans[:-1]
