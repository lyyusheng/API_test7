#ddt data driver test(數據驅動測試)
#安装：pip install ddt
import unittest
from ddt import ddt,data,unpack #前面的ddt是模块，后面三个是函数，同时引入多个用逗号隔开即可

#ddt是装饰器，装饰测试类,所以要引入unittest.TestCase
@ddt
class TestPringMsg(unittest.TestCase):#ddt是装饰器，装饰测试类,所以要引入unittest.TestCase

    @data(1,2,3)
    def test_001(self,a):
        print('我正在执行第{}条用例'.format(a))
        print('a:',a)
        # print('b:',b)
        # print('c:',c)
#照着老师的视频抄，但是既不报错也没打印结果，改了个名字又好了，原因不明,文件名以ddt结尾可能会有坑！

