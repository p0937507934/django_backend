import pymysql

pymysql.install_as_MySQLdb()

# 開啟資料庫連線
db = pymysql.connect('140.125.45.160', 'hsipl','211','api')
# db = pymysql.connect(host="localhost", user="root", password="admin", db="epoch", port=3306)
# 使用cursor()方法獲取操作遊標
cursor = db.cursor()
# 使用 executor()方法執行SQL語句
cursor.execute("SELECT VERSION()")
# 使用fetchone()獲取一條資料庫
data = cursor.fetchone()
print("Database version : %s " % data)
# 關閉資料庫連線
db.close()