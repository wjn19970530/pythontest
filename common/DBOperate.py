import pymysql

from common.BaseCommon import BaseCommon


class DBOperate(BaseCommon):
    def __init__(self, db):
        self.db = db

    def connect_saas_test_db(self):
        return pymysql.connect(host='10.0.25.28',
                               port=3306,
                               user='root',
                               password='123456',
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


if __name__ == '__main__':
    print(DBOperate("usercenter_1001").query_sql("SELECT user_id from tq_user where phone_num='15060138093'")[0])
    # DBOperate("mall_1001").execute_sql("update tq_order set user_id='2115600' where user_id='21156'")
