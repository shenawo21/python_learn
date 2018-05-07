import json
import requests
from requests.exceptions import RequestException
import re
import time

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    print(isinstance(html, dict))
    print(isinstance(html, str))
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    # print(isinstance(html,str))
    print(1)
    for item in parse_one_page(html):
        print(2)
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    # for i in range(10):
    #     main(offset=i * 10)
    #     time.sleep(1)
    main()