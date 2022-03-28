def extract_info(webtoon_list):
  result = []

  for webtoon in webtoon_list:
    title = webtoon.select_one("dl > dt > a").string
    cartoonist = webtoon.select_one("dl > dd.desc > a").string
    grade = webtoon.select_one("dl> dd > div.rating_type > strong").string

    webtoon_info = {
      'title': title,
      'cartoonist': cartoonist,
      'grade': grade,
    }
    result.append(webtoon_info)
  return result


