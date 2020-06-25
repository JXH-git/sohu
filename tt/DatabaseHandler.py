# coding:utf-8

import pymysql
from pymysql.err import *


class DatabaseHandler(object):
    def __init__(self, host, username, password, database, port=3306):
        """初始化数据库连接"""
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, self.port, charset='utf8')
        self.cursor = None

    def execute(self, sql):
        """执行SQL语句"""
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute(sql)
            self.db.commit()
        except (MySQLError, ProgrammingError) as e:
            print(e)
            self.db.rollback()
        else:
            print("rowCount: %s rowNumber: %s" % (self.cursor.rowcount, self.cursor.rownumber))
        finally:
            self.cursor.close()

    def update(self, sql):
        """ 更新操作"""
        self.execute(sql)

    def insert(self, sql):
        """插入数据"""
        self.execute(sql)
        return self.cursor.lastrowid

    def insert_bath(self, sql, rows):
        """批量插入"""
        try:
            self.cursor.executemany(sql, rows)
            self.db.commit()
        except (MySQLError, ProgrammingError) as e:
            print(e)
            self.db.rollback()
        else:
            print("rowCount: %s rowNumber: %s" % (self.cursor.rowcount, self.cursor.rownumber))
        finally:
            self.cursor.close()

    def delete(self, sql):
        """删除数据"""
        self.execute(sql)

    def select(self, sql):
        """查询数据 返回 map 类型的数据"""
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        result = []
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            for row in data:
                result.append(row)
        except MySQLError as e:
            print(e)
        else:
            print("rowCount: {} rowNumber: {}".format(self.cursor.rowcount,self.cursor.rownumber))
            return result
        finally:
            self.cursor.close()

    def call_proc(self, name):
        """调用存储过程"""
        self.cursor.callproc(name)
        return self.cursor.fetchone()

    def close(self):
        """关闭连接"""
        self.db.close()


if __name__ == "__main__":
    pass
