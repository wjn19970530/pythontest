import pymysql

from common.BaseCommon import BaseCommon
from config import *


class DBOperate(BaseCommon):
    def __init__(self, db):
        self.db = db

    def connect_saas_test_db(self):
        return pymysql.connect(host='10.0.25.28',
                               port=3306,
                               user='root',
                               password='123456',
                               database=self.db)

    def connect_online_db(self):
        return pymysql.connect(host='120.77.1.114',
                               port=3306,
                               user='at4taoqi',
                               password='Taoqi1030!@#',
                               database=self.db)

    def query_sql(self, sql_str):
        con = self.connect_saas_test_db()
        cur = con.cursor()
        cur.execute(sql_str)
        result = cur.fetchone()
        cur.close()
        con.close()
        return result

    def execute_sql(self, sql_str):
        con = self.connect_saas_test_db()
        cur = con.cursor()
        try:
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            self.log().error('数据库操作报错，执行语句【%s】' % sql_str)
            raise
        finally:
            cur.close()
            con.close()

    def query_sql_get_verify_code(self, sql_str):
        con = self.connect_online_db()
        cur = con.cursor()
        cur.execute(sql_str)
        result = cur.fetchone()
        cur.close()
        con.close()
        return result

if __name__ == '__main__':
    print(DBOperate("autotest-usercenter_1001").query_sql("SELECT user_id from tq_user where phone_num='15060138093'")[0])
    print(DBOperate("saas-componentcenter").query_sql_get_verify_code("SELECT answer from captcha where transaction_no='7ec11663e8104f2c85a17300cc8f4931'")[0])
    # DBOperate("mall_1001").execute_sql("update tq_order set user_id='2115600' where user_id='21156'")
