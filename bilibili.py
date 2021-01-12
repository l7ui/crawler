import requests
import matplotlib.pyplot as plt
import os
import jieba
from wordcloud import WordCloud
import time


def weekly_hit():
    get_url = 'https://api.bilibili.com/x/web-interface/popular/series/one?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    max_number = 95

    ups = []
    tnames = ''

    print('crawler started...')
    for number in range(1, max_number):
        get_params = {
            'number': number
        }
        response = requests.get(url=get_url, params=get_params, headers=headers)
        print(get_url + ':' + str(number))
        json_obj = response.json()
        list = json_obj['data']['list']
        for video in list:
            ups.append(video['owner']['name'])
            tnames += video['tname']

    print('crawler finished!')
    plot(ups, 'up')
    cut_text = jieba.cut(tnames)
    plot(tnames, 'tname')


def plot(text, name):
    words = ','.join(text)
    wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920, height=1080, margin=5)
    wc.generate(words)
    wc.to_file(r''+name+'.jpg')  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰

if __name__ == '__main__':
    weekly_hit()
