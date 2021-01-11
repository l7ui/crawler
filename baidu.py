import os
import requests
import json

folder_path = './baidu/'

def translate():
    post_url = 'https://fanyi.baidu.com/sug'
    post_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    word = input('input the word:\n')
    post_data = {
        'kw': word
    }
    response = requests.post(url=post_url, data=post_data, headers=post_headers)
    file_path = folder_path + word + '.json'
    json_obj = response.json()
    fp = open(file=file_path, mode='w', encoding='utf-8')
    json.dump(obj=json_obj, fp=fp, ensure_ascii=False)
    print(file_path + ' saved!')

if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    translate()