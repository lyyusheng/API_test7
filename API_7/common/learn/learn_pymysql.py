import pymysql

db_config = {'host': '106.13.46.204',
             'user': 'root',
             'password': 'root1234',
             'port': 3306,
             'database': 'future'
             }
# db_config = {'host': '47.107.168.87',
#              'user': 'python',
#              'password': 'python666',
#              'port': 3306,
#              'database': 'future'}
# 连接数据库
db = pymysql.connect(**db_config)

# 获取游标
cur = db.cursor()

# 第三步：操作数据表
query = 'select * from member where Mobilephone=18300070752'
cur.execute(query)
res = cur.fetchall()
db.close()

print('数据库查询结果是:｛｝'.format(res))