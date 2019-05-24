#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-4-23 08:20
# @Author  : zhdya@zhdya.cn
# @File    : TESTAAA.py

###套图爬取下载（需要给定指定的二级目录）
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.mzitu.com/141253'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
           ,'Referer':'http://www.mzitu.com/'}

html = requests.get(url,headers = headers)
soup = BeautifulSoup(html.text,'html.parser')

pic_max = soup.find_all('span')[9].text

title = soup.find('h2',class_='main-title').text


for i in range(1, int(pic_max)+1):
    herf = url+"/"+str(i)
    print(herf)
    html = requests.get(herf, headers = headers)
    mess = BeautifulSoup(html.text, 'html.parser')

    pic_url = mess.find('img', alt=title)
    # print(pic_url)
    html = requests.get(pic_url['src'], headers=headers)
    file_name = pic_url['src'].split(r'/')[-1]
    with open(file_name, 'wb') as f:
        f.write(html.content)
    time.sleep(2)
###################################################################
##下载全平台mzitu
# import requests
# from bs4 import BeautifulSoup
# import os
# import sys
# import time
#
# if os.name == "nt":
#     print(u'你使用的平台是Windows')
# else:
#     print(u'你使用的平台是Linux')
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
#             ,'Referer':'http://www.mzitu.com/'}
#
# #http请求头
# all_url = "http://www.mzitu.com"
# start_html = requests.get(all_url, headers = headers)
# # print(start_html.text)
#
# #保存地址
# path = "D:/mzitu/"
#
# #找寻最大页数
# soup = BeautifulSoup(start_html.text, 'html.parser')
# page = soup.find_all('a', class_='page-numbers')
# max_page = page[-2].text
# print("总共：{} 页".format(max_page))
#
# same_url = 'http://www.mzitu.com/page/'
#
# for i in range(1, int(max_page)+1):
#     ul = same_url+str(i)
#     start_html = requests.get(ul, headers = headers)
#     # print(start_html.text)
#     soup = BeautifulSoup(start_html.text, 'html.parser')
#     all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
#     for a in all_a:
#         # print("aaaaaa", a)
#         title = a.get_text() #提取文本
#         if(title != ''):
#             print("准备扒取："+title)
#             if os.path.exists(path+title.strip().replace('?','')):
#                 flag =1
#             else:
#                 os.mkdir(path+title.strip().replace('?',''))
#                 flag =0
#             os.chdir(path+title.strip().replace('?',''))
#             herf = a['href']
#             html = requests.get(herf, headers=headers)
#             mess = BeautifulSoup(html.text, 'html.parser')
#             # print("messss", mess)
#             pic_max = mess.find_all('span')[9].text ##单个套图的最大页数
#             # print("asdasd", pic_max)
#             if flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max):
#                 print("已经保存过了！！")
#                 continue
#             for num in range(1, int(pic_max)+1):
#                 time.sleep(1)  ##每隔1s 去爬取一次！
#                 pic = herf + '/' + str(num)
#                 print(pic)
#                 html = requests.get(pic, headers=headers)
#                 mess = BeautifulSoup(html.text, "html.parser")
#                 pic_url = mess.find('img', alt=title)
#                 html = requests.get(pic_url['src'], headers=headers)
#                 file_name = pic_url['src'].split(r'/')[-1]
#                 with open(file_name, 'wb') as f:
#                     f.write(html.content)
#             print("{} <<保存完成!!>>".format(title))
#     print("{}页已经完成".format(i))

