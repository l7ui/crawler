import requests
import os
import json

folder_path = './douban/'

def top_list():
    post_url = 'https://movie.douban.com/j/chart/top_list'
    post_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    post_data = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '1'
    }
    response = requests.post(url=post_url, data=post_data, headers=post_headers)
    file_path = folder_path + 'action_list.json'
    fp = open(file_path, 'w', encoding='utf-8')
    json_obj = response.json()
    json.dump(json_obj, fp=fp, ensure_ascii=False)
    print(file_path + ' saved!')


if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    top_list()
