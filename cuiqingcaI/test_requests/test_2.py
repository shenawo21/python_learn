# import requests
#
# files = {'file': open('favicon.ico','rb')}
#
# r = requests.post('http://httpbin.org/post', files=files)
#
# print(r.text)

# import requests
#
# r = requests.get('http://www.baidu.com')
#
# for key, value in r.cookies.items():
#     print(key+'='+value)
#
# a = 5
#
# def add():
#     a = 6
#     print(a)
#
# add()
#
# a = (1,2,3)
#
# print(a[3:])

# import requests
#
# session = requests.session()
# session.get('http://httpbin.org/cookies/set/number/12456')
# res = session.get('http://httpbin.org/cookies')
# print(res.text)

# import  requests
# import urllib3
#
# urllib3.disable_warnings()
#
# res = requests.get('https://12306.cn', verify=False)
#
# print(res.status_code)

# import requests
#
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)
#
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
proxies = {
  "http": "http://127.0.0.1:9743",
  "https": "https://127.0.0.1:9743",
}
try:
    response = requests.get("https://www.taobao.com", proxies=proxies)
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')

# print(response.status_code)

# import requests
# from requests.exceptions import ReadTimeout, ConnectionError, RequestException
# try:
#     response = requests.get("http://httpbin.org/get", timeout = 0.5)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')
# except ConnectionError:
#     print('Connection error')
# except RequestException:
#     print('Error')