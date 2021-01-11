import requests
import os
import json

folder_path = './kfc/'

def location():
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }
    post_data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '1'
    }
    response = requests.post(url=post_url, data=post_data, headers=headers)
    json_txt = response.text
    file_path = folder_path + 'beijing_location.json'
    fp = open(file_path, 'w', encoding='utf-8')
    json.dump(json_txt, fp, ensure_ascii=False)
    print(file_path + ' saved!')


if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    location()

