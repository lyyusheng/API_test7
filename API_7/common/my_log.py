# 不要把模块命名为logging，会与系统自带的冲突
# 日子的等级debug-info-warning-error-critical/fatal
# 日志收集器logger    默认的日志收集器 rootlogger
import logging
from FuXi2.read_config import ReadConfig
from API_test.API_7.common import project_path


class MyLog:
    # def __init__(self):
    #    self.logger_name= ReadConfig('LOG','logger_name').get_str()
    # 我的ReadConfig类跟老师的不一样的，我的ReadConfig类有初始化函数，应该从对象传入参数，但是我把参数写到了ReadConfig().get_str('LOG','logger_name'),
    # 一直报错缺2个参数，原来的模块参数从哪里传入的，导入之后也是从哪里传入
    def my_log(self, level, msg):
        # 1.自定义一个日志收集器并且设置级别getLogger
        my_logger = logging.getLogger('api_log')
        my_logger.setLevel('DEBUG')
        # 2.指定输出渠道还要设置级别 StreamHandler(控制台) 、FileHandler（指定文件）
        # 输出到控制台
        formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')
        # 根据自己需要设置格式，顺序不限制，可以用[]括起来，
        ch = logging.StreamHandler()
        ch.setLevel('INFO')
        ch.setFormatter(formatter)  # 设置日志格式，有很多种格式，根据需要网上找
        # 输出到指定文件
        fh = logging.FileHandler(project_path.log_path, encoding='utf-8')  # 文件不存在时自动生成
        fh.setLevel('INFO')
        fh.setFormatter(formatter)  # 设置格式

        # 3、对接 最终的输出信息是取两者的交集
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'Error':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)  # 把渠道移除，不然会存一大堆旧日志
        my_logger.removeHandler(ch)  # 后进先出的缓存方式，所以后开先关，ch先开的，所以先移除fh

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    MyLog().my_log('ERROR', '这特么的是error信息')
    MyLog().my_log('INFO', '只是info信息')
    MyLog().error('error信息')
