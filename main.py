import requests

headers = {
    'Host': "www.duitang.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    'Cookie': "js=1; sessionid=9530d068-13d1-4bc2-b433-4b2777035aa0; js=1; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1610119798; __dtac=; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1610120524"
}

url = 'https://www.duitang.com/p/atlas/?id=124020193'

response = requests.get(url, headers)

print(response)

