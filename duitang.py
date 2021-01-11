# 爬取堆糖图片

import requests
import time
import os

folder_path = 'D:/Document/images/duitang/waller/'

def test():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }
    baseurl = "https://www.duitang.com/napi/vienna/atlas/detail/?atlas_id=%d"

    start_id = 124020195
    end_id = start_id + 10

    for num in range(start_id, end_id):
        new_url = baseurl % num
        response = requests.get(new_url, headers)
        json_obj = response.json()
        # print(html)
        image_blogs = json_obj['data']['blogs']

        for image_blog in image_blogs:
            image_url = image_blog['photo']['path']
            print(image_url)
            time.sleep(0.5)
            response_image = requests.get(image_url).content  # 请求单个图像网址
            image_name = image_url.split('/')[-1]  # 保存图片的名字
            image_path = "./images/" + image_name  # 文件路径
            with open(image_path, "wb") as fp:
                fp.write(response_image)
                print(image_name + " finish")

def get_kw():
    get_url = 'https://www.duitang.com/napi/blog/list/by_search/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    start_id = 1610371634917
    end_id = start_id + 10

    for id in range(start_id, end_id):
        get_params = {
            'kw': '壁纸',
            'type': 'feed',
            'include_fields': 'top_comments,is_root, source_link, item, buyable, root_id, status, like_count, like_id, sender, album, reply_count, favorite_blog_id',
            '_type': '',
            'start': (id - start_id + 1) * 24,
            '_': id
        }
        response = requests.get(url=get_url, params=get_params, headers=headers)
        json_obj = response.json()
        image_list = json_obj['data']['object_list']
        for image in image_list:
            image_url = image['photo']['path']
            print(image_url)
            time.sleep(0.1)
            response_image = requests.get(image_url).content
            image_name = image_url.split('/')[-1]
            image_path = folder_path + image_name
            fp = open(image_path, 'wb')
            fp.write(response_image)
            print(image_path + " saved!")


if __name__ == '__main__':
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    get_kw()