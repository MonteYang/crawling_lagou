#-*- coding: utf-8 -*-
import requests
import pymongo
from pymongo import MongoClient
import datetime
import time


client = MongoClient('localhost', 27017)
db = client.data_position # 创建一个data_position数据库
collection = db.pachong_3 # 创建一个pachong集合

for i in range(2):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=1'
    payload ={
        'first': 'true',
        'pn': i+1,
        'kd': '爬虫'
    }
    headers = {
        'Cookie': '59-05a7ce82a22054-1f20130c-2073600-16410e12c92f3d; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1529291550; _ga=GA1.2.1962030681.1529291550; user_trace_token=20180618111230-6f85751d-72a5-11e8-a8e3-525400f775ce; LGUID=20180618111230-6f85795d-72a5-11e8-a8e3-525400f775ce; _gid=GA1.2.1869280888.1529291550; X_HTTP_TOKEN=5154d44589ffc19f8f8572e82b2ad3b7; _putrc=217FDF00EA61DA36123F89F2B170EADC; login=true; unick=%E6%9D%A8%E8%8C%82%E7%94%B7; JSESSIONID=ABAAABAAAIAACBI0D3DBD77A9CC255A08C3E8BA0C8C9D16; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=5; gate_login_token=394d2e9df746c3e306aa92a38acbee46c11dbb273c6e51e1c9f321541ebe057e; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=search_code; _gat=1; LGSID=20180618134453-b96761fb-72ba-11e8-a8ee-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3Fpx%3Ddefault%26gx%3D%25E5%25AE%259E%25E4%25B9%25A0%26city%3D%25E5%258C%2597%25E4%25BA%25AC%26isSchoolJob%3D1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3Fpx%3Ddefault%26gx%3D%26isSchoolJob%3D1%26city%3D%25E5%258C%2597%25E4%25BA%25AC; SEARCH_ID=571ee541e844469990daf247029cd836; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1529300735; LGRID=20180618134535-d26b81f0-72ba-11e8-a8ee-525400f775ce',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Referer': r'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?px=default&gx=&isSchoolJob=1&city=%E5%85%A8%E5%9B%BD'
    }
    r = requests.post(url, data=payload, headers=headers)
    # print(r.json()['content']['positionResult']['result'])
    data = r.json()['content']['positionResult']['result']
    collection.insert(data)
    print('正在插入第{}页职位信息'.format(str(i+1)))
    time.sleep(1)

print("Done")
