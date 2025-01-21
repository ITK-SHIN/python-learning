from requests import get

""" 
tuple 에 있는 웹사이트가 동작중인지 내려갔는지 확인하는 작업 
"""

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
    "https://httpstat.us/502",
    "https://httpstat.us/404",
    "https://httpstat.us/300",
    "https://httpstat.us/200",
    "https://httpstat.us/101",
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 200 and response.status_code < 300:
        results[website] = "OK"
    elif response.status_code >= 300 and response.status_code < 400:
        results[website] = "REDIRECT"
    elif response.status_code >= 400 and response.status_code < 500:
        results[website] = "CLIENT ERROR"
    else:
        results[website] = "SERVER ERROR"

print(results)
