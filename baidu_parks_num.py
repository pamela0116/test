import requests
import openpyxl
import time

def baidu_num(city,area):
    url = 'http://api.map.baidu.com/place/v2/search'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    params = {
        'query': '{}停车场'.format(area),
        'region': city,
        'page_size': '20',
        'page_num': 0,
        'output': 'json',
        'ak': '3rVySs3rr89Sg4HpMhshMrusnwKkMGEf'
    }
    res = requests.get(url, headers=headers, params=params)  # ,verify=False
    json = res.json()
    nums = json['total']
    print(nums)

wb = openpyxl.load_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\area.xlsx')
sheet = wb['Sheet1']
for i in range(2, 20):
    city = sheet['C{}'.format(i)].value
    area = sheet['D{}'.format(i)].value
    baidu_num(city, area)
