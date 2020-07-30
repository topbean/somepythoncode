# =============================================================================
# 从数据库汇总(每日)评分
# =============================================================================

import pymysql
import time

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='financedatahub', charset='utf8')

# 设定参数
company = '熊猫直播'   # 选定公司
today = time.strftime("%Y-%m-%d")  # 设置当天日期

#  编写SQL
cur = db.cursor()  # 获取会话指针，用来调用SQL语句
# sql = 'SELECT * FROM article WHERE company = %s '  # 如果想获取全部信息，可以把AND后面的筛选条件去掉   
sql = 'SELECT * FROM article WHERE company = %s  AND date = %s'  # 如果想获取全部信息，可以把AND后面的筛选条件去掉   
# cur.execute(sql, (company))
cur.execute(sql, (company, today))
data = cur.fetchall()  # 提取所有数据并赋值给data变量
# 计算当日评分
score = 100
for i in range(len(data)):
    score += data[i][5]  # 合并该公司当天每条新闻分数

db.commit()  # 更新表单，如果对数据表没有修改，可以不写这行
cur.close()  # 关闭会话指针
db.close()  # 关闭

print(company + '的今日舆情评分为：' + str(score))
# print(company + '的舆情评分为：' + str(score))
