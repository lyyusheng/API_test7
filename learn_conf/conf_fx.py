#写配置文件格式
#   [section]
#   #注释（前面用井号）
#   option1=value1      #注意value不要加"",用“=”或者“：”都可以
#   ...

#读配置文件  引入configparser模块，里面有很多类，其中一个类是Configparser
import configparser
#创建对象
cf=configparser.ConfigParser()
#第一步：打开文件 调用read()方法，源码里面调用的是open的
cf.read('learn14.conf',encoding='utf-8')  #内容有中文时要设置encoding
 #第二步：读取内容,读到的内容不管原来是什么类型，都变成字符串,openpyxl则不一样，数字还是数字，其他的变成字符串或者布尔型
res=cf.get('StudentName','stu_1')#第一种方法
res1=cf['StudentName']['stu_1'] #第二种方法
print(res)
print(type(res))
print(type(eval(res)))#eval转换回原来的类型，但是原本就是字符串的，用了eval会报错。也可用于open
#想要读取特定数据类型，就要用特定函数
cf.getboolean()
cf.getfloat()
cf.getint()
