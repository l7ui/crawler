# 爬取糗事百科图片

import requests
import re
import time
import os

folder_name = 'E:/Document/images/qiushibaike/'

def get_images():
    # 正则表达式
    ex = 'img src="(.*?)jpg"'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    baseurl = "https://www.qiushibaike.com/imgrank/page/%d/"

    for num in range(1, 14):
        new_url = baseurl % num
        response = requests.get(new_url, headers)
        html = response.text
        # print(html)
        url_list = re.findall(ex, html)

        for img_url in url_list:
            time.sleep(1)
            img_url = 'http:' + img_url + 'jpg'   # 获得完整链接
            print(img_url)
            response_image = requests.get(img_url).content  # 请求单个图像网址
            image_name = img_url.split('/')[-1]  # 保存图片的名字
            image_path = folder_name + image_name  # 文件路径
            with open(image_path, "wb") as fp:
                fp.write(response_image)
                print(image_path + " finish")


if __name__ == '__main__':
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    get_images()

