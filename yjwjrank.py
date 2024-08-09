import requests
import urllib
from urllib import parse
import time

def getname():
    oldestname = input("请输入永劫无间ID(请注意，如果发现查询出来的战绩与自己战绩不符，说明你的id输入有误，请检查是否有特殊字符或空格)：")
    name = urllib.parse.quote(oldestname)
    return name
def nameolding(name):
    return urllib.parse.unquote(name)

def hint(name):
    url = f'https://record.uu.163.com/api/naraka/auth/{name}/163'
    headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://record.uu.163.com/naraka/query",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }
    response = requests.get(url, headers=headers)
def getrecord(name):
    url = 'https://record.uu.163.com/api/naraka/battles'
    headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "cookie": "",
    "sec-fetch-mode": "cors",
    "referer": f"https://record.uu.163.com/naraka/?name={name}&server=163",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    '''for i in range(1, 5):
        params={
        "page": f"{i}",
        "page_size": "10"
        }
        response = requests.get(url, headers=headers, params=params)
        print(response.text)'''

    params={
    "page": "1",
    "page_size": "10"
    }
    response = requests.get(url, headers=headers, params=params)
    data_json = response.text
    return data_json

def time_shift(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

