# -*- coding: utf-8 -*-
# @Time    : 2022/3/21 上午11:09
# @Author  : YeaHii

import optparse
import os
import time
import re
import requests
import threading
import json
import random
from func_timeout import func_set_timeout

file_f = "../../search_report_mem/"
file_p = ".txt"

ua = random.choice([
"Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
"Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
"Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
"Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
"Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"])

head = {
        "User-Agent":ua
}

# 操作 配置
def os_c():
    parser = optparse.OptionParser()
    parser.add_option('-u',dest='domain',help='query domain finger')
    parser.add_option('-f',dest='file',help='more url scan')
    parser.add_option('-s',dest='subdomain',help='ssl crt.sh and fuzz collection subdomain')
    parser.add_option('-d',dest='Deduplication',help='Deduplication')
    parser.add_option('-j',dest='dic_tojson',help='dic type to be json -j + json')
    parser.add_option('-t',dest='type',help='divide type -t + type')
    (options,args) = parser.parse_args()

    if options.domain:
        url = options.domain
        find_finger(url)
    elif options.file:
        file_path = file_f+options.file+file_p
        file_scan(file_path)
    elif options.Deduplication:
        url_D = options.Deduplication
        Deduplication(url_D)
    elif options.dic_tojson:
         dic_tojson(options.dic_tojson)
    elif options.type:
         flag = options.type
         divide(flag)
    elif options.subdomain:
        url_s = options.subdomain
        os_path = file_f + url_s + file_p
        if os.path.exists(os_path):
            print(os_path + " file is exist")
        else:
            a = ssl_sub_domain(url_s)
            a.spider_ssl()
            b = fuzz(url_s)
            b.web_sub_domain()

# 调用 TiteFinger 进行扫描 one
def find_finger(url,p=0,m=50,time=5,dir=0):
    os_path = "TideFinger.py"
    # os.system('python ' + filepath + ' -u ' + url + " -m " +m + " -p " + p + " -t " + time + " -d " + dir )
    os.system('python '+ os_path + ' -u ' + url)
# 多次调用TiteFinger 进行扫描, 文件扫描
def file_scan(url_file):
   try:
       with open(url_file, "r", encoding="utf8") as f:
           url = f.readline()
           while url:
               url = "https://" + url
               time.sleep(1)
               find_finger(url)
               url = f.readline()
   except:
       print("file is not exist")


# 子域名爆破,速度慢,多线程 有尝试过
class fuzz:
    def __init__(self,domain):
        self.domain = domain
    # 这个注释是 方法超时时间(爆破时间太长了) 超过三分钟就停下来
    @func_set_timeout(180)
    def web_sub_domain(self):

        search_memory = "../../python_cms/search_report_mem/" + self.domain +'.txt'
        with open('../../dic/dic.txt','r',encoding='utf8') as rf:
            key = rf.readline().strip()

            while key:
                url ="http://" + key + "." + self.domain
                try:
                    response = requests.get(url,headers=head)
                    if response.status_code == 200:
                        with open(search_memory,'a+',encoding='utf8') as wf:
                            wf.write(url + '\n')
                        print(url)
                except:
                    pass
                key = rf.readline().strip()


# ssl 证书 查询小爬虫,然后可以通过去重完成目的
class ssl_sub_domain:
    def __init__(self,url):
        self.url = url

    def spider_ssl(self):
        # 要改,单独提出一个函数 ,在全部子域名写入后 再进行去重
        # mys = set()
        url = 'https://crt.sh/?q='+ self.url
        l = []
        response = requests.get(url,head)

        html = response.text
        content = re.compile(r".[^ =]+" + self.url)
        co = content.findall(html)
        for i in co:
            i = i.replace('<TD>', "").replace('<BR>', "\n").strip()
            l.append(i)
            # mys.add(i)
        file_path = "../../search_report_mem/" + self.url + ".txt"
        with open(file_path,'a+',encoding='utf8') as wf:
            for x in l:
                x = x.replace("*.","").replace("'","")
                wf.write(x)
                wf.write('\n')

# 去除重复的域名 吐槽: 扫出一万左右 去重后  300-500个域名
def Deduplication(filename): # 文件名 example baidu.com
    mys = set()
    D_filepath = "../../search_report_mem/" + filename + ".txt"
    with open(D_filepath,"r",encoding="utf8") as D_rf:
        f = D_rf.readline()
        while f:
            # if "".__eq__(f):
            #     continue
            mys.add(f)
            f = D_rf.readline()
        l = list(mys)
        with open(D_filepath,"w",encoding="utf8") as D_wf:
            for i in l:
                D_wf.write(i)

# 字典转成json 保存
def dic_tojson(Restore):
    if "json".__eq__(Restore):
        Restorepath = "../Web_Information/Restore.txt"
        Restorepath2 = "../Web_Information/Restore.json"
        l = []
        with open(Restorepath,"r",encoding="utf8") as r :
            while True:
                data = r.readline()
                if not data:
                    break
                l.append(data)
        with open(Restorepath2,"w",encoding="utf8") as w:
            json.dump(l,w,ensure_ascii=False)
            w.write('\n')
    else:
        # 后面可能增加功能
        print("请在-j后输入json,提示转成json数据保存")


'''
通过 Nginx | Vue | PHP 等等架构分类,通过找指定文件找到对应架构的网站doamin
然后 针对性找漏洞脚本
'''
def divide(type):
    if "type".__eq__(type):
        mys = set()
        mys_t = set()

        with open("../Web_Information/Restore.json","r",encoding="utf8")as r :
            data = r.readline()
            datas = json.loads(data,strict=False)

            for i in datas:
                i = eval(i)
                for key, value in i.items():
                    # print(key)
                    # print(value)
                    for m, n in value.items():
                        if ("banner".__eq__(m)):
                            a = n.split("|")
                            for j in a:
                                j = j.strip()
                                mys.add(j)
                                with open("../Web_Information/banner_" + j + ".txt", "a+", encoding="utf8") as mset:
                                    mset.write(key)
                                    mset.write("\n")

                        elif ("Cms_name".__eq__(m)):
                            a = n.split("|")
                            for z in a:
                                if z not in mys_t:
                                    mys_t.add(z)
                                    with open("../Web_Information/cms_" + z + ".txt", "a", encoding="utf8") as mset_t:
                                        mset_t.write(key)
                                        mset_t.write("\n")
    else:
        print("请在-t后面添加type提示进行分类")


# start
if __name__ == '__main__':
    os_c()
