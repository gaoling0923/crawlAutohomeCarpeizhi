# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time

from bs4 import BeautifulSoup
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class IsJavaScriptMiddleware(object):

    # def __init__(self):
    #     self.browser = webdriver.PhantomJS()

    def process_request(self, request, spider):
        # conn = RedisClient();
        # proxy = conn.pop();
        # print('当前使用的IP:', proxy);
        # request.meta['proxy'] = "http://%s" % proxy
        # if spider.name in("spiderbbsdetail","crawlb30bbsdetail"):
        isjs = request.meta['isjs']
        print('isjs=', isjs)
        if isjs == 'True':
            print("execute PhantomJS spiderName", spider.name);
            print("PhantomJS is starting...")
            # browser = webdriver.PhantomJS() #指定使用的浏览器
            browser = webdriver.Chrome()
            # driver = webdriver.Firefox()
            time.sleep(1)
            # driver.implicitly_wait(30)  # seconds
            # wait = WebDriverWait(driver, 60)
            browser.get(request.url)
            print("访问:" + request.url)
            # 等待完成

            body = browser.page_source

            response = HtmlResponse(browser.current_url, body=body, encoding='utf-8', request=request)
            soup = BeautifulSoup(response.text, 'lxml')

            # request.meta.
            isjs = request.meta['isjs']
            content = ''
            print('isjs=%s' % isjs)
            if isjs == 'True':
                # print(body)
                ##有可能多个内容
                # mouthcons = soup.findAll('div', class_='mouth-item')
                mouthcons = soup.findAll(class_='tbcs')
                mouthcons2 = soup.findAll('div', class_='carbox')
                # print('mouthcons=', mouthcons)
                cartypelist = []
                rowdict = {}
                # 顶部操作部分
                for navcon in mouthcons2:
                    print('navcon=', navcon)
                    replace_content_s_list = navcon.findAll('span', attrs={"class": True})
                    print('replace_content_s_list2==', replace_content_s_list)
                    if len(replace_content_s_list) > 0:
                        listlen = len(replace_content_s_list) - 1
                        # 等待完成
                        first_class = replace_content_s_list[listlen].attrs['class'][0]
                        print('first_class==', first_class)
                        element_present = EC.presence_of_element_located((By.CLASS_NAME, first_class))
                        WebDriverWait(browser, 60).until(element_present)

                        # 字典，存储获取过的内容
                        span_class_dict = {}
                        for replace_span_s in replace_content_s_list:
                            # print('replace_span_s:', replace_span_s)
                            # print('replace_span_s:', replace_span_s)
                            cls = replace_span_s.attrs['class'][0]
                            # print('replace_span_s.attrs:', replace_span_s.attrs['class'])
                            print('cls2:', cls)
                            if cls not in span_class_dict:
                                # script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                    cls)
                                trans = browser.execute_script(script).strip('\"')
                                span_class_dict[cls] = trans.strip()
                                print('cls2=', cls)  # hs_kw59_optionpl
                                print('trans2=', trans.strip())  # css value
                            replace_span_s.replace_with(span_class_dict[cls])

                    cartype = navcon.find('div').get_text().strip()
                    print('navcon.get_text=', cartype)
                    # cartype=navcon.get_text().strip()
                    cartypelist.append(cartype if cartype else '')
                # 配置table span
                for mouthcon in mouthcons:
                    # print('mouthcon:',mouthcon)

                    # mouthcons = soup.find('tbody').findAll('tr')
                    koubei_content = mouthcon
                    # for mouthcon in mouthcons:
                    # type = mouthcon.find('i', class_='icon icon-zj').get_text()
                    # if type == '口碑':
                    # koubei_content = mouthcon
                    # 正文内容
                    # print('koubei_content=%s' % koubei_content)
                    # text_con = koubei_content.find('div')

                    # print('text_con=', text_con)
                    replace_content_s_list = koubei_content.findAll('span', attrs={"class": True})
                    print('replace_content_s_list==', replace_content_s_list)
                    if len(replace_content_s_list) > 1:
                        listlen = len(replace_content_s_list) - 1

                        # 等待完成
                        first_class = replace_content_s_list[listlen].attrs['class'][0]
                        # print('first_class==',first_class)
                        element_present = EC.presence_of_element_located((By.CLASS_NAME, first_class))
                        WebDriverWait(browser, 60).until(element_present)

                        # 字典，存储获取过的内容
                        span_class_dict = {}
                        for replace_span_s in replace_content_s_list:
                            # print('replace_span_s:', replace_span_s)
                            # print('replace_span_s:', replace_span_s)
                            cls = replace_span_s.attrs['class'][0]
                            # print('replace_span_s.attrs:', replace_span_s.attrs['class'])
                            # print('cls:', cls)
                            if cls not in span_class_dict:
                                try:
                                    # script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                    script = "return window.getComputedStyle(document.getElementsByClassName('%s')[1],'before').getPropertyValue('content')" % (
                                        cls)
                                    trans = browser.execute_script(script).strip('\"')
                                    span_class_dict[cls] = trans.strip()
                                    # print('cls=', cls)#hs_kw59_optionpl
                                    # print('trans=', trans.strip())  # css value
                                except WebDriverException:
                                    script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                        cls)
                                    trans = browser.execute_script(script).strip('\"')
                                    span_class_dict[cls] = trans.strip()

                            replace_span_s.replace_with(span_class_dict[cls])

                        # for i in koubei_content.findAll('style'):
                        #     print('style=',i)
                        # for i in koubei_content.findAll('script'):
                        #     print('script=', i)
                        # 清除style和script
                        [i.extract() for i in koubei_content.findAll('style')]
                        [i.extract() for i in koubei_content.findAll('script')]
                        # print('koubei_content=', koubei_content)

                    for cl in koubei_content.findAll('tr'):
                        # print('cl=',cl)
                        # for cl in koubei_content.findAll('tr'):
                        # 名称
                        ths = cl.find('th')
                        if ths:
                            content = content + ths.get_text().strip() + ','
                            th = ths.get_text().strip()

                            tds = cl.findAll('td')

                            # cells = ''
                            cells2 = []
                            for t in tds:
                                # print('td=',t)
                                # cells = cells + t.get_text().strip() + ','
                                # print('t.find(class_="color-ul")==', t.find('ul',class_="color-ul"))
                                if t.find(class_="color-ul"):
                                    coloruls = t.find('ul', class_="color-ul").findAll('span')
                                    coloras = t.find('ul', class_="color-ul").findAll('a')
                                    # print('coloruls:', coloruls)
                                    text = ''
                                    for c in coloras:
                                        text = text + ' ' + c.attrs['title']
                                    for c in coloruls:
                                        text = text + ' ' + c.attrs['title']
                                else:
                                    text = t.get_text().strip()

                                cells2.append(text if text else '')
                            # rowdict[th] = cells
                            rowdict[th] = cells2
                            # celllist.extend(content)

                    print('content:', content)
                print('celllist=', rowdict)
                # body2 = browser.page_source
                # response2 = HtmlResponse(browser.current_url, body=body2, encoding='utf-8', request=request)

                request.meta['tcontent'] = content
                request.meta['rowdict'] = rowdict
                request.meta['cartypelist'] = cartypelist

                # time.sleep(1)
                # browser.implicitly_wait(30)  # seconds
                # return HtmlResponse(browser.current_url, body=body, encoding='utf-8', request=request)
                browser.close()
                return response
        else:
            # print('')
            return

class JavaScriptMiddleware(object):

    # def __init__(self):
    #     self.browser = webdriver.PhantomJS()

    def process_request(self, request, spider):
        # conn = RedisClient();
        # proxy = conn.pop();
        # print('当前使用的IP:', proxy);
        # request.meta['proxy'] = "http://%s" % proxy
        # if spider.name in("spiderbbsdetail","crawlb30bbsdetail"):
        print("execute PhantomJS spiderName", spider.name);
        print("PhantomJS is starting...")
        # browser = webdriver.PhantomJS() #指定使用的浏览器
        browser =webdriver.Chrome()
        # driver = webdriver.Firefox()
        time.sleep(1)
        # driver.implicitly_wait(30)  # seconds
        # wait = WebDriverWait(driver, 60)
        browser.get(request.url)
        print("访问" + request.url)
        # 等待完成

        body = browser.page_source

        response = HtmlResponse(browser.current_url, body=body, encoding='utf-8', request=request)
        soup = BeautifulSoup(response.text, 'lxml')

        # request.meta.
        isjs = request.meta['isjs']
        content = ''
        print('isjs=%s' % isjs)
        if isjs == 'True':
            # print(body)
            ##有可能多个内容
            # mouthcons = soup.findAll('div', class_='mouth-item')
            mouthcons = soup.findAll(class_='tbcs')
            mouthcons2 = soup.findAll('div', class_='carbox')
            # print('mouthcons=', mouthcons)
            cartypelist=[]
            rowdict = {}
            #顶部操作部分
            for navcon in mouthcons2:
                print('navcon=',navcon)
                replace_content_s_list = navcon.findAll('span', attrs={"class": True})
                print('replace_content_s_list2==', replace_content_s_list)
                if len(replace_content_s_list) > 0:
                    listlen = len(replace_content_s_list) - 1
                    # 等待完成
                    first_class = replace_content_s_list[listlen].attrs['class'][0]
                    print('first_class==',first_class)
                    element_present = EC.presence_of_element_located((By.CLASS_NAME, first_class))
                    WebDriverWait(browser, 60).until(element_present)

                    # 字典，存储获取过的内容
                    span_class_dict = {}
                    for replace_span_s in replace_content_s_list:
                        # print('replace_span_s:', replace_span_s)
                        # print('replace_span_s:', replace_span_s)
                        cls = replace_span_s.attrs['class'][0]
                        # print('replace_span_s.attrs:', replace_span_s.attrs['class'])
                        print('cls2:', cls)
                        if cls not in span_class_dict:
                            # script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                            script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                cls)
                            trans = browser.execute_script(script).strip('\"')
                            span_class_dict[cls] = trans.strip()
                            print('cls2=', cls)#hs_kw59_optionpl
                            print('trans2=', trans.strip())  # css value
                        replace_span_s.replace_with(span_class_dict[cls])

                cartype = navcon.find('div').get_text().strip()
                print('navcon.get_text=',cartype)
                # cartype=navcon.get_text().strip()
                cartypelist.append(cartype if cartype else '')
            #配置table span
            for mouthcon in mouthcons:
                # print('mouthcon:',mouthcon)

                # mouthcons = soup.find('tbody').findAll('tr')
                koubei_content = mouthcon
                # for mouthcon in mouthcons:
                # type = mouthcon.find('i', class_='icon icon-zj').get_text()
                # if type == '口碑':
                # koubei_content = mouthcon
                # 正文内容
                # print('koubei_content=%s' % koubei_content)
                # text_con = koubei_content.find('div')

                # print('text_con=', text_con)
                replace_content_s_list = koubei_content.findAll('span', attrs={"class": True})
                print('replace_content_s_list==', replace_content_s_list)
                if len(replace_content_s_list) > 1:
                    listlen = len(replace_content_s_list) - 1

                    # 等待完成
                    first_class = replace_content_s_list[listlen].attrs['class'][0]
                    # print('first_class==',first_class)
                    element_present = EC.presence_of_element_located((By.CLASS_NAME, first_class))
                    WebDriverWait(browser, 60).until(element_present)

                    # 字典，存储获取过的内容
                    span_class_dict = {}
                    for replace_span_s in replace_content_s_list:
                        # print('replace_span_s:', replace_span_s)
                        # print('replace_span_s:', replace_span_s)
                        cls = replace_span_s.attrs['class'][0]
                        # print('replace_span_s.attrs:', replace_span_s.attrs['class'])
                        # print('cls:', cls)
                        if cls not in span_class_dict:
                            try:
                                # script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                script = "return window.getComputedStyle(document.getElementsByClassName('%s')[1],'before').getPropertyValue('content')" % (
                                    cls)
                                trans = browser.execute_script(script).strip('\"')
                                span_class_dict[cls] = trans.strip()
                                # print('cls=', cls)#hs_kw59_optionpl
                                # print('trans=', trans.strip())  # css value
                            except WebDriverException:
                                script = "return window.getComputedStyle(document.getElementsByClassName('%s')[0],'before').getPropertyValue('content')" % (
                                    cls)
                                trans = browser.execute_script(script).strip('\"')
                                span_class_dict[cls] = trans.strip()

                        replace_span_s.replace_with(span_class_dict[cls])

                    # for i in koubei_content.findAll('style'):
                    #     print('style=',i)
                    # for i in koubei_content.findAll('script'):
                    #     print('script=', i)
                    # 清除style和script
                    [i.extract() for i in koubei_content.findAll('style')]
                    [i.extract() for i in koubei_content.findAll('script')]
                    # print('koubei_content=', koubei_content)

                for cl in koubei_content.findAll('tr'):
                    # print('cl=',cl)
                # for cl in koubei_content.findAll('tr'):
                    # 名称
                    ths = cl.find('th')
                    if ths:
                        content = content + ths.get_text().strip() + ','
                        th = ths.get_text().strip()

                        tds = cl.findAll('td')

                        # cells = ''
                        cells2 = []
                        for t in tds:
                            # print('td=',t)
                            # cells = cells + t.get_text().strip() + ','
                            # print('t.find(class_="color-ul")==', t.find('ul',class_="color-ul"))
                            if t.find(class_="color-ul"):
                                coloruls = t.find('ul',class_="color-ul").findAll('span')
                                coloras = t.find('ul',class_="color-ul").findAll('a')
                                # print('coloruls:', coloruls)
                                text = ''
                                for c in coloras:
                                    text = text + ' ' + c.attrs['title']
                                for c in coloruls:
                                    text = text + ' ' + c.attrs['title']
                            else:
                                text = t.get_text().strip()

                            cells2.append(text if text else '')
                        # rowdict[th] = cells
                        rowdict[th] = cells2
                        # celllist.extend(content)

                print('content:', content)
            print('celllist=', rowdict)
            # body2 = browser.page_source
            # response2 = HtmlResponse(browser.current_url, body=body2, encoding='utf-8', request=request)

            request.meta['tcontent'] = content
            request.meta['rowdict'] = rowdict
            request.meta['cartypelist'] = cartypelist


            # time.sleep(1)
            # browser.implicitly_wait(30)  # seconds
            # return HtmlResponse(browser.current_url, body=body, encoding='utf-8', request=request)
            browser.close()
            return response
        else:
            return


class CrawlautohomecarpeizhiSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
