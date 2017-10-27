# -*- coding: utf-8 -*-
import datetime

import scrapy
from bs4 import BeautifulSoup

from crawlAutohomeCarpeizhi.items import carpeizhiItem


class SpidercarSpider(scrapy.Spider):
    name = 'spidercar'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = [
        'http://car.autohome.com.cn/config/series/4069.html', #x40
        'http://car.autohome.com.cn/config/series/4166.html', #宝骏510
        'http://car.autohome.com.cn/config/series/3824.html', #森雅R7
        'http://car.autohome.com.cn/config/series/3080.html', #瑞风S3
        'http://car.autohome.com.cn/config/series/2778.html', #长安CS35
        'http://car.autohome.com.cn/config/series/632.html' #B50
        #http://www.autohome.com.cn/a/
                  ]


    def __init__(self, **kwargs):
        self.count=0

    def start_requests(self):
        for url in self.start_urls:
            request= scrapy.Request(url=url, callback=self.parse)
            # request= scrapy.Request(url=url, callback=self.parse)
            request.meta['isjs']='True'
            yield  request

    # def getCarlink(self,response):


    def parse(self, response):

        # tcontent=response.meta['tcontent']
        #配置
        rowdict=response.meta['rowdict']
        #车型
        cartypelist=response.meta['cartypelist']
        print('rowdict:', rowdict)
        print('rowdictlen:', len(rowdict))
        switem = carpeizhiItem()
        cardict={}
        cararray = []
        for key in switem.switcher:
            #去掉基本参数等小标题，转换二维数组
            # if switem.switcher.get(key):
            values = rowdict.get(key,'')
            # va= values.split(',')
            cararray.append(values)
            # for i in values:
            #     item[item.switcher.get(key)] = i
            #     cardict[key]=i
            #     print(item.switcher.get(key),i)


        print('cardict=', cardict)
        print('cararray:', cararray)
        print('cararray长度：',len(cararray))
        # cararray.
        # listb2 = [[r[col] for r in cararray] for col in range(len(cararray[0]))]

        itemlist = []
        for col in range(len(cararray[0])):
            l = []
            for r in cararray:
                try:
                    # print('r[col]:', r[col])
                    l.append(r[col])
                except IndexError:
                    # print('r[col]:', '')
                    l.append('')
            itemlist.append(l)

        # print('itemlistlen=',len(itemlist))
        # print('itemlist=',itemlist)

        # print('rowlist.get[厂商指导价]:', self.listget(rowlist,'厂商指导价',' '))


        #获取页面信息
        webname = response.css('.subnav .subnav-title .subnav-title-name a::text').extract_first()
        # wgyanse = response.css('.color-ul *::text').extract_first()
        # wgyanse = response.css('.color-ul *::text').extract_first()

        soup = BeautifulSoup(response.text, 'lxml')

        #当前位置
        pathnav = soup.find('div', class_='path')
        pathtext=pathnav.get_text(strip=True)
        print('pathtext=',pathtext)

        #颜色
        colorul=soup.findAll('ul',class_='color-ul')
        for c in colorul:
            color = c.get_text(separator=' ', strip=True)
        #     print(color)
        # tbcs = soup.findAll(class_='tbcs')
        #详细车型url
        mouthcons2 = soup.findAll('div', class_='carbox')
        carurls=[]
        for m in mouthcons2:
            carurl =m.find('a').attrs['href']
            curl='http:'+carurl
            carurls.append(curl)
            # print('carurl=',carurl)




        fromurl = response.url
        crawldate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 将二维数组存入item
        itemArray = []
        # for r in itemlist:
        for i in range(len(itemlist)):
            r=itemlist[i]
            item = carpeizhiItem()
            for c in range(len(r)):
                item[item.snames[c]] = r[c]
            # print('item.len=',len(item))
            # print('item=', item)
            item['cartype'] = cartypelist[i]
            item['webname'] = webname
            item['fromurl'] = fromurl
            item['crawldate'] = crawldate
            item['carurl'] = carurls[i]
            item['pathtext'] = pathtext
            itemArray.append(item)


        print('cartypelist=',cartypelist)
        # print('itemArray=', itemArray[0])
        # for i in range(len(cartypelist)):

            # item = itemArray[i]
            # # print(i,cartypelist[i])
            # item.
            # item['cartype']=cartypelist[i]
            # item['webname']=webname
            # item['formurl']=formurl

            # yield item
            # print(item)

        #返回item
        for item in itemArray:
            # print(item)
            yield item



        # print('tcontent=',tcontent)
        # print('tcontent=',response.text)

    def listget(self,list, key, default=None):
        try:
            return list[key]
        except IndexError:
            return default
