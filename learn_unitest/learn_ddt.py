#ddt data driver test(數據驅動測試)
#安装：pip install ddt
import unittest
from ddt import ddt,data,unpack #前面的ddt是模块，后面三个是函数，同时引入多个用逗号隔开即可
test_data_1=[[1,2,3],[3,-2,1]]
test_data_2=[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}]

#ddt是装饰器，装饰测试类,所以要引入unittest.TestCase
@ddt
class TestPringMsg(unittest.TestCase):#ddt是装饰器，装饰测试类,所以要引入unittest.TestCase

    # @data([1,2,3],(4,5,6))    #拆分并分别传参，类似for循环#用来装饰测试用例。#a=(1,2,3),@data(a)结果不一样的
    # @unpack #对可迭代的数据进行拆分，拆出来是多少个元素，函数就要用几个参数接收
    # def test_001(self,a,b,expected=0):#设置默认参数，防止data元素个数不一样，一般不用*args,因为相当于把拆了的又封装成元祖
    #     print('我正在执行第{}条用例'.format(a))
    #     c=a+b
    #     self.assertEqual(c,expected)
    #     print('a:',a)
    #     # print('b:',b)
    #     # print('c:',c)
    # @data(*test_data_1)#用*解包[[1,2,3],[3,-2,1]]--->[1,2,3],[3,-2,1]
    # @unpack             #拆分[1,2,3]-->1,2,3
    # def test_002(self,a,b,expected):#里面的参数是局部变量
    #     c=a+b
    #     self.assertEqual(c,expected)
    @data(*test_data_2)  #[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}]-->{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}
    @unpack     #{'a':1,'b':2,'expected':3}-->'a':1,'b':2,'expected':3
    def test_003(self,a,b,expected):#如果对字典进行拆分，要用对应的key作为参数名来接收值
        c=a+b
        print(c)
        self.assertEqual(c,expected)














