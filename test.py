import json
import urllib.request,urllib.parse
import os
import zipfile
from urllib import request,parse

l=[]
pan=0
f=open('data.json',encoding='utf-8')#打开‘data.json’的json文件
res=f.read()
data=json.loads(res)#加载json数据

key=data.keys()
for num in key:
    d=data[num]['cases']
    for de in d:
        pan=0
        id=de["case_id"]
        for temp in l:
            if(temp==id):
                pan=1
                break
        if(pan==0):
            l.append(id)
            pan=0
            count=0
            sco=0
            lenth=0
            size=0
            for tnum in key:
                td=data[tnum]['cases']
                for x in td:
                    if(x["case_id"]==id):
                        count+=1
                        sco+=x["final_score"]
                        lenth += len(x["upload_records"])
                        filename = urllib.parse.unquote(os.path.basename(de["case_zip"]))  # 获取文件名，url里对中文会urlencode，解个码
                        # 中文转Unicode编码
                        b = b'/:?=&#'  # 此处定义忽略转码的字符
                        new_url = parse.quote(de["case_zip"], b)
                        urllib.request.urlretrieve(new_url, filename)  # 下载题目包到本地
                        read_hey = zipfile.ZipFile(filename)
                        t = read_hey.namelist()
                        information = read_hey.getinfo('.mooctest/answer.py')
                        size += information.file_size#information.file_size,.compress_size

            sco=sco/count
            print(id)
#           print(de["upload_records"][0])

            print(de["case_type"])
            name = de["case_type"]
            temp1=0
            if name == "排序算法" or name=="数字操作" or name=="线性表":
                temp1 = 4
            elif name == "查找算法" or name=="数组":
                temp1 = 6
            elif name == "字符串" or name=="树结构":
                temp1 = 8
            elif name == "图结构":
                temp1 = 10

            print(len(de["upload_records"]))
            lenth=lenth/count
            temp2=0
            if lenth==0:
                temp2=10
            elif lenth>0 and lenth<=5:
                temp2=2
            elif lenth > 5 and lenth <= 10:
                temp2 = 4
            elif lenth > 10 and lenth <= 20:
                temp2 = 6
            elif lenth>20 and lenth<=50:
                temp2=8
            elif lenth>50:
                temp2=10

            print(sco)
            temp3=0
            if sco<=20:
                temp3=10
            elif sco<=40:
                temp3=8
            elif sco<=60:
                temp3=6
            elif sco<=80:
                temp3=4
            elif sco<=100:
                temp3=2

            print(information)
            size=size/count
            temp4=0
            if size<=200:
                temp4=2
            elif size<=500:
                temp4=4
            elif size<=1000:
                temp4=6
            elif size<=3000:
                temp4=8
            elif size>3000:
                temp4=10

            res=0.3*temp1+0.2*temp2+0.2*temp3+0.3*temp4
            print(res)