from bs4 import BeautifulSoup
import requests

def crawling(url):
    response = requests.get(url)
    state = response.status_code
    data = []

    if state == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all(class_='se-fs-fs16 se-ff-system')
    else:
        print(f"state code: {state}")

    return data

def txtFile(contents):
    writer = open("/home/pjh/test/news.txt", 
                  "w", 
                  encoding="UTF-8")

    for content in contents:
        writer.write(content.text + "\n")
    

url = "https://m.blog.naver.com/sj3589/223496946522?referrerCode=1"

news = crawling(url)
txtFile(news)