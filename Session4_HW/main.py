import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

f = open('webtoon.csv', mode='w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(['title','cartoonist','grade'])

final_result = []

WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=wed'
webtoon_html = requests.get(WEBTOON_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box = webtoon_soup.select_one("ul.img_list")
webtoon_list = webtoon_list_box.select("li")

final_result = extract_info(webtoon_list)

for result in final_result:
  row=[]
  row.append(result['title'])
  row.append(result['cartoonist'])
  row.append(result['grade'])
  writer.writerow(row)
print(final_result)


