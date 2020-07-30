# =============================================================================
#连接数据库汇总评分
# =============================================================================


import pymysql
# import datetime
import pandas as pd

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root',password='123456', database='financedatahub', charset='utf8')

# 设定参数
company = '熊猫直播'   # 选定公司
date_list = list(pd.date_range('2019-11-01', '2019-12-17'))  # 时间区间
for i in range(len(date_list)):
    # date_list[i] = datetime.datetime.strftime(date_list[i], '%Y-%m-%d')  # 也可以这样写：date_list[i] = date_list[i].strftime('%Y-%m-%d')
    date_list[i] = date_list[i].strftime('%Y-%m-%d')
# print(date_list)

#  编写SQL
cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'SELECT * FROM test WHERE company = %s AND date = %s'
# sql = 'SELECT * FROM test WHERE company = %s AND date = %s'

# 遍历date_list中的日期，获取每日分数并存储到字典score_list中
score_list = {}    # 定义分数的字典，用以存储每日分数
for d in date_list:
    cur.execute(sql, (company, d))
    data = cur.fetchall()  # 提取所有数据并赋值给data变量
    score = 100
    for i in range(len(data)):
        score += data[i][5]  # 合并该公司当天每条新闻分数
    score_list[d] = score
print(score_list)



db.commit()  # 更新表单，如果对数据表没有修改，可以不写这行
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库连接


# # 将dic转换为DataFrame表格
# data = pd.DataFrame.from_dict(score_list, orient='index')
# data.index.name = 'date'  # 将行索引那一列命名为date
# data.reset_index()  # 重置索引

# # 保存数据
# data.to_excel('score1.xlsx', index=False)  # 存储到本地的score.xlsx


data = pd.DataFrame(list(score_list.items()), columns=['date', 'score'])
print(data)
data.to_excel('score_测试数据.xlsx', index=False)

# 
# No module named 'openpyxl'  openpyxl  错误  pip install openpyxl
# TypeError: got invalid input value of type <class 'xml.etree.ElementTree.Element'>, expected string or Element
# pip uninstall openpyxl
# pip install openpyxl==3.0.1
# 



# 最后获取结果为：
# score_list = {'2018-09-01': 100, '2018-09-02': 100, '2018-09-03': 70, '2018-09-04': 75, ……, '2018-12-01': 100}
# 在之后的学习中，如果还没有创建数据库，可以把上面的字典里的省略号给去掉，以一个简单的数据进行之后的学习，无需提前创建好数据库。
# score_list = {'2018-09-01': 100, '2018-09-02': 100, '2018-09-03': 70, '2018-09-04': 75, '2018-12-01': 100}
