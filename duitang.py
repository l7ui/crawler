# 爬取堆糖图片

import requests
import time
import os
import sys

params = {
    'diannaobizhi': {
        'id': 1610372830329,
        'kw': '电脑壁纸'
    },
    'chengxiao': {
        'id': 1610373907289,
        'kw': '程潇'
    },
    'shoujibizhi': {
        'id': 1610377600148,
        'kw': '手机壁纸'
    },
    'meinv': {
        'id': 1610378156225,
        'kw': '美女'
    },
    'touxiang': {
        'id': 1610378665418,
        'kw': '头像'
    }
}

keyword = input('input the keyword:\n')
if not params.get(keyword):
    print('***\nempty keyword!\n***')
    sys.exit(0)

folder_path = 'E:/Document/images/duitang/' + keyword + '/'

def get_kw():
    get_url = 'https://www.duitang.com/napi/blog/list/by_search/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    start_id = params[keyword]['id']
    end_id = start_id + 24
    count = 0

    for id in range(start_id, end_id):
        get_params = {
            'kw': params[keyword]['kw'],
            'type': 'feed',
            'include_fields': 'top_comments,is_root, source_link, item, buyable, root_id, status, like_count, like_id, sender, album, reply_count, favorite_blog_id',
            '_type': '',
            'start': (id - start_id) * 24,
            '_': id
        }
        response = requests.get(url=get_url, params=get_params, headers=headers)
        json_obj = response.json()
        image_list = json_obj['data']['object_list']
        for image in image_list:
            image_url = image['photo']['path']
            count += 1
            print(image_url + ':' + str(count))
            time.sleep(0.1)  # 反爬虫冷静
            try:
                response_image = requests.get(image_url, timeout=5).content
                image_name = image_url.split('/')[-1]
                image_path = folder_path + image_name
                fp = open(image_path, 'wb')
                fp.write(response_image)
                print(image_path + " saved!")
            except:
                print('***\ntimeout, pass!\n***')


if __name__ == '__main__':
    print('crawler started...')
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    get_kw()
    print('crawler finished!')