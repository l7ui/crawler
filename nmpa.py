# 爬取监管局化妆品生产许可证

import requests
import os
import json

folder_path = './nmpa/'

def get_ids():
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    pageNumber = 11
    ids = []
    for page in range(1, pageNumber):
        post_data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        response = requests.post(url=post_url, data=post_data, headers=headers)
        print(post_url + ':' + str(page))
        json_obj = response.json()
        for dict in json_obj['list']:
            ids.append(dict['ID'])
    return ids

def get_certification():
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    ids= get_ids()
    file_path = folder_path + 'xkzs.json'
    fp = open(file_path, 'w', encoding='utf-8')
    totalCount = 0
    data_list = []
    for id in ids:
        post_data = {
            'id': id
        }
        response = requests.post(url=post_url, data=post_data, headers=headers)
        totalCount += 1
        print(post_url + ':' + str(totalCount))
        json_obj = response.json()
        data_list.append(json_obj)
    json.dump(data_list, fp, ensure_ascii=False)
    print(file_path + ' saved!')


if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    get_certification()
