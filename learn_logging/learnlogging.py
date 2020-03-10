#尽量听懂，听不懂，后续会给出标准解决方案
#不要把模块命名为logging，会与系统自带的冲突
#日子的等级debug-info-warning-error-critical/fatal
#日志收集器logger    默认的日志收集器 rootlogger
import logging
#1.自定义一个日志收集器并且设置级别getlogger
my_logger=logging.getLogger('python14')
my_logger.setLevel('DEBUG')
#2.指定输出渠道还要设置级别 StreamHandler(控制台) 、FileHandler（指定文件）
#输出到控制台
formatter=logging.Formatter( '%(asctime)s-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')
#根据自己需要设置格式，顺序不限制，可以用[]括起来，
ch=logging.StreamHandler()
ch.setLevel('INFO')
ch.setFormatter(formatter)  #设置日志格式，有很多种格式，根据需要网上找
#输出到指定文件
fh=logging.FileHandler('test.log',encoding='utf-8') #文件不存在时自动生成
fh.setLevel('INFO')
fh.setFormatter(formatter)#设置格式


#3、对接 最终的输出信息是取两者的交集
my_logger.addHandler(ch )
my_logger.addHandler(fh)

my_logger.debug ('这是debug信息')
my_logger.info('这是info级别的日志')
my_logger.warning('这是warning级别的日志')
my_logger.error('这里是error级别的日志')
my_logger.critical('这是critical级别的日志')

my_logger.removeHandler(fh) #把渠道移除，不然会存一大堆旧日志
my_logger.removeHandler(ch)#后进先出的缓存方式，所以后开先关，ch先开的，所以先移除fh