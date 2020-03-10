#写配置文件格式
#   [section]
#   #注释（前面用井号）
#   option1=value1      #注意value不要加"",用“=”或者“：”都可以
#   ...

#读配置文件  引入configparser模块，里面有很多类，其中一个类是Configparser
import configparser
#创建对象
cf = configparser.ConfigParser()
class ReadConfig:
    def __init__(self,section1,option1):
        self.section=section1
        self.option=option1
    #第一步：打开文件 调用read()方法，源码里面调用的是open的
    cf.read('log.conf',encoding='utf-8')  #内容有中文时要设置encoding
     #第二步：读取内容,读到的内容不管原来是什么类型，都变成字符串,openpyxl则不一样，数字还是数字，其他的变成字符串或者布尔型
    def get_str(self):
        res=cf.get(self.section,self.option)#第一种方法
       # res1=cf['StudentName']['stu_1'] #第二种方法
        return res
        #print(type(res))
        #print(type(eval(res)))#eval转换回原来的类型，但是原本就是字符串的，用了eval会报错。也可用于open
    #想要读取特定数据类型，就要用特定函数
    def get_bool(self,):
        res=cf.getboolean(self.section,self.option)
        print(res)
    def get_float(self):
        res=cf.getfloat(self.section,self.option)
        print(res)
    def get_int(self):
        res=cf.getint(self.section,self.option)
        print(res)
if __name__ == '__main__':
    res= ReadConfig('LOG','logger_name').get_str()
    print(res)
    print(type(res))


