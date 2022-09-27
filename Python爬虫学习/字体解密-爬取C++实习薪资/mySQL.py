import pymysql


class MySQL:
    # db = pymysql.connect("localhost","user","test123","TESTDB" )
    def __init__(self, _user, _passwd, _database, _host='127.0.0.1', _port=3306, _charset='utf8'):
        self.conPtr = pymysql.connect(
            user=_user,
            passwd=_passwd,
            database=_database,
            host=_host,
            port=_port,
            charset=_charset,
        )
        # 创建游标对象修改数据库
        self.curPtr = self.conPtr.cursor()

    def __execute(self, sql):
        try:
            self.curPtr.execute(sql)
            self.conPtr.commit()
            print('INFO:操作成功')
        except:
            self.conPtr.rollback()

    def CreateDatabase(self, sql):
        self.curPtr.execute(sql)

    # 查找一条语句
    def Search(self, sql):
        self.curPtr.execute(sql)
        result = self.curPtr.fetchone()
        return result

    # 查找多条数据
    def SearchAll(self, sql):
        self.curPtr.execute(sql)
        result = self.curPtr.fetchall()
        return result

    # 更新SQL
    def UpdateSQL(self, sql):
        self.__execute(sql)

    # 插入操作
    def InsertSQL(self, sql):
        self.__execute(sql)

    # 删除操作
    def DropSQL(self, sql):
        self.__execute(sql)

    # 关闭链接
    def Close(self):
        self.conPtr.close()
