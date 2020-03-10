import unittest
import HTMLTestRunnerNew
from learn_unitest import test_case#从之前写好的测试用例模块导入测试加法的测试用例类TestAdd。import *則是導入所有類
from learn_unitest import test_case_ddt
#添加測試用例
suite=unittest.TestSuite()  #TestSuite是一个类，继承了BaseTestSuite类
# #方法一：
# suite.addTest(test_case.TestAdd('test_001')) #addTest是BaseTestSuite类里面的一个函数，用来添加测试用例。创建TestAdd这个测试加法的测试用例类的实例（对象），需要传入方法名作为参数
# suite.addTest(test_case.TestAdd('test_002'))
# suite.addTest(test_case.TestAdd('test_003'))
# suite.addTest(test_case.TestAdd('test_004'))

#專門用來加載用例的兩種方法 LOADER,使用ddt的话只能用下面这两种
#方法二：通過測試用例类來添加
# loader=unittest.TestLoader()    #TestLoader()是一個對象
# suite.addTest(loader.loadTestsFromTestCase(test_case.TestAdd))

#方法三：通過測試模塊添加。前面的導入就不能具體到方法名了
loader=unittest.TestLoader()    #TestLoader()是一個對象
suite.addTest(loader.loadTestsFromModule(test_case_ddt))


#执行测试用例生成報告
#方法一：  TextTestRunner
# with open('test.txt','w',encoding='utf-8') as file:
#     runner=unittest.TextTestRunner( stream=file,  verbosity=2)    #TextTestRunner是一个类,生成測試用例
#     #verbosity表示測試報告詳細程度，一般用2最詳細
#     runner.run(suite)   #執行測試套件裏面的用例

#方法二：
with open('test_0816.html','wb') as file:  #HTML需要選用wb模式（二進制），不需要設置encoding
    runner=HTMLTestRunnerNew.HTMLTestRunner( stream=file,
                                             verbosity=2,
                                             title='2018年測試報告',
                                             description='實驗用的',
                                             tester='liyusheng')
    runner.run(suite)
