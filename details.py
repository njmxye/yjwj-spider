import requests
import json
def clean_details():
    def details():
        room_id = input("请输入房间号：")
        url = f'https://record.uu.163.com/api/naraka/battle/detail/{room_id}'

        headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "cookie": "",
        "priority": "u=1, i",
        "referer": f"https://record.uu.163.com/naraka/detail?id={room_id}",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }

        response = requests.get(url, headers=headers)
        resjson = json.loads(response.text)
        return resjson
    text = details()
    
