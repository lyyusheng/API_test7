# 安装mysql
# pip install pymysql或者装pip install mysql-connector-python两个库
from mysql import connector  # 一直报错划红线，左键悬浮安装了MySQL还是报错，后来发现装错了，要装mysql-connector-python，从提示后面选

# 第一步：链接数据库
# db_config={'host':'192.168.114.130',
#            'user':'root',
#            'password':'123456',
#            'port':3306,
#           'database':'jktest50',
#            }
# db_config = {'host': 'localhost',
#              'user': 'root',
#              'password': '',
#              'port': 3306,
#              'database': 'python14_jiekou'}
db_config = {'host': '47.107.168.87',
             'user': 'python',
             'password': 'python666',
             'port': 3306,
             'database': 'future'}
cnn = connector.connect(**db_config)  # 关键字参数，db_config原来是字典，直接传进来之后还是字典
# 或者这样传：cnn=connector.connect(host='192.168.114.130',user:'root',password:'123456', port:3306,database:'lemomjiekou')

# 第二步：获取游标，获取操作数据库的权限
cursor = cnn.cursor()  # 建立游标

# 第三步：操作数据表
query = 'select * from member where Id<23529'
cursor.execute(query)

# 第四步：打印结果
res1 = cursor.fetchone()  # 获取第一个结果，返回值是元组
res2 = cursor.fetchall()  # ，获取光标后面所有结果，返回值是列表里面的元组。
# 由于光标移动，如果第一条被fetchone获取过了，即使用fetchall()也只打印第二及后面的,如果只有一个结果，fetchone之后接fetchone会报错，可能是后面没结果了
print('数据库查询结果1是:{}'.format(res1))  # 把{ }忘了，搞到死都打印不出结果
print('数据库查询结果2是:{}'.format(res2))

# 增删改 update (测试一般只用到查，这里只做了解)
# cursor.execute(query)
# cursor.execute('commit')    #提交
