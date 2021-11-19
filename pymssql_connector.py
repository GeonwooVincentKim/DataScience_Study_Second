import pymysql

user_db = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='STATISTICS_EXAMPLE_DB',
    charset='utf8'
)

cursor = user_db.cursor(pymysql.cursors.DictCursor)
