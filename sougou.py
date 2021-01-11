import os
import requests

folder_path = './sogou/'

def main_page():
    url = 'https://www.sogou.com/'
    response = requests.get(url=url)
    page_text = response.text
    file_path = folder_path + 'main.html'
    with open(file_path, mode='w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_path + ' saved successfully!')


def query():
    url = 'https://www.sogou.com/web'
    kw = input('key work to query:\n')
    params = {
        'query': kw
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url=url, params=params, headers=headers)
    page_text = response.text
    file_path = folder_path + kw + '.html'
    with open(file_path, mode='w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_path + ' saved successfully!')


if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    main_page()
