from crw_test import crawling, allTxt, count_news
from kobart_test import newSum

## 1. 뉴스 내용 전체 크롤링 ##
url = "https://m.blog.naver.com/sj3589/223496946522?referrerCode=1"

# 기사 내용
input_text = allTxt(crawling(url))
# 기사 개수
countNews_i = count_news(input_text)

# 특정 단어 단위로 리스트에 저장 #
newsList = input_text.split("[")
newsList0_split = newsList[0].split("★")
print("-", newsList0_split[1], "-")


## 2. 크롤링 내용 기반 본문 요약 ##
# 기사 개수만큼 반복 수행 -> 출력
for i in range(1, len(newsList)):
    smallTitle_split = newsList[i].split(")")
    smallTile = "[" + smallTitle_split[0] + ")"
    print(smallTile)
    print(i, ")", newSum(newsList[i]))
    print()

