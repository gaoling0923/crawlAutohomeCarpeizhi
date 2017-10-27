# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class carpeizhiItem(scrapy.Item):

    snames=[
        'zhidaoprice',
        'butie',
        'cankaoprice',
        'changshang',
        'jibie',
        'shangshidate',
        'changkg',
        'jiegou',
        'maxspeed',
        'guanfangjiasu',
        'shicejiasu',
        'shicezhidong',
        'shiceyouhao',
        'zongheyouhao',
        'shicejianxi',
        'carzhibao',
        'changdu',
        'kuangdu',
        'gaodu',
        'zhouju',
        'qianlunju',
        'houlunju',
        'minjianxi',
        'carweight',
        # 'carshengtype',
        'chemen',
        'zhuowei',
        'youxiang',
        'xinglixiang',
        'fadongjinum',
        'pailiangml',
        'pailiangl',
        'jqxingshi',
        'qgplxingshi',
        'qimen',
        'mgqmnum',
        'yasuocom',
        'pqjigou',
        'gangjing',
        'xingcheng',
        'maxmali',
        'maxgonglv',
        'maxzhuansu',
        'maxniuju',
        'maxniujuzhuan',
        'fadongjijs',
        'rxingshi',
        'rybiaohao',
        'gongyoufangshi',
        'ganggai',
        'gangti',
        'huanbao',
        'jiancheng',
        'dangwei',
        'biansxtype',
        'qudong',
        'qxuanjiatype',
        'hxuanjiatype',
        'chulitype',
        'chetijiegou',
        'qzhiqitype',
        'hzhiqitype',
        'zhucetype',
        'qlunguige',
        'hlunguige',
        'beitaiguige',
        'safeqinang',
        'ceqinang',
        'headqinang',
        'xibuqinang',
        'taiyajiance',
        'lingtaiya',
        'safedaitishi',
        'erdongzhuoyi',
        'abs',
        'zhidonglifenpei',
        'shacefuzhu',
        'qianyinliconsole',
        'carwendingconsole',
        'bingxfuzhu',
        'cdplyjxitong',
        'shacxitong',
        'yeshixitong',
        'pljstishi',
        'qhzcleida',
        'daocyxiang',
        'shextou',
        'dsxunhang',
        'zsyxunhang',
        'zdbcruwei',
        'fdjqiting',
        'spfuzhu',
        'zdzhuce',
        'dphuanjiang',
        'kbxuanjia',
        'kqxuanjia',
        'dcgyxuanjia',
        'kbzxiangbi',
        'qqxhchasuqi',
        'zychasuqi',
        'hqxhchasuqi',
        'ztzdzxxitong',
        'diandtianchuang',
        'quanjtianchuang',
        'ydwgtaojian',
        'lhjlunquan',
        'diandxihemen',
        'cehuamen',
        'diandhoubeix',
        'gyhbeix',
        'cedxinglijia',
        'fdjdianzifangd',
        'ceneikongsuo',
        'ykyaosi',
        'wysqidxitong',
        'wysjinrxitong',
        'ycqidfadongji',
        'zpfangxpan',
        'fxptiaojie',
        'fxpddtiaojie',
        'dgnfangxpan',
        'fxphuandang',
        'fxpjiare',
        'fxpjiyi',
        'xcdnxianshi',
        'qyjyibiaopan',
        'hudxianshi',
        'nzxcjiluyi',
        'zdjiangzao',
        'sjwxchongdian',
        'zycaizhi',
        'ydfgzhuoyi',
        'zhygdtiaojie',
        'ybzctiaojie',
        'jbzctiaojie',
        'zfjsddtiaojie',
        'dierpaikbeitiaojie',
        'dierpaizhyyidong',
        'hpaizhyddtiaojie',
        'fujiashitiaojie',
        'ddzhyjiyi',
        'qhpaizhyjiare',
        'qhpaizhytongfeng',
        'qhpaizhyanmo',
        'dierpaizhy',
        'disanpaizhy',
        'hpaizhyfdxingshi',
        'qhzyfushou',
        'houpaibeijia',
        'kjiarezlbeijia',
        'gpsxitong',
        'dingweifuwu',
        'zhongkongdaping',
        'dapingchicun',
        'fenpingxs',
        'lanyaphone',
        'shoujihlian',
        'chelianwang',
        'chezaidianshi',
        'hpaiyejping',
        'dianyuan',
        'waijieyinkou',
        'cddvd',
        'ysqpingpai',
        'ysqishuli',
        'jingdeng',
        'yuangdeng',
        'ledchedeng',
        'zsyyjguang',
        'zdtoudeng',
        'zzfuzhudeng',
        'zztoudeng',
        'qwdeng',
        'dadengtj',
        'dadengzz',
        'cnfwdeng',
        'ddchechuang',
        'ccyjsjiang',
        'ccfjsgongn',
        'gereboli',
        'hsjzztj',
        'hsjjre',
        'nwhsjzdfxm',
        'lmtcnhsj',
        'hsjddzd',
        'hsjjy',
        'hfdzyl',
        'hpczyl',
        'hpcysbl',
        'zybhzj',
        'hys',
        'gyys',
        'ktkzfs',
        'hpdlkt',
        'hzcfk',
        'wdfqkz',
        'cnkqtj',
        'czkqjhq',
        'czbx',
        'wgyanse',
        'nsyanse'
        ]
    switcher={
        '厂商指导价':'zhidaoprice',
        '国家/地方补贴':'butie',
        '经销商参考价':'cankaoprice',
        '厂商':'changshang',
        '级别':'jibie',
        '上市时间':'shangshidate',
        '长*宽*高(mm)':'changkg',
        '车身结构':'jiegou',#车身结构
        '最高车速(km/h)':'maxspeed',
        '官方0-100km/h加速(s)':'guanfangjiasu',
        '实测0-100km/h加速(s)':'shicejiasu',
        '实测100-0km/h制动(m)':'shicezhidong',
        '实测油耗(L/100km)':'shiceyouhao',
        '工信部综合油耗(L/100km)':'zongheyouhao',
        '实测离地间隙(mm)':'shicejianxi',
        '整车质保':'carzhibao',
        '长度(mm)':'changdu',
        '宽度(mm)':'kuangdu',
        '高度(mm)':'gaodu',
        '轴距(mm)':'zhouju',
        '前轮距(mm)':'qianlunju',
        '后轮距(mm)':'houlunju',
        '最小离地间隙(mm)':'minjianxi',
        '整备质量(kg)':'carweight',
        # '车身结构2':'carshengtype',#车身结构2
        '车门数(个)':'chemen',
        '座位数(个)':'zhuowei',
        '油箱容积(L)':'youxiang',
        '行李厢容积(L)':'xinglixiang',
        '发动机型号':'fadongjinum',
        '排量(mL)':'pailiangml',
        '排量(L)':'pailiangl',
        '进气形式':'jqxingshi',
        '气缸排列形式':'qgplxingshi',
        '气缸数(个)':'qimen',
        '每缸气门数(个)':'mgqmnum',
        '压缩比':'yasuocom',
        '配气机构':'pqjigou',
        '缸径(mm)':'gangjing',
        '行程(mm)':'xingcheng',
        '最大马力(Ps)':'maxmali',
        '最大功率(kW)':'maxgonglv',
        '最大功率转速(rpm)':'maxzhuansu',
        '最大扭矩(N·m)':'maxniuju',
        '最大扭矩转速(rpm)':'maxniujuzhuan',
        '发动机特有技术':'fadongjijs',
        '燃料形式':'rxingshi',
        '燃油标号':'rybiaohao',
        '供油方式':'gongyoufangshi',
        '缸盖材料':'ganggai',
        '缸体材料':'gangti',
        '环保标准':'huanbao',
        '简称':'jiancheng',
        '挡位个数':'dangwei',
        '变速箱类型':'biansxtype',
        '驱动方式':'qudong',
        '前悬架类型':'qxuanjiatype',
        '后悬架类型':'hxuanjiatype',
        '助力类型':'chulitype',
        '车体结构':'chetijiegou',
        '前制动器类型':'qzhiqitype',
        '后制动器类型':'hzhiqitype',
        '驻车制动类型':'zhucetype',
        '前轮胎规格':'qlunguige',
        '后轮胎规格':'hlunguige',
        '备胎规格':'beitaiguige',
        '主/副驾驶座安全气囊':'safeqinang',
        '前/后排侧气囊':'ceqinang',
        '前/后排头部气囊(气帘)':'headqinang',
        '膝部气囊':'xibuqinang',
        '胎压监测装置':'taiyajiance',
        '零胎压继续行驶':'lingtaiya',
        '安全带未系提示':'safedaitishi',
        'ISOFIX儿童座椅接口':'erdongzhuoyi',
        'ABS防抱死':'abs',
        '制动力分配(EBD/CBC等)':'zhidonglifenpei',
        '刹车辅助(EBA/BAS/BA等)':'shacefuzhu',
        '牵引力控制(ASR/TCS/TRC等)':'qianyinliconsole',
        '车身稳定控制(ESC/ESP/DSC等)':'carwendingconsole',
        '并线辅助':'bingxfuzhu',
        '车道偏离预警系统':'cdplyjxitong',
        '主动刹车/主动安全系统':'shacxitong',
        '夜视系统':'yeshixitong',
        '疲劳驾驶提示':'pljstishi',
        '前/后驻车雷达':'qhzcleida',
        '倒车视频影像':'daocyxiang',
        '全景摄像头':'shextou',
        '定速巡航':'dsxunhang',
        '自适应巡航':'zsyxunhang',
        '自动泊车入位':'zdbcruwei',
        '发动机启停技术':'fdjqiting',
        '上坡辅助':'spfuzhu',
        '自动驻车':'zdzhuce',
        '陡坡缓降':'dphuanjiang',
        '可变悬架':'kbxuanjia',
        '空气悬架':'kqxuanjia',
        '电磁感应悬架':'dcgyxuanjia',
        '可变转向比':'kbzxiangbi',
        '前桥限滑差速器/差速锁':'qqxhchasuqi',
        '中央差速器锁止功能':'zychasuqi',
        '后桥限滑差速器/差速锁':'hqxhchasuqi',
        '整体主动转向系统':'ztzdzxxitong',
        '电动天窗':'diandtianchuang',
        '全景天窗':'quanjtianchuang',
        '运动外观套件':'ydwgtaojian',
        '铝合金轮圈':'lhjlunquan',
        '电动吸合门':'diandxihemen',
        '侧滑门':'cehuamen',
        '电动后备厢':'diandhoubeix',
        '感应后备厢':'gyhbeix',
        '车顶行李架':'cedxinglijia',
        '发动机电子防盗':'fdjdianzifangd',
        '车内中控锁':'ceneikongsuo',
        '遥控钥匙':'ykyaosi',
        '无钥匙启动系统':'wysqidxitong',
        '无钥匙进入系统':'wysjinrxitong',
        '远程启动发动机':'ycqidfadongji',
        '真皮方向盘':'zpfangxpan',
        '方向盘调节':'fxptiaojie',
        '方向盘电动调节':'fxpddtiaojie',
        '多功能方向盘':'dgnfangxpan',
        '方向盘换挡':'fxphuandang',
        '方向盘加热':'fxpjiare',
        '方向盘记忆':'fxpjiyi',
        '行车电脑显示屏':'xcdnxianshi',
        '全液晶仪表盘':'qyjyibiaopan',
        'HUD抬头数字显示':'hudxianshi',
        '内置行车记录仪':'nzxcjiluyi',
        '主动降噪':'zdjiangzao',
        '手机无线充电':'sjwxchongdian',
        '座椅材质':'zycaizhi',
        '运动风格座椅':'ydfgzhuoyi',
        '座椅高低调节':'zhygdtiaojie',
        '腰部支撑调节':'ybzctiaojie',
        '肩部支撑调节':'jbzctiaojie',
        '主/副驾驶座电动调节':'zfjsddtiaojie',
        '第二排靠背角度调节':'dierpaikbeitiaojie',
        '第二排座椅移动':'dierpaizhyyidong',
        '后排座椅电动调节':'hpaizhyddtiaojie',
        '副驾驶位后排可调节按钮':'fujiashitiaojie',
        '电动座椅记忆':'ddzhyjiyi',
        '前/后排座椅加热':'qhpaizhyjiare',
        '前/后排座椅通风':'qhpaizhytongfeng',
        '前/后排座椅按摩':'qhpaizhyanmo',
        '第二排独立座椅':'dierpaizhy',
        '第三排座椅':'disanpaizhy',
        '后排座椅放倒方式':'hpaizhyfdxingshi',
        '前/后中央扶手':'qhzyfushou',
        '后排杯架':'houpaibeijia',
        '可加热/制冷杯架':'kjiarezlbeijia',
        'GPS导航系统':'gpsxitong',
        '定位互动服务':'dingweifuwu',
        '中控台彩色大屏':'zhongkongdaping',
        '中控台彩色大屏尺寸':'dapingchicun',
        '中控液晶屏分屏显示':'fenpingxs',
        '蓝牙/车载电话':'lanyaphone',
        '手机互联/映射':'shoujihlian',
        '车联网':'chelianwang',
        '车载电视':'chezaidianshi',
        '后排液晶屏':'hpaiyejping',
        '220V/230V电源':'dianyuan',
        '外接音源接口':'waijieyinkou',
        'CD/DVD':'cddvd',
        '扬声器品牌':'ysqpingpai',
        '扬声器数量':'ysqishuli',
        '近光灯':'jingdeng',
        '远光灯':'yuangdeng',
        'LED日间行车灯':'ledchedeng',
        '自适应远近光':'zsyyjguang',
        '自动头灯':'zdtoudeng',
        '转向辅助灯':'zzfuzhudeng',
        '转向头灯':'zztoudeng',
        '前雾灯':'qwdeng',
        '大灯高度可调':'dadengtj',
        '大灯清洗装置':'dadengzz',
        '车内氛围灯':'cnfwdeng',
        '前/后电动车窗':'ddchechuang',
        '车窗一键升降':'ccyjsjiang',
        '车窗防夹手功能':'ccfjsgongn',
        '防紫外线/隔热玻璃':'gereboli',
        '后视镜电动调节':'hsjzztj',
        '后视镜加热':'hsjjre',
        '内/外后视镜自动防眩目':'nwhsjzdfxm',
        '流媒体车内后视镜':'lmtcnhsj',
        '后视镜电动折叠':'hsjddzd',
        '后视镜记忆':'hsjjy',
        '后风挡遮阳帘':'hfdzyl',
        '后排侧遮阳帘':'hpczyl',
        '后排侧隐私玻璃':'hpcysbl',
        '遮阳板化妆镜':'zybhzj',
        '后雨刷':'hys',
        '感应雨刷':'gyys',
        '空调控制方式':'ktkzfs',
        '后排独立空调':'hpdlkt',
        '后座出风口':'hzcfk',
        '温度分区控制':'wdfqkz',
        '车内空气调节/花粉过滤':'cnkqtj',
        '车载空气净化器':'czkqjhq',
        '车载冰箱':'czbx',
        '外观颜色':'wgyanse',
        '内饰颜色':'nsyanse'

    }
    zhidaoprice = scrapy.Field()
    butie = scrapy.Field()
    cankaoprice = scrapy.Field()
    changshang = scrapy.Field()
    jibie = scrapy.Field()
    shangshidate = scrapy.Field()
    changkg = scrapy.Field()
    jiegou = scrapy.Field()
    maxspeed = scrapy.Field()
    guanfangjiasu = scrapy.Field()
    shicejiasu = scrapy.Field()
    shicezhidong = scrapy.Field()
    shiceyouhao = scrapy.Field()
    zongheyouhao = scrapy.Field()
    shicejianxi = scrapy.Field()
    carzhibao = scrapy.Field()
    changdu = scrapy.Field()
    kuangdu = scrapy.Field()
    gaodu = scrapy.Field()
    zhouju = scrapy.Field()
    qianlunju = scrapy.Field()
    houlunju = scrapy.Field()
    minjianxi = scrapy.Field()
    carweight = scrapy.Field()
    carjiegou = scrapy.Field()
    chemen = scrapy.Field()
    zhuowei = scrapy.Field()
    youxiang = scrapy.Field()
    xinglixiang = scrapy.Field()
    fadongjinum = scrapy.Field()
    pailiangml = scrapy.Field()
    pailiangl = scrapy.Field()
    jqxingshi = scrapy.Field()
    qgplxingshi = scrapy.Field()
    qimen = scrapy.Field()
    mgqmnum = scrapy.Field()
    yasuocom = scrapy.Field()
    pqjigou = scrapy.Field()
    gangjing = scrapy.Field()
    xingcheng = scrapy.Field()
    maxmali = scrapy.Field()
    maxgonglv = scrapy.Field()
    maxzhuansu = scrapy.Field()
    maxniuju = scrapy.Field()
    maxniujuzhuan = scrapy.Field()
    fadongjijs = scrapy.Field()
    rxingshi = scrapy.Field()
    rybiaohao = scrapy.Field()
    gongyoufangshi = scrapy.Field()
    ganggai = scrapy.Field()
    gangti = scrapy.Field()
    huanbao = scrapy.Field()
    jiancheng = scrapy.Field()
    dangwei = scrapy.Field()
    biansxtype = scrapy.Field()
    qudong = scrapy.Field()
    qxuanjiatype = scrapy.Field()
    hxuanjiatype = scrapy.Field()
    chulitype = scrapy.Field()
    chetijiegou = scrapy.Field()
    qzhiqitype = scrapy.Field()
    hzhiqitype = scrapy.Field()
    zhucetype = scrapy.Field()
    qlunguige = scrapy.Field()
    hlunguige = scrapy.Field()
    beitaiguige = scrapy.Field()
    safeqinang = scrapy.Field()
    ceqinang = scrapy.Field()
    headqinang = scrapy.Field()
    xibuqinang = scrapy.Field()
    taiyajiance = scrapy.Field()
    lingtaiya = scrapy.Field()
    safedaitishi = scrapy.Field()
    erdongzhuoyi = scrapy.Field()
    abs = scrapy.Field()
    zhidonglifenpei = scrapy.Field()
    shacefuzhu = scrapy.Field()
    qianyinliconsole = scrapy.Field()
    carwendingconsole = scrapy.Field()
    bingxfuzhu = scrapy.Field()
    cdplyjxitong = scrapy.Field()
    shacxitong = scrapy.Field()
    yeshixitong = scrapy.Field()
    pljstishi = scrapy.Field()
    qhzcleida = scrapy.Field()
    daocyxiang = scrapy.Field()
    shextou = scrapy.Field()
    dsxunhang = scrapy.Field()
    zsyxunhang = scrapy.Field()
    zdbcruwei = scrapy.Field()
    fdjqiting = scrapy.Field()
    spfuzhu = scrapy.Field()
    zdzhuce = scrapy.Field()
    dphuanjiang = scrapy.Field()
    kbxuanjia = scrapy.Field()
    kqxuanjia = scrapy.Field()
    dcgyxuanjia = scrapy.Field()
    kbzxiangbi = scrapy.Field()
    qqxhchasuqi = scrapy.Field()
    zychasuqi = scrapy.Field()
    hqxhchasuqi = scrapy.Field()
    ztzdzxxitong = scrapy.Field()
    diandtianchuang = scrapy.Field()
    quanjtianchuang = scrapy.Field()
    ydwgtaojian = scrapy.Field()
    lhjlunquan = scrapy.Field()
    diandxihemen = scrapy.Field()
    cehuamen = scrapy.Field()
    diandhoubeix = scrapy.Field()
    gyhbeix = scrapy.Field()
    cedxinglijia = scrapy.Field()
    fdjdianzifangd = scrapy.Field()
    ceneikongsuo = scrapy.Field()
    ykyaosi = scrapy.Field()
    wysqidxitong = scrapy.Field()
    wysjinrxitong = scrapy.Field()
    ycqidfadongji = scrapy.Field()
    zpfangxpan = scrapy.Field()
    fxptiaojie = scrapy.Field()
    fxpddtiaojie = scrapy.Field()
    dgnfangxpan = scrapy.Field()
    fxphuandang = scrapy.Field()
    fxpjiare = scrapy.Field()
    fxpjiyi = scrapy.Field()
    xcdnxianshi = scrapy.Field()
    qyjyibiaopan = scrapy.Field()
    hudxianshi = scrapy.Field()
    nzxcjiluyi = scrapy.Field()
    zdjiangzao = scrapy.Field()
    sjwxchongdian = scrapy.Field()
    zycaizhi = scrapy.Field()
    ydfgzhuoyi = scrapy.Field()
    zhygdtiaojie = scrapy.Field()
    ybzctiaojie = scrapy.Field()
    jbzctiaojie = scrapy.Field()
    zfjsddtiaojie = scrapy.Field()
    dierpaikbeitiaojie = scrapy.Field()
    dierpaizhyyidong = scrapy.Field()
    hpaizhyddtiaojie = scrapy.Field()
    fujiashitiaojie = scrapy.Field()
    ddzhyjiyi = scrapy.Field()
    qhpaizhyjiare = scrapy.Field()
    qhpaizhytongfeng = scrapy.Field()
    qhpaizhyanmo = scrapy.Field()
    dierpaizhy = scrapy.Field()
    disanpaizhy = scrapy.Field()
    hpaizhyfdxingshi = scrapy.Field()
    qhzyfushou = scrapy.Field()
    houpaibeijia = scrapy.Field()
    kjiarezlbeijia = scrapy.Field()
    gpsxitong = scrapy.Field()
    dingweifuwu = scrapy.Field()
    zhongkongdaping = scrapy.Field()
    dapingchicun = scrapy.Field()
    fenpingxs = scrapy.Field()
    lanyaphone = scrapy.Field()
    shoujihlian = scrapy.Field()
    chelianwang = scrapy.Field()
    chezaidianshi = scrapy.Field()
    hpaiyejping = scrapy.Field()
    dianyuan = scrapy.Field()
    waijieyinkou = scrapy.Field()
    cddvd = scrapy.Field()
    ysqpingpai = scrapy.Field()
    ysqishuli = scrapy.Field()
    jingdeng = scrapy.Field()
    yuangdeng = scrapy.Field()
    ledchedeng = scrapy.Field()
    zsyyjguang = scrapy.Field()
    zdtoudeng = scrapy.Field()
    zzfuzhudeng = scrapy.Field()
    zztoudeng = scrapy.Field()
    qwdeng = scrapy.Field()
    dadengtj = scrapy.Field()
    dadengzz = scrapy.Field()
    cnfwdeng = scrapy.Field()
    ddchechuang = scrapy.Field()
    ccyjsjiang = scrapy.Field()
    ccfjsgongn = scrapy.Field()
    gereboli = scrapy.Field()
    hsjzztj = scrapy.Field()
    hsjjre = scrapy.Field()
    nwhsjzdfxm = scrapy.Field()
    lmtcnhsj = scrapy.Field()
    hsjddzd = scrapy.Field()
    hsjjy = scrapy.Field()
    hfdzyl = scrapy.Field()
    hpczyl = scrapy.Field()
    hpcysbl = scrapy.Field()
    zybhzj = scrapy.Field()
    hys = scrapy.Field()
    gyys = scrapy.Field()
    ktkzfs = scrapy.Field()
    hpdlkt = scrapy.Field()
    hzcfk = scrapy.Field()
    wdfqkz = scrapy.Field()
    cnkqtj = scrapy.Field()
    czkqjhq = scrapy.Field()
    czbx = scrapy.Field()
    wgyanse = scrapy.Field()
    nsyanse = scrapy.Field()
    cartype=scrapy.Field()
    webname=scrapy.Field()
    fromurl = scrapy.Field()
    crawldate = scrapy.Field()
    carurl = scrapy.Field()
    pathtext = scrapy.Field()


class CrawlautohomecarpeizhiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
