#文件名以ddt结尾可能会有坑！不报错也不出结果，改下名字再执行又一切正常
import unittest
from ddt import ddt,data,unpack
test_data_1=[[1,2,4],[-1,2,1],[-1,-2,-3],[0,0,0]]
test_data_2=[[1,2,3],[-1,2,1],[-1,-2,-3],[0,0,0]]
@ddt
class TestAdd(unittest.TestCase):   #繼承TestCase這個類
    '''1、用例方法名必須以test_開頭，否則無法識別。
    2、鼠标放在测试用例类名上面右键执行该类里面的全部用例鼠標懸浮在用例方法名上右鍵則單獨執行該條用例，
        光標移到最底下空白右鍵執行最下面那个测试用例类里面的全部用例
    3、用例執行順序是按照asclll編碼執行的'''

    def setUp(self):#每條用例執行之前執行
        print('開始執行新一條測試了')    #準備工作
    def tearDown(self):#每條用例執行之後執行
        print('一條測試用例執行完畢')  #清場工作，把占用的環境資源關掉
    @data(*test_data_1)
    @unpack
    def test_001(self,a,b,expected):#測試兩數相加

        c = a + b
        try:
            self.assertEqual(expected,c)    ##asserEqual是TestCase裏面的方法，class TestAdd(unittest.TestCase):繼承了TestCase這個類，所以用self.調用
            #斷言不對，後面就不會再執行，所以不會執行下面的print（），引入異常處理后則可以執行
        except AssertionError as e:
            print('001用例執行失敗，錯誤是{}'.format(e))
            raise e
        print('測試結果是：{}'.format(c))
#     def test_002(self):#測試一正一負相加
#         a=-1
#         b=2
#         expected=1
#         c=a+b
#         try:
#             self.assertEqual(expected, c)
#         except AssertionError as e:
#             print('002測試用例執行失敗，錯誤是{}'.format(e))
#             raise e
#         print('測試結果是{}'.format(c))
#     def test_003(self):#測試兩個負數相加
#         a=-1
#         b=-2
#         expected=-3
#         c=a+b
#         try:
#             self.assertEqual(expected, c)
#         except AssertionError as e:
#             print('003測試用例執行失敗，錯誤是{}'.format(e))
#             raise e
#         #asserEqual是TestCase裏面的方法，class TestAdd(unittest.TestCase):   #繼承TestCase這個類，所以用self.調用。
#         print('測試結果是{}'.format(c))
#     def test_004(self):#測試兩個0相加
#         a=0
#         b=0
#         c = a + b
#         expected=0
#         try:
#             self.assertEqual(expected, c)
#         except AssertionError as e:
#             print('004測試用例執行失敗，錯誤是{}'.format(e))
#             raise e
#         self.assertEqual(expected, c)
#         print('測試結果是{}'.format(c))
#
# class TestSub():
#     def setUp(self):#每條用例執行之前執行
#         print('開始執行新一條測試了')    #準備工作
#     def tearDown(self):#每條用例執行之後執行
#         print('一條測試用例執行完畢')  #清場工作，把占用的環境資源關掉
#     def test_positive_negative(self):#測試兩個正數相减
#         a=1
#         b=2
#         c=a-b
#         print('測試結果是：{}'.format(c))
#     def test_two_negative(self):#測試一正一負相减
#         a=-1
#         b=2
#         c=a-b
#         print('測試結果是{}'.format(c))
#     def test_two_zero(self):#測試兩個0相减
#         a=-1
#         b=-2
#         c=a-b
#         print('測試結果是{}'.format(c))
