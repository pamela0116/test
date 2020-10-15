# #爬虫的四个步骤：获取数据，解析数据，提取数据，储存数据
# import requests
#
# # 获取数据
# url = 'https://www.baidu.com'
# res = requests.get(url)
#
# # 解析数据
# html = res.text
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'html.parser')
#
# # 提取数据
# items = soup.find_all('div')
# for item in items:
#     item.text
#     item['href']

# def text_create(name,msg):
#     url = '/c/username/'
#     text_name = url+name+'.txt'
#     with open(text_name,'w') as f:
#         f.write(msg)
#
# def text_filter(word,cen_word='lame',change_word='hi'):
#     return word.replace(cen_word,change_word)
#
# def filter_text_create(name,msg):
#     msg_new = text_filter(msg)
#     text_create(name,msg_new)


# import openpyxl
# wb = openpyxl.load_workbook(r'F:\测试文档\parks_uid.xlsx')
# sheet = wb['小店区停车场']
# uid='1'
# name='2'
# address='3'
# lng='4'
# lat='5'
# sheet.append([uid, name, address, lng, lat])
# wb.save(r'F:\测试文档\parks_uid.xlsx')
#
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# account = 'pan1290613973@qq.com'  # input('请输入你的邮箱：')  # 登录邮箱
# password = 'dorhznqyjeizggdb'  # input('请输入你的密码：')  # 登录邮箱授权码
# receiver = ['panping0116@hotmail.com', '303644511@qq.com']  # input('请输入收件人的邮箱：')
# # 宋：'303644511@qq.com'，'panping0116@hotmail.com'
#
# def send_email():
#     global account,password,receiver
#     mailhost='smtp.qq.com'  # 发信服务器
#     qqmail = smtplib.SMTP()  # 指定qq邮箱服务器
#     qqmail.connect(mailhost,25)  # 连接qq邮箱服务器
#     qqmail.login(account,password)  # 登录邮箱
#     content = 'ceshi'
#     message = MIMEText(content, 'plain', 'utf-8')
#     message['From'] = '服务器管理员<1290613973@qq.com>'  # 发件人
#     message['To'] ='303644511@qq.com'  # 收件人
#     subject = '服务器报错啦，快去查看吧'  # 邮件主题
#     message['Subject'] = Header(subject, 'utf-8')
#     try:
#         qqmail.sendmail(account, receiver, message.as_string())  # 发送邮件
#         print ('邮件发送成功')
#     except:
#         print ('邮件发送失败')
#     qqmail.quit()  # 退出qq邮箱服务器
#
# # send_email()
#
# import paramiko
# def link_server_client(serverip, user, pwd, addr):
#     # 进行连接
#     print('------------开始连接服务器(%s)-----------' % serverip)
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('------------开始认证......-----------')
#     client.connect(serverip, 22, username=user, password=pwd, timeout=4)
#     print('------------认证成功!.....-----------')
# link_server_client('47.93.80.140', 'root', 'SxTw@2019$1', '/usr/java/tomcat')
# # link_server_client('47.93.83.95', 'root', 'SxTw@2019$2', '/usr/java/apache-tomcat-7.0.75')
# # link_server_client('39.106.69.146', 'root', 'SxTw@2019$3', '/usr/java/apache-tomcat-8.5.42')

# for i in range(1):
#     print(round(3.1,3))

# from decimal import Decimal

# a = 12.325
# print("%.2f" % a)
# print(round(a, 2))

# import xlrd
# workbook = xlrd.open_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\停车场坐标\ipark_park_info - 副本.xls')
# sheet = workbook.sheet_by_index(0)
# cols = sheet.col_values(1)
# for i in cols[1:]:
#     print(i)

# from xlutils import copy
# import xlrd
# import xlwt
# import pymysql
#
# database = pymysql.connect(host='139.9.133.242', user='root', password='111111', database='ipark', charset='utf8')
# cursor = database.cursor()
# sql = 'select NAME from ipark_park_info'
# try:
#    cursor.execute(sql)  # 执行SQL语句
#    results = cursor.fetchall()  # 获取所有记录列表
#    for row in results:
#        park = row[0]
#        print(park)
# except:
#    print ("Error: unable to fetch data")
# cursor.close()
# database.close()

# workbook = xlrd.open_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\停车场坐标\ts.xls',formatting_info=True)
# sheet = workbook.sheet_by_index(0)
#
# new_workbook = copy.copy(workbook)
# new_sheet = new_workbook.get_sheet(0)
#
# style = xlwt.XFStyle()  # excel样式
#
# font = xlwt.Font()  # 字体
# font.name = '微软雅黑'  # 字体
# font.bold = True  # 加粗
# font.height = 280  # 字号，excel的字号乘20
# style.font = font  # 把字体设置添加到样式中
#
# borders = xlwt.Borders()  # 边框
# borders.top = xlwt.Borders.THIN
# borders.bottom = xlwt.Borders.THIN
# borders.left = xlwt.Borders.THIN
# borders.right = xlwt.Borders.THIN
# style.borders = borders  # 把边框设置添加到样式中
#
# alignment = xlwt.Alignment()  # 对齐
# alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平对齐
# alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直对齐
# style.alignment = alignment
#
# new_sheet.write(1,1,'z',style)
# new_sheet.write(2,1,'x',style)
# new_sheet.write(3,1,'c',style)
# new_workbook.save(r'F:\测试文档\6（百度地图坐标爬虫）\停车场坐标\test.xls')

# import requests
# requests.packages.urllib3.disable_warnings()
# url = 'https://park.weiwopark.com/api/park/findParkInfoT.shtml'
# headers = {
#     'User-Agent': 'wwtc/2.2.3 (iPhone; iOS 12.2; Scale/3.00)',
#     'Content-Type': 'application/json',
#     'CELLPHONE': '18234017875'
# }
# data = {'LON': '112.553440', 'LAN': '37.802027'}
# res = requests.post(url, headers=headers, json=data, verify=False)  # ,verify=False
# json = res.json()
# parks = json['data']['datas']
# for park in parks:
#     print(park)

# # 阶乘
# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n-1)
# print(func(5))


# # 匿名函数
# add = lambda a, b: a + b
# print(add(2, 3))  # -->5
#
# from functools import reduce
# number = [2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
# positive = filter(lambda x: x > 0, number)
# average = reduce(lambda x, y: x + y, positive) / len(positive)
# print(average)

# def login(flag=0):
#     if flag:
#         def lgin(func):
#             u=''
#             p=''
#             if u == '':
#                 func()
#                 flag=0
#         return lgin
#
# @login(1)
# def home():
#     print('首页')
#
# def article():
#     print('文章')
#
# def api():
#     print('接口')

# import requests
# import json
# requests.packages.urllib3.disable_warnings()
# from bs4 import BeautifulSoup
#
# url = 'https://baike.baidu.com/item/%E5%B1%B1%E8%A5%BF%E7%9C%81%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/12777879'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
# params = {
#     'fr': 'aladdin'
# }
# res = requests.get(url, headers=headers, params=params,verify=False)  # ,verify=False
# html = res.text
# soup = BeautifulSoup(html,'html.parser')
# items = soup.find_all(class_="para")
# for item in items:
#     area = item.text
#     print(area)

# import requests
# import json
# def baidu_num(city,area):
#     url = 'http://api.map.baidu.com/place/v2/search'
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
#     params = {
#         'query': '{}停车场'.format(area),
#         'region': city,
#         'page_size': '20',
#         'page_num': 0,
#         'output': 'json',
#         'ak': 'VF77swtwMycxYNbGM3mwyiOXXsvWGPxC'
#     }
#
#     res = requests.get(url, headers=headers, params=params)  # ,verify=False
#     json = res.json()
#     nums = json['total']
#     print(nums)

# baidu_num('长治市','潞州区')

# import openpyxl
# wb = openpyxl.load_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\山西省(除太原市)停车场坐标\parks.xlsx')
# sheet = wb['Sheet1']
# for i in range(2, 106):
#     city = sheet['A{}'.format(i)].value
#     area = sheet['C{}'.format(i)].value
#     page = sheet['E{}'.format(i)].value
#     print(city, area, page)
# wb.close()

import requests
import time
# def baidu_parks(city,area,page):
#     # wb = openpyxl.load_workbook(r'F:\测试文档\gas_station.xlsx')
#     # sheet = wb['sheet']
#     for i in range(int(page)):
#         # url = 'https://api.map.baidu.com/'
#         url = 'http://api.map.baidu.com/place/v2/search'
#         headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
#         params = {
#             'query': '{}停车场'.format(area),
#             'region': city,
#             'page_size': '20',
#             'page_num': i,
#             'output': 'json',
#             'ak': 'VF77swtwMycxYNbGM3mwyiOXXsvWGPxC'
#         }
#         res = requests.get(url, headers=headers, params=params)  # ,verify=False
#         json = res.json()
#         parks = json['results']
#         for park in parks:
#             uid = park['uid']
#             name = park['name']
#             address = park['address']
#             province = park['province']
#             city = park['city']
#             area = park['area']
#             lng = park['location']['lng']
#             lat = park['location']['lat']
#             print(name)
#         time.sleep(5)
# baidu_parks('长治市','潞州区',1)

from collections import Counter

# import openpyxl
# # def area_code():
# wb1 = openpyxl.load_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\山西省(除太原市)停车场坐标\region.xlsx')
# sheet = wb1['region']
# area = {}
# for i in range(2, 144):
#     code = sheet['B{}'.format(i)].value
#     name = sheet['C{}'.format(i)].value
#     area[name]=code
# # print(area)
# # b = dict(Counter(uids))
# # print ([key for key,value in b.items()if value > 1])
#
#
# wb2 = openpyxl.load_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\山西省(除太原市)停车场坐标\area.xlsx')
# sheet = wb2['Sheet1']
# for i in range(2, 109):
#     city = sheet['A{}'.format(i)].value
#     a = sheet['B{}'.format(i)].value
#     if a not in area:
#         area[a] = 'wu'
#     area_cod = area[a]
#     print(area_cod)
# wb2.close()
# wb1.close()

# import socket, time, threading
# socket.setdefaulttimeout(3) #设置默认超时时间
# def socket_port(ip, port):
#     """
#     输入IP和端口号，扫描判断端口是否占用
#     """
#     try:
#         if port >= 65535:
#             print('端口扫描结束')
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         result = s.connect_ex((ip, port))
#         if result == 0:
#             lock.acquire()  # 获取锁
#             print(ip, ':', port, '端口已占用')
#             lock.release()  # 释放锁
#     except:
#         print('端口扫描异常')
#
# def ip_scan(ip):
#     """
#     输入IP，扫描IP的0-65534端口情况
#     """
#     try:
#         print('开始扫描 %s' % ip)
#         start_time = time.time()
#         for i in range(8080, 9000):
#             threading.Thread(socket_port(ip, int(i)))  # 开始一个新的线程并返回它的标识符
#         print('扫描端口完成，总共用时：%.2f' % (time.time()-start_time))
#         input("Press Enter to Exit")
#     except:
#         print('扫描ip出错')
# if __name__=='__main__':
#     url = input('Input the ip you want to scan: ')
#     lock = threading.Lock()  # 实例锁对象
#     ip_scan(url)

# import requests,openpyxl
# import time
#
# def baidu_parks(city,area,page):
#     wb = openpyxl.load_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\34台湾省.xlsx')
#     sheet = wb['Sheet1']
#     # for i in range(int(page)):
#     #     # url = 'https://api.map.baidu.com/'
#     url = 'http://api.map.baidu.com/place/v2/search'
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
#     params = {
#         'query': '{}停车场'.format(area),
#         'region': city,
#         'page_size': '20',
#         'page_num': 0,
#         'output': 'json',
#         'ak': '3rVySs3rr89Sg4HpMhshMrusnwKkMGEf'
#     }
#     res = requests.get(url, headers=headers, params=params)  # ,verify=False
#     json = res.json()
#     parks = json['results']
#     for park in parks:
#         uid = park['uid']
#         name = park['name']
#         address = park['address']
#         province = park['province']
#         city = park['city']
#         area = park['area']
#         lng = park['location']['lng']
#         lat = park['location']['lat']
#         print(name, city, area, lng, lat)
#         sheet.append([uid, name, address, 710000, province, 710000, city, 710000, area, lng, lat])
#     wb.save(r'F:\测试文档\6（百度地图坐标爬虫）\34台湾省.xlsx')
#
# baidu_parks('高雄市', '台湾', 1)

# import openpyxl
# wb = openpyxl.load_workbook(r'F:\测试文档\6（百度地图坐标爬虫）\1北京市.xlsx')
# sheet = wb['Sheet1']
# for i in range(2, 1885):
#     name = sheet['B{}'.format(i)].value
#     if '停车场' not in name:
#         print(name)

# 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# 计算器
# 1、检测用户输入，如非法报错
# 3、文本格式化（清除空格、替换++为+、替换+-为-）
# 4、先算括号
# 5、再算乘除
# 6、最后加减

print('ok')