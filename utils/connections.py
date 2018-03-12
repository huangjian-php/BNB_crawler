#!/usr/bin/env python
# coding=utf-8

import pymysql as MySQLdb

from conf import config

MYSQL_CONN_POOL = []

class MysqlConnection(object):
    '''
    operate mysql
    '''
    def __init__(self):
        self.reconnect()

    def reconnect(self):
        self.conn = MySQLdb.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            passwd=config.MYSQL_PWD,
            #db=config.MYSQL_DB,
            charset='utf8')
        self.conn.autocommit(True)

    def __del__(self):
        self.conn.close()

    def _ping(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('select 1;')
            cursor.fetchall()
            cursor.close()
        except MySQLdb.OperationalError:
            self.reconnect()

def get_mysql():
    if not MYSQL_CONN_POOL:
        MYSQL_CONN_POOL.append(MysqlConnection())
    conn = MYSQL_CONN_POOL.pop(0)
    conn._ping()
    return conn

def rel_mysql(conn):
    MYSQL_CONN_POOL.append(conn)
