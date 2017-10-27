# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from _md5 import md5

import happybase
import pymongo

from scrapy.conf import settings
import datetime
import random

from crawlAutohomeCarpeizhi.items import carpeizhiItem

class randomRowKey(object):
    # 生产唯一key
    def getRowKey(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
        randomNum = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum
class HBasePipeline(object):
    def __init__(self):
        self.host = settings['HBASE_HOST']
        self.table_name = settings['HBASE_TABLE']
        self.port = settings['HBASE_PORT']
        # self.connection = happybase.Connection(host=self.host,port=self.port,timeout=120000,transport='framed' protocol='compact')
        self.connection = happybase.Connection(host=self.host,port=self.port, timeout=None,autoconnect=False)
        # self.connection = happybase.Connection(host=self.host,port=self.port)
        # self.table = self.connection.table(self.table_name)




    def process_item(self, item, spider):
        # cl = dict(item)
        self.connection.open()
        table = self.connection.table(self.table_name)
        if isinstance(item, carpeizhiItem):
            # self.table.put('text', cl)
            print('进入pipline')
            randomrkey = randomRowKey()
            rowkey = randomrkey.getRowKey()

            zhidaoprice = item.get('zhidaoprice', '')
            butie = item.get('butie', '')
            cankaoprice = item.get('cankaoprice', '')
            changshang = item.get('changshang', '')
            jibie = item.get('jibie', '')
            shangshidate = item.get('shangshidate', '')
            changkg = item.get('changkg', '')
            jiegou = item.get('jiegou', '')
            maxspeed = item.get('maxspeed', '')
            guanfangjiasu = item.get('guanfangjiasu', '')
            shicejiasu = item.get('shicejiasu', '')
            shicezhidong = item.get('shicezhidong', '')
            shiceyouhao = item.get('shiceyouhao', '')
            zongheyouhao = item.get('zongheyouhao', '')
            shicejianxi = item.get('shicejianxi', '')
            carzhibao = item.get('carzhibao', '')
            changdu = item.get('changdu', '')
            kuangdu = item.get('kuangdu', '')
            gaodu = item.get('gaodu', '')
            zhouju = item.get('zhouju', '')
            qianlunju = item.get('qianlunju', '')
            houlunju = item.get('houlunju', '')
            minjianxi = item.get('minjianxi', '')
            carweight = item.get('carweight', '')
            chemen = item.get('chemen', '')
            zhuowei = item.get('zhuowei', '')
            youxiang = item.get('youxiang', '')
            xinglixiang = item.get('xinglixiang', '')
            fadongjinum = item.get('fadongjinum', '')
            pailiangml = item.get('pailiangml', '')
            pailiangl = item.get('pailiangl', '')
            jqxingshi = item.get('jqxingshi', '')
            qgplxingshi = item.get('qgplxingshi', '')
            qimen = item.get('qimen', '')
            mgqmnum = item.get('mgqmnum', '')
            yasuocom = item.get('yasuocom', '')
            pqjigou = item.get('pqjigou', '')
            gangjing = item.get('gangjing', '')
            xingcheng = item.get('xingcheng', '')
            maxmali = item.get('maxmali', '')
            maxgonglv = item.get('maxgonglv', '')
            maxzhuansu = item.get('maxzhuansu', '')
            maxniuju = item.get('maxniuju', '')
            maxniujuzhuan = item.get('maxniujuzhuan', '')
            fadongjijs = item.get('fadongjijs', '')
            rxingshi = item.get('rxingshi', '')
            rybiaohao = item.get('rybiaohao', '')
            gongyoufangshi = item.get('gongyoufangshi', '')
            ganggai = item.get('ganggai', '')
            gangti = item.get('gangti', '')
            huanbao = item.get('huanbao', '')
            jiancheng = item.get('jiancheng', '')
            dangwei = item.get('dangwei', '')
            biansxtype = item.get('biansxtype', '')
            qudong = item.get('qudong', '')
            qxuanjiatype = item.get('qxuanjiatype', '')
            hxuanjiatype = item.get('hxuanjiatype', '')
            chulitype = item.get('chulitype', '')
            chetijiegou = item.get('chetijiegou', '')
            qzhiqitype = item.get('qzhiqitype', '')
            hzhiqitype = item.get('hzhiqitype', '')
            zhucetype = item.get('zhucetype', '')
            qlunguige = item.get('qlunguige', '')
            hlunguige = item.get('hlunguige', '')
            beitaiguige = item.get('beitaiguige', '')
            safeqinang = item.get('safeqinang', '')
            ceqinang = item.get('ceqinang', '')
            headqinang = item.get('headqinang', '')
            xibuqinang = item.get('xibuqinang', '')
            taiyajiance = item.get('taiyajiance', '')
            lingtaiya = item.get('lingtaiya', '')
            safedaitishi = item.get('safedaitishi', '')
            erdongzhuoyi = item.get('erdongzhuoyi', '')
            abs = item.get('abs', '')
            zhidonglifenpei = item.get('zhidonglifenpei', '')
            shacefuzhu = item.get('shacefuzhu', '')
            qianyinliconsole = item.get('qianyinliconsole', '')
            carwendingconsole = item.get('carwendingconsole', '')
            bingxfuzhu = item.get('bingxfuzhu', '')
            cdplyjxitong = item.get('cdplyjxitong', '')
            shacxitong = item.get('shacxitong', '')
            yeshixitong = item.get('yeshixitong', '')
            pljstishi = item.get('pljstishi', '')
            qhzcleida = item.get('qhzcleida', '')
            daocyxiang = item.get('daocyxiang', '')
            shextou = item.get('shextou', '')
            dsxunhang = item.get('dsxunhang', '')
            zsyxunhang = item.get('zsyxunhang', '')
            zdbcruwei = item.get('zdbcruwei', '')
            fdjqiting = item.get('fdjqiting', '')
            spfuzhu = item.get('spfuzhu', '')
            zdzhuce = item.get('zdzhuce', '')
            dphuanjiang = item.get('dphuanjiang', '')
            kbxuanjia = item.get('kbxuanjia', '')
            kqxuanjia = item.get('kqxuanjia', '')
            dcgyxuanjia = item.get('dcgyxuanjia', '')
            kbzxiangbi = item.get('kbzxiangbi', '')
            qqxhchasuqi = item.get('qqxhchasuqi', '')
            zychasuqi = item.get('zychasuqi', '')
            hqxhchasuqi = item.get('hqxhchasuqi', '')
            ztzdzxxitong = item.get('ztzdzxxitong', '')
            diandtianchuang = item.get('diandtianchuang', '')
            quanjtianchuang = item.get('quanjtianchuang', '')
            ydwgtaojian = item.get('ydwgtaojian', '')
            lhjlunquan = item.get('lhjlunquan', '')
            diandxihemen = item.get('diandxihemen', '')
            cehuamen = item.get('cehuamen', '')
            diandhoubeix = item.get('diandhoubeix', '')
            gyhbeix = item.get('gyhbeix', '')
            cedxinglijia = item.get('cedxinglijia', '')
            fdjdianzifangd = item.get('fdjdianzifangd', '')
            ceneikongsuo = item.get('ceneikongsuo', '')
            ykyaosi = item.get('ykyaosi', '')
            wysqidxitong = item.get('wysqidxitong', '')
            wysjinrxitong = item.get('wysjinrxitong', '')
            ycqidfadongji = item.get('ycqidfadongji', '')
            zpfangxpan = item.get('zpfangxpan', '')
            fxptiaojie = item.get('fxptiaojie', '')
            fxpddtiaojie = item.get('fxpddtiaojie', '')
            dgnfangxpan = item.get('dgnfangxpan', '')
            fxphuandang = item.get('fxphuandang', '')
            fxpjiare = item.get('fxpjiare', '')
            fxpjiyi = item.get('fxpjiyi', '')
            xcdnxianshi = item.get('xcdnxianshi', '')
            qyjyibiaopan = item.get('qyjyibiaopan', '')
            hudxianshi = item.get('hudxianshi', '')
            nzxcjiluyi = item.get('nzxcjiluyi', '')
            zdjiangzao = item.get('zdjiangzao', '')
            sjwxchongdian = item.get('sjwxchongdian', '')
            zycaizhi = item.get('zycaizhi', '')
            ydfgzhuoyi = item.get('ydfgzhuoyi', '')
            zhygdtiaojie = item.get('zhygdtiaojie', '')
            ybzctiaojie = item.get('ybzctiaojie', '')
            jbzctiaojie = item.get('jbzctiaojie', '')
            zfjsddtiaojie = item.get('zfjsddtiaojie', '')
            dierpaikbeitiaojie = item.get('dierpaikbeitiaojie', '')
            dierpaizhyyidong = item.get('dierpaizhyyidong', '')
            hpaizhyddtiaojie = item.get('hpaizhyddtiaojie', '')
            fujiashitiaojie = item.get('fujiashitiaojie', '')
            ddzhyjiyi = item.get('ddzhyjiyi', '')
            qhpaizhyjiare = item.get('qhpaizhyjiare', '')
            qhpaizhytongfeng = item.get('qhpaizhytongfeng', '')
            qhpaizhyanmo = item.get('qhpaizhyanmo', '')
            dierpaizhy = item.get('dierpaizhy', '')
            disanpaizhy = item.get('disanpaizhy', '')
            hpaizhyfdxingshi = item.get('hpaizhyfdxingshi', '')
            qhzyfushou = item.get('qhzyfushou', '')
            houpaibeijia = item.get('houpaibeijia', '')
            kjiarezlbeijia = item.get('kjiarezlbeijia', '')
            gpsxitong = item.get('gpsxitong', '')
            dingweifuwu = item.get('dingweifuwu', '')
            zhongkongdaping = item.get('zhongkongdaping', '')
            dapingchicun = item.get('dapingchicun', '')
            fenpingxs = item.get('fenpingxs', '')
            lanyaphone = item.get('lanyaphone', '')
            shoujihlian = item.get('shoujihlian', '')
            chelianwang = item.get('chelianwang', '')
            chezaidianshi = item.get('chezaidianshi', '')
            hpaiyejping = item.get('hpaiyejping', '')
            dianyuan = item.get('dianyuan', '')
            waijieyinkou = item.get('waijieyinkou', '')
            cddvd = item.get('cddvd', '')
            ysqpingpai = item.get('ysqpingpai', '')
            ysqishuli = item.get('ysqishuli', '')
            jingdeng = item.get('jingdeng', '')
            yuangdeng = item.get('yuangdeng', '')
            ledchedeng = item.get('ledchedeng', '')
            zsyyjguang = item.get('zsyyjguang', '')
            zdtoudeng = item.get('zdtoudeng', '')
            zzfuzhudeng = item.get('zzfuzhudeng', '')
            zztoudeng = item.get('zztoudeng', '')
            qwdeng = item.get('qwdeng', '')
            dadengtj = item.get('dadengtj', '')
            dadengzz = item.get('dadengzz', '')
            cnfwdeng = item.get('cnfwdeng', '')
            ddchechuang = item.get('ddchechuang', '')
            ccyjsjiang = item.get('ccyjsjiang', '')
            ccfjsgongn = item.get('ccfjsgongn', '')
            gereboli = item.get('gereboli', '')
            hsjzztj = item.get('hsjzztj', '')
            hsjjre = item.get('hsjjre', '')
            nwhsjzdfxm = item.get('nwhsjzdfxm', '')
            lmtcnhsj = item.get('lmtcnhsj', '')
            hsjddzd = item.get('hsjddzd', '')
            hsjjy = item.get('hsjjy', '')
            hfdzyl = item.get('hfdzyl', '')
            hpczyl = item.get('hpczyl', '')
            hpcysbl = item.get('hpcysbl', '')
            zybhzj = item.get('zybhzj', '')
            hys = item.get('hys', '')
            gyys = item.get('gyys', '')
            ktkzfs = item.get('ktkzfs', '')
            hpdlkt = item.get('hpdlkt', '')
            hzcfk = item.get('hzcfk', '')
            wdfqkz = item.get('wdfqkz', '')
            cnkqtj = item.get('cnkqtj', '')
            czkqjhq = item.get('czkqjhq', '')
            czbx = item.get('czbx', '')
            wgyanse = item.get('wgyanse', '')
            nsyanse = item.get('nsyanse', '')
            cartype = item.get('cartype', '')
            webname = item.get('webname', '')
            fromurl = item.get('fromurl', '')
            crawldate = item.get('crawldate', '')
            crawldate = item.get('crawldate', '')
            carurl = item.get('carurl', '')
            pathtext = item.get('pathtext', '')
            table.put(md5(str(rowkey).encode('utf-8')).hexdigest(), {
                'cf1:zhidaoprice':zhidaoprice,
                'cf1:butie':butie,
                'cf1:cankaoprice':cankaoprice,
                'cf1:changshang':changshang,
                'cf1:jibie':jibie,
                'cf1:shangshidate':shangshidate,
                'cf1:changkg':changkg,
                'cf1:jiegou':jiegou,
                'cf1:maxspeed':maxspeed,
                'cf1:guanfangjiasu':guanfangjiasu,
                'cf1:shicejiasu':shicejiasu,
                'cf1:shicezhidong':shicezhidong,
                'cf1:shiceyouhao':shiceyouhao,
                'cf1:zongheyouhao':zongheyouhao,
                'cf1:shicejianxi':shicejianxi,
                'cf1:carzhibao':carzhibao,
                'cf1:changdu':changdu,
                'cf1:kuangdu':kuangdu,
                'cf1:gaodu':gaodu,
                'cf1:zhouju':zhouju,
                'cf1:qianlunju':qianlunju,
                'cf1:houlunju':houlunju,
                'cf1:minjianxi':minjianxi,
                'cf1:carweight':carweight,
                'cf1:chemen':chemen,
                'cf1:zhuowei':zhuowei,
                'cf1:youxiang':youxiang,
                'cf1:xinglixiang':xinglixiang,
                'cf1:fadongjinum':fadongjinum,
                'cf1:pailiangml':pailiangml,
                'cf1:pailiangl':pailiangl,
                'cf1:jqxingshi':jqxingshi,
                'cf1:qgplxingshi':qgplxingshi,
                'cf1:qimen':qimen,
                'cf1:mgqmnum':mgqmnum,
                'cf1:yasuocom':yasuocom,
                'cf1:pqjigou':pqjigou,
                'cf1:gangjing':gangjing,
                'cf1:xingcheng':xingcheng,
                'cf1:maxmali':maxmali,
                'cf1:maxgonglv':maxgonglv,
                'cf1:maxzhuansu':maxzhuansu,
                'cf1:maxniuju':maxniuju,
                'cf1:maxniujuzhuan':maxniujuzhuan,
                'cf1:fadongjijs':fadongjijs,
                'cf1:rxingshi':rxingshi,
                'cf1:rybiaohao':rybiaohao,
                'cf1:gongyoufangshi':gongyoufangshi,
                'cf1:ganggai':ganggai,
                'cf1:gangti':gangti,
                'cf1:huanbao':huanbao,
                'cf1:jiancheng':jiancheng,
                'cf1:dangwei':dangwei,
                'cf1:biansxtype':biansxtype,
                'cf1:qudong':qudong,
                'cf1:qxuanjiatype':qxuanjiatype,
                'cf1:hxuanjiatype':hxuanjiatype,
                'cf1:chulitype':chulitype,
                'cf1:chetijiegou':chetijiegou,
                'cf1:qzhiqitype':qzhiqitype,
                'cf1:hzhiqitype':hzhiqitype,
                'cf1:zhucetype':zhucetype,
                'cf1:qlunguige':qlunguige,
                'cf1:hlunguige':hlunguige,
                'cf1:beitaiguige':beitaiguige,
                'cf1:safeqinang':safeqinang,
                'cf1:ceqinang':ceqinang,
                'cf1:headqinang':headqinang,
                'cf1:xibuqinang':xibuqinang,
                'cf1:taiyajiance':taiyajiance,
                'cf1:lingtaiya':lingtaiya,
                'cf1:safedaitishi':safedaitishi,
                'cf1:erdongzhuoyi':erdongzhuoyi,
                'cf1:abs':abs,
                'cf1:zhidonglifenpei':zhidonglifenpei,
                'cf1:shacefuzhu':shacefuzhu,
                'cf1:qianyinliconsole':qianyinliconsole,
                'cf1:carwendingconsole':carwendingconsole,
                'cf1:bingxfuzhu':bingxfuzhu,
                'cf1:cdplyjxitong':cdplyjxitong,
                'cf1:shacxitong':shacxitong,
                'cf1:yeshixitong':yeshixitong,
                'cf1:pljstishi':pljstishi,
                'cf1:qhzcleida':qhzcleida,
                'cf1:daocyxiang':daocyxiang,
                'cf1:shextou':shextou,
                'cf1:dsxunhang':dsxunhang,
                'cf1:zsyxunhang':zsyxunhang,
                'cf1:zdbcruwei':zdbcruwei,
                'cf1:fdjqiting':fdjqiting,
                'cf1:spfuzhu':spfuzhu,
                'cf1:zdzhuce':zdzhuce,
                'cf1:dphuanjiang':dphuanjiang,
                'cf1:kbxuanjia':kbxuanjia,
                'cf1:kqxuanjia':kqxuanjia,
                'cf1:dcgyxuanjia':dcgyxuanjia,
                'cf1:kbzxiangbi':kbzxiangbi,
                'cf1:qqxhchasuqi':qqxhchasuqi,
                'cf1:zychasuqi':zychasuqi,
                'cf1:hqxhchasuqi':hqxhchasuqi,
                'cf1:ztzdzxxitong':ztzdzxxitong,
                'cf1:diandtianchuang':diandtianchuang,
                'cf1:quanjtianchuang':quanjtianchuang,
                'cf1:ydwgtaojian':ydwgtaojian,
                'cf1:lhjlunquan':lhjlunquan,
                'cf1:diandxihemen':diandxihemen,
                'cf1:cehuamen':cehuamen,
                'cf1:diandhoubeix':diandhoubeix,
                'cf1:gyhbeix':gyhbeix,
                'cf1:cedxinglijia':cedxinglijia,
                'cf1:fdjdianzifangd':fdjdianzifangd,
                'cf1:ceneikongsuo':ceneikongsuo,
                'cf1:ykyaosi':ykyaosi,
                'cf1:wysqidxitong':wysqidxitong,
                'cf1:wysjinrxitong':wysjinrxitong,
                'cf1:ycqidfadongji':ycqidfadongji,
                'cf1:zpfangxpan':zpfangxpan,
                'cf1:fxptiaojie':fxptiaojie,
                'cf1:fxpddtiaojie':fxpddtiaojie,
                'cf1:dgnfangxpan':dgnfangxpan,
                'cf1:fxphuandang':fxphuandang,
                'cf1:fxpjiare':fxpjiare,
                'cf1:fxpjiyi':fxpjiyi,
                'cf1:xcdnxianshi':xcdnxianshi,
                'cf1:qyjyibiaopan':qyjyibiaopan,
                'cf1:hudxianshi':hudxianshi,
                'cf1:nzxcjiluyi':nzxcjiluyi,
                'cf1:zdjiangzao':zdjiangzao,
                'cf1:sjwxchongdian':sjwxchongdian,
                'cf1:zycaizhi':zycaizhi,
                'cf1:ydfgzhuoyi':ydfgzhuoyi,
                'cf1:zhygdtiaojie':zhygdtiaojie,
                'cf1:ybzctiaojie':ybzctiaojie,
                'cf1:jbzctiaojie':jbzctiaojie,
                'cf1:zfjsddtiaojie':zfjsddtiaojie,
                'cf1:dierpaikbeitiaojie':dierpaikbeitiaojie,
                'cf1:dierpaizhyyidong':dierpaizhyyidong,
                'cf1:hpaizhyddtiaojie':hpaizhyddtiaojie,
                'cf1:fujiashitiaojie':fujiashitiaojie,
                'cf1:ddzhyjiyi':ddzhyjiyi,
                'cf1:qhpaizhyjiare':qhpaizhyjiare,
                'cf1:qhpaizhytongfeng':qhpaizhytongfeng,
                'cf1:qhpaizhyanmo':qhpaizhyanmo,
                'cf1:dierpaizhy':dierpaizhy,
                'cf1:disanpaizhy':disanpaizhy,
                'cf1:hpaizhyfdxingshi':hpaizhyfdxingshi,
                'cf1:qhzyfushou':qhzyfushou,
                'cf1:houpaibeijia':houpaibeijia,
                'cf1:kjiarezlbeijia':kjiarezlbeijia,
                'cf1:gpsxitong':gpsxitong,
                'cf1:dingweifuwu':dingweifuwu,
                'cf1:zhongkongdaping':zhongkongdaping,
                'cf1:dapingchicun':dapingchicun,
                'cf1:fenpingxs':fenpingxs,
                'cf1:lanyaphone':lanyaphone,
                'cf1:shoujihlian':shoujihlian,
                'cf1:chelianwang':chelianwang,
                'cf1:chezaidianshi':chezaidianshi,
                'cf1:hpaiyejping':hpaiyejping,
                'cf1:dianyuan':dianyuan,
                'cf1:waijieyinkou':waijieyinkou,
                'cf1:cddvd':cddvd,
                'cf1:ysqpingpai':ysqpingpai,
                'cf1:ysqishuli':ysqishuli,
                'cf1:jingdeng':jingdeng,
                'cf1:yuangdeng':yuangdeng,
                'cf1:ledchedeng':ledchedeng,
                'cf1:zsyyjguang':zsyyjguang,
                'cf1:zdtoudeng':zdtoudeng,
                'cf1:zzfuzhudeng':zzfuzhudeng,
                'cf1:zztoudeng':zztoudeng,
                'cf1:qwdeng':qwdeng,
                'cf1:dadengtj':dadengtj,
                'cf1:dadengzz':dadengzz,
                'cf1:cnfwdeng':cnfwdeng,
                'cf1:ddchechuang':ddchechuang,
                'cf1:ccyjsjiang':ccyjsjiang,
                'cf1:ccfjsgongn':ccfjsgongn,
                'cf1:gereboli':gereboli,
                'cf1:hsjzztj':hsjzztj,
                'cf1:hsjjre':hsjjre,
                'cf1:nwhsjzdfxm':nwhsjzdfxm,
                'cf1:lmtcnhsj':lmtcnhsj,
                'cf1:hsjddzd':hsjddzd,
                'cf1:hsjjy':hsjjy,
                'cf1:hfdzyl':hfdzyl,
                'cf1:hpczyl':hpczyl,
                'cf1:hpcysbl':hpcysbl,
                'cf1:zybhzj':zybhzj,
                'cf1:hys':hys,
                'cf1:gyys':gyys,
                'cf1:ktkzfs':ktkzfs,
                'cf1:hpdlkt':hpdlkt,
                'cf1:hzcfk':hzcfk,
                'cf1:wdfqkz':wdfqkz,
                'cf1:cnkqtj':cnkqtj,
                'cf1:czkqjhq':czkqjhq,
                'cf1:czbx':czbx,
                'cf1:wgyanse':wgyanse,
                'cf1:nsyanse':nsyanse,
                'cf1:cartype':cartype,
                'cf1:webname':webname,
                'cf1:fromurl':fromurl,
                'cf1:crawldate':crawldate,
                'cf1:carurl':carurl,
                'cf1:pathtext':pathtext
            })
        self.connection.close()
        return item

class CrawlautohomecarpeizhiPipeline(object):
    def process_item(self, item, spider):
        return item
