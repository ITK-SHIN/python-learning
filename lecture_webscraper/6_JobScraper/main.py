# 2강
# <section class”job” id=”category-2></section> 안의 모든 li들 가져오는 코드
import requests
from bs4 import BeautifulSoup

all_jobs = []

# 
def scrape_page(url):
    url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        company_spans = job.find_all("span", class_="company")

        # 리스트의 인덱스에 안전하게 접근하는 helper function
        def get_text(spans, index, default="Not specified"):
            return spans[index].text.strip() if len(spans) > index else default

        company = get_text(company_spans, 0)
        position = get_text(company_spans, 1)
        region = get_text(company_spans, 2)

        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        # html에서 태그의 속성 추출하기
        # print(title, "\n", company, "\n", position, "\n", region)
        # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        job_data = {
            "tiile": title,
            "company": company,
            "position": position,
            "region": region,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)


print(all_jobs)
