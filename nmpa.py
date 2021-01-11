import requests
import os
import json

folder_path = './nmpa/'

def get_ids():
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    post_data = {
        'on': 'true',
        'page': '1',
        'pageSize': '20',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    response = requests.post(url=post_url, data=post_data, headers=headers)
    json_obj = response.json()
    ids = []
    for dict in json_obj['list']:
        ids.append(dict['ID'])
    return ids

def get_certification():
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    ids = get_ids()
    file_path = folder_path + 'xkzs.json'
    fp = open(file_path, 'a', encoding='utf-8')
    for id in ids:
        post_data = {
            'id': id
        }
        response = requests.post(url=post_url, data=post_data, headers=headers)
        json_obj = response.json()
        json.dump(json_obj, fp, ensure_ascii=False)
    print(file_path + ' saved!')


if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    get_certification()
