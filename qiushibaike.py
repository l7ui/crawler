# 爬取糗事百科图片

import requests
import re
import time
import os

# 正则表达式
ex = '<img src="(.*?)" alt=".*?" class=.*? width=.*? height=.*?>'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

baseurl = "https://www.qiushibaike.com/imgrank/page/%d/"

if not os.path.exists("./images"):
    os.mkdir("./images")

for num in range(1, 14):
    new_url = baseurl % num
    response = requests.get(new_url, headers)
    html = response.text
    # print(html)
    image_data = re.findall(ex, html)
    print(image_data)

    for image_single in image_data:
        time.sleep(0.5)
        image_single = "https:" + image_single  # 获得完整链接
        response_image = requests.get(image_single).content  # 请求单个图像网址
        image_name = image_single.split('/')[-1]  # 保存图片的名字
        image_path = "./images/" + image_name  # 文件路径
        with open(image_path, "wb") as fp:
            fp.write(response_image)
            print(image_name + " finish")
