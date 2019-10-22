import time
from common.log import MyLog
import json
import os


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

    @staticmethod
    def read_tmp_file(file):
        if not os.path.exists(file):
            f = open(file, "w")
            f.write("{}")
            f.close()
        with open(file, "r") as f:
            message = json.load(f)
        f.close()
        return message

    @staticmethod
    def write_tmp_file(file, message):
        with open(file, "w") as f:
            json.dump(message, f)
        f.close()

