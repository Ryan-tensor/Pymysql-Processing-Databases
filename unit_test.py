import pymysql
def create_database(dbname):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "CRETE DATABASE " + dbname + ';'
    curs.execute(sql)

def drop_database(dbname):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "DROP DATABASES IF EXISTS " + dbname + ';'
    curs.execute(sql)

def use(dbname):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "USE " + dbname + ';'
    curs.execute(sql)

def create_table(tablename):            ###column name 및 속성 바꿔서 사용할 것
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''CREATE TABLE '''+tablename+'''(
  column_name1 INT PRIMARY KEY AUTO_INCREMENT,
  column_name2 VARCHAR(15) NOT NULL,
  column_name3 INT
) ENGINE=INNODB;'''
    curs.execute(sql)

def status():
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "STATUS"
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
def drop_table(tablename):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "DROP TABLE "+tablename+';'
    curs.execute(sql)

def describe(tablename):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "DESCRIBE " + tablename + ';'
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)
def explain(tablename):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "EXPLAIN " + tablename + ';'
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)

def insert_into(tablename, *values):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "INSERT INTO " + tablename + " VALUES("
    for val in values:
        sql += val + ","
    sql = sql[:-1]
    sql += ");"
    curs.execute(sql)

def select_from(tablename, *values):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT "
    for val in values:
        sql += val + ","
    sql = sql[:-1]
    sql += " FROM "+tablename+";"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)
def commit():
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("COMMIT;")
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='1qaz@WSX#eDc',
                       db='testtable1', charset='utf8')

# Connection 으로부터 Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

#sql = "select * from person where name=%s and gip=%s"
#curs.execute(sql, ('박동수', '금천구'))
#status() ###상태보기는 에러   1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'STATUS' at line 1"
#explain("tablename")
#describe("tablename")
#create_table("tablename")
#drop_table("tablename")
insert_into("tablename", "1","2","3")
select_from("tablename", "*")
commit()
"""
# 데이타 Fetch
rows = curs.fetchall()
for row in rows:
    print(row)
    # 출력 : {'category': 1, 'id': 1, 'region': '서울', 'name': '김정수'}
    print(row['gip'], row['name'])
    # 1 김정수 서울
"""
# Connection 닫기
conn.close()