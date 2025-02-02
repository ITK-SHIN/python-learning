# 6-0 ~ 6-4강
# <section class”job” id=”category-2></section> 안의 모든 li들 가져오는 코드
import requests
from bs4 import BeautifulSoup

all_jobs = []

# 
def scrape_page(url=''):
    url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser") # 전체 html 가져오기
    jobs = soup.find("section", class_="jobs").find_all("li")[:-1] # html에서 section 내의 li 가져옴

    for job in jobs:
        title = job.find("span", class_="title").text # title 가져옴
        company_spans = job.find_all("span", class_="company") # 회사명

        # 리스트의 인덱스에 안전하게 접근하는 helper function
        def get_text(spans, index, default="Not specified"):
            return spans[index].text.strip() if len(spans) > index else default

        company = get_text(company_spans, 0) # 회사명
        position = get_text(company_spans, 1) # 계약직/풀타임
        region = get_text(company_spans, 2) # 직무 제안 지역

        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        # html에서 태그의 속성 추출하기
        # print(title, "\n", company, "\n", position, "\n", region)
        # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        job_data = {
            "tiile": title,  # 제목
            "company": company,  # 회사명
            "position": position, # 계약직 / 풀타임
            "region": region, # 직무 제안 지역
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)


scrape_page()
print(all_jobs)

#response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")

#soup = BeautifulSoup(response.content, "html.parser")