#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import threading
import random
import uuid
from multiprocessing import Pool, cpu_count
import os
import sys
from ProductItem import ProductItem as ProductItem
import utils

import pp
import pymongo
import MySQLdb


reload(sys)
sys.setdefaultencoding("utf-8")
lock = threading.Lock()

#============= DB Mysql ==============
db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='880819',
    db='insurance',
    charset='UTF8'
)
cursor = db.cursor()

sql = "insert into product(uuid,id,company,productname,type,designtype,productattr," \
      "acceptance,period,paytype,termcode,salestate,stopsaledate,briefurl,detailurl,pdfurl)" \
      "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


def saveToMySql(p):
    params = (
        p.uuid,
        p.id,
        p.company,
        p.productname,
        p.type,
        p.designtype,
        p.productattr,
        p.acceptance,
        p.period,
        p.paytype,
        p.termcode,
        p.salestate,
        p.stopsaledate,
        p.briefurl,
        p.detailurl,
        p.pdfurl)
    cursor.execute(sql, params)
    db.commit()
    return

def truncateTableP():
    sql = 'truncate table product'
    cursor.execute(sql)
    db.commit()
    print "truncate table product"
    return
#============= DB Mysql ==============



#============= DB Mongodb ==============


def connectMongoOnce():
    # 多线程情况下 参数 connect=False
    myclient = pymongo.MongoClient("mongodb://localhost:27017", connect=False)
    # dblist = myclient.list_database_names()
    mydb = myclient["insurance"]
    mycol = mydb["product"]
    return mycol

def saveToMongo(datafile):
    mycol = connectMongoOnce()
    mycol.insert_one(datafile)
    # print "save %s OK" % datafile


def clearCollection():
    mycol = connectMongoOnce()
    x = mycol.delete_many({})
    print "Clear Mongodb [insurance], %d 个文档已删除" % x.deleted_count


#============= DB Mongodb ==============


HEADERS = utils.HEADERS
cnt = 10000
prodTypeCodeOne = "ProdTypeCode_00"
prodTypeCodeTwo = "ProdTypeCode_00_00"
prodTermsShow_prodTypeCode = "ProdTypeCode_00_00"
param ={
"pageNo": "1",
"pageCount": "200",
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_01",
"prodTypeCodeTwo": "ProdTypeCode_00_00",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
# "prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_01_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}


mainurl = "http://tiaokuan.iachina.cn:8090/sinopipi/loginServlet/publicQueryResult.do"
# r = requests.post(url, headers=HEADERS, data=param)
# print r.text
# soup = BeautifulSoup(r.text,'lxml')

url1= "http://www.iachina.cn/IC/tkk/01/"
url2= "http://www.iachina.cn/IC/tkk/02/"
url3= "http://www.iachina.cn/IC/tkk/03/"



def getIdListALL(url):
    idlistall = []
    for par in pp.plist:
        list = getIdList(url,par)
        idlistall=idlistall+list
        print "par: %s | %d " % (par["prodTermsShow.prodTypeCode"],list.__len__())
    print "Total List length : %d " % idlistall.__len__()
    return idlistall


def getIdList(url,par):
    # par = pp.param2
    r = requests.post(url, headers=HEADERS, data=par)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')
    bt1 = soup.select('#but1')[0]
    bt2 = soup.select('#but2')[0]
    click = soup.select('input[onclick]')
    # print click
    click.remove(bt1)
    # print click
    click.remove(bt2)
    # print click.__len__()
    idlist =[]
    for index,x in enumerate(click):
        info = x.attrs["onclick"]
        id = info[10:46]
        idlist.append(id)

    # print idlist
    # print idlist.__len__()
    return idlist




urlpage = "http://www.iachina.cn/IC/tkk/02/082e334a-153b-4f77-9cfe-3d2bdceda6d3.html"

def getProductInfo(id):
    url1 = "http://www.iachina.cn/IC/tkk/01/"
    url2 = "http://www.iachina.cn/IC/tkk/02/"
    url3 = "http://www.iachina.cn/IC/tkk/03/"
    detailurl = url2+id+'.html'
    # print detailurl
    html = requests.get(detailurl).text.encode("ISO-8859-1").decode("gbk")
    # print html
    soup = BeautifulSoup(html, "lxml")
    o = soup.find_all("td", attrs={"align": "left"})
    # print o

    product = ProductItem()
    product.uuid = uuid.uuid4()
    product.id = id
    product.company = o[0].get_text().rstrip().encode("utf-8")
    product.productname = o[1].get_text().rstrip().encode("utf-8")
    product.type = o[2].get_text().rstrip().encode("utf-8")
    product.designtype = o[3].get_text().rstrip().encode("utf-8")
    product.productattr = o[4].get_text().rstrip().encode("utf-8")
    product.acceptance = o[5].get_text().rstrip().encode("utf-8")
    product.period = o[6].get_text().rstrip().encode("utf-8")
    product.paytype = o[7].get_text().rstrip().encode("utf-8")
    product.termcode = o[8].get_text().rstrip().encode("utf-8")
    product.salestate = o[9].get_text().rstrip().encode("utf-8")
    product.stopsaledate = o[10].get_text().rstrip().encode("utf-8")
    product.briefurl = url1+id+'.html'
    product.detailurl = detailurl
    product.pdfurl = url3+id+'_TERMS.PDF'
    # print product.__dict__
    print product.company,product.productname
    return product



DIR_PATH = r"/Users/zhy/PycharmProjects/InsureProduct/TermPDF/"
def make_dir(folder_name):
    """
    新建套图文件夹并切换到该目录下
    """
    path = os.path.join(DIR_PATH, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        os.chdir(path)
        return True
    print("Folder has existed!")
    return False



def write_pdf(product):
    try:
        file = requests.get(product.pdfurl)
        filename = product.company+'_'+product.type+'_'+product.productname+'_'+product.termcode+'.pdf'
        with open(filename,'ab') as f:
            f.write(file.content)
            # print filename
            print "write local file OK : %s" % filename
    except Exception as e:
        print e


def SaveFile(product):
    folder_name = product.company
    path = os.path.join(DIR_PATH, folder_name)
    if make_dir(folder_name):
        write_pdf(product)
        os.chdir("..")
    else:
        os.chdir(path)
        write_pdf(product)
        os.chdir("..")


def doSave(product):
    filename = product.company+'_'+product.type+'_'+product.productname+'_'+product.termcode+'.pdf'
    SaveFile(product)
    saveToMySql(product)
    print "insert to mysql OK : %s " % filename
    saveToMongo(product.__dict__)
    print "save to mongodb OK : %s " % filename

def muiltThreadCrawler(id):
    with lock:
        p = getProductInfo(id)
        doSave(p)

if __name__ =="__main__":
    pool = Pool(processes=cpu_count())
    muiltThreadFlag = True
    try:
        truncateTableP()
        clearCollection()
        idlist = getIdListALL(mainurl)
        # idlist = getIdList(mainurl,pp.param1)
        print idlist.__len__()
        # 多线程版
        if muiltThreadFlag:
            print "MuiltTreadCrawler"
            pool.map(muiltThreadCrawler,idlist)
        else:  # 单线程版
            for index,id in enumerate(idlist):
                p = getProductInfo(id)
                doSave(p)
    except Exception as e:
        print e

