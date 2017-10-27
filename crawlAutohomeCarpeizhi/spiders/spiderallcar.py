# -*- coding: utf-8 -*-
import datetime

import scrapy
import time
from bs4 import BeautifulSoup

import logging

from crawlAutohomeCarpeizhi.items import carpeizhiItem

logger = logging.getLogger('SpiderarticleSpider')
class SpiderallcarSpider(scrapy.Spider):
    name = 'spiderallcar'
    # allowed_domains = ['car.autohome.com.cn']
    allowed_domains = ['www.autohome.com.cn','car.autohome.com.cn']
    start_urls = [
        'http://www.autohome.com.cn/a00/', #微型车
        'http://www.autohome.com.cn/a0/',#小型车
        ## 'http://www.autohome.com.cn/a/', #紧凑型车
        'http://www.autohome.com.cn/b/', #中型车
        'http://www.autohome.com.cn/d/', #大型车
        'http://www.autohome.com.cn/c/', #中大型车
        ## 'http://www.autohome.com.cn/suv/', #全部SUV
        'http://www.autohome.com.cn/mpv/', #mpv
        'http://www.autohome.com.cn/s/', #跑车
        'http://www.autohome.com.cn/p/', #皮卡
        'http://www.autohome.com.cn/mb/', #微面
        'http://www.autohome.com.cn/qk/', #轻客
                  ]

    def __init__(self, **kwargs):
        self.count = 0
        self.cartypelist= {'a00': '微型车', 'a0': '','a': '紧凑型车', 'b': '中型车','c': '中大型车', 'suv': '全部SUV','mpv': 'MPV', 's': '跑车','p': '皮卡', 'mb': '微面','qk': '轻客'
                            }

    def start_requests(self):
        for url in self.start_urls:
            self._wait()
            request = scrapy.Request(url=url, callback=self.parse)
            # request= scrapy.Request(url=url, callback=self.parse)
            request.meta['isjs'] = 'False'
            yield request

    def parse(self, response):
        # print('解析车型URL')
        logger.log(logging.INFO, '解析车型URL：%s' % response.url)
        soup = BeautifulSoup(response.text, 'lxml')
        uibox= soup.findAll('div',class_='uibox')
        ul= soup.findAll('ul',class_='rank-list-ul')
        for l in ul:
            h4=l.find('h4')
            lt = h4.get_text()
            lturl = h4.find('a').attrs['href']
            url=response.urljoin(lturl)
            # print(type(lturl))
            print(lt,url)


            request = scrapy.Request(url=url, callback=self.pzurlparse)
            request.meta['isjs'] = 'False'
            yield request

    def pzurlparse(self, response):
        # print('进入解析参数配置URL')
        logger.log(logging.INFO, '进入解析参数配置URL：%s' % response.url)
        soup = BeautifulSoup(response.text, 'lxml')
        navTop = soup.find(id='navTop')
        if navTop:
            alli= navTop.findAll('li',class_='nav-item')
            pzli=alli[1].find('a')
            if pzli:
                pzurl = pzli.attrs['href']
                # print('pzli=',pzurl)
                url='http:'+pzurl
                print('pzli=', url)
                self._wait()
                request = scrapy.Request(url=url, callback=self.pzcomparse)
                request.meta['isjs'] = 'True'
                yield request

    def pzcomparse(self, response):
        logger.log(logging.INFO, '当前参数配置URL：%s' % response.url)
        # tcontent=response.meta['tcontent']
        # 配置
        rowdict = response.meta['rowdict']
        # 车型
        cartypelist = response.meta['cartypelist']
        print('rowdict:', rowdict)
        print('rowdictlen:', len(rowdict))
        switem = carpeizhiItem()
        cardict = {}
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
        print('cararray长度：', len(cararray))
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


        # 获取页面信息
        webname = response.css('.subnav .subnav-title .subnav-title-name a::text').extract_first()
        # wgyanse = response.css('.color-ul *::text').extract_first()
        # wgyanse = response.css('.color-ul *::text').extract_first()
        soup = BeautifulSoup(response.text, 'lxml')
        #当前位置
        pathnav = soup.find('div', class_='path')
        pathtext=pathnav.get_text(strip=True)

        try:
            pathtext=pathtext.split('>')[1]
        except Exception :
            pathtext=''


        print('pathtext=',pathtext)

        #颜色
        colorul=soup.findAll('ul',class_='color-ul')
        for c in colorul:
            color = c.get_text(separator=' ', strip=True)
        #     print(color)
        # tbcs = soup.findAll(class_='tbcs')
        #详细车型url
        mouthcons2 = soup.findAll('div', class_='carbox')
        carurls = []
        for m in mouthcons2:
            carurl = m.find('a').attrs['href']
            curl = 'http:' + carurl
            carurls.append(curl)
            # print('carurl=',carurl)

        fromurl = response.url
        crawldate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 将二维数组存入item
        itemArray = []
        # for r in itemlist:
        for i in range(len(itemlist)):
            r = itemlist[i]
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

        print('cartypelist=', cartypelist)
        print('itemArray=', len(itemArray))
        # for i in range(len(cartypelist)):


        # 返回item
        for item in itemArray:
            # print(item)
            yield item



        # print('tcontent=',tcontent)
        # print('tcontent=',response.text)

        #返回item
        for item in itemArray:
            # print(item)
            yield item

    def _wait(self):
        for i in range(0, 3):
            print('.' * (i % 3 + 1))
            time.sleep(10)


