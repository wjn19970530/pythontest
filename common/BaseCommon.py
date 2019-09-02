import time
from common.log import MyLog


class BaseCommon(object):
    @staticmethod
    def get_time():
        time1 = int(time.time())
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time1))
        now_date = time.strftime('%Y-%m-%d', time.localtime(time1))
        return {'now_time': now_time, 'now_date': now_date}

    @staticmethod
    def log():
        log = MyLog()
        return log

    @staticmethod
    def get_logfile():
        return MyLog().log_file
