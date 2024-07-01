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

def allTxt(contents):
    stentence = ""
    for content in contents:
        stentence += (content.text + "\n")
    return stentence

def count_news(news) :    
    count_word = "기자"
    count  = 0
    word_list = news.split(".")
    for word in word_list :
        if count_word in word : count += 1
    return count

url = "https://m.blog.naver.com/sj3589/223496946522?referrerCode=1"

news = allTxt(crawling(url))
count_news(news)