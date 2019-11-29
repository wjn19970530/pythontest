import time
from common.DBOperate import DBOperate
from common.log import MyLog
import json
import os


class BaseCommon(object):
    @staticmethod
    def get_time():
        time1 = int(time.time())
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time1))
        now_date = time.strftime('%Y-%m-%d', time.localtime(time1))
        return {'timestamp': time1, 'now_time': now_time, 'now_date': now_date}

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
            f = open(file, "w", encoding="utf-8")
            f.write("{}")
            f.close()
        with open(file, "r", encoding="utf-8") as f:
            message = json.load(f)
        f.close()
        return message

    @staticmethod
    def write_tmp_file(file, message):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(message, f)
        f.close()

    @staticmethod
    def get_result(summary):
        start_at = summary['time']['start_at']
        duration = summary['time']['duration']
        status = summary['success']
        total = summary['stat']['testcases']['total']
        success = summary['stat']['testcases']['success']
        fail = summary['stat']['testcases']['fail']
        step_total = summary['stat']['teststeps']['total']
        step_failures = summary['stat']['teststeps']['failures']
        step_errors = summary['stat']['teststeps']['errors']
        step_skipped = summary['stat']['teststeps']['skipped']
        step_expectedFailures = summary['stat']['teststeps']['expectedFailures']
        step_unexpectedSuccesses = summary['stat']['teststeps']['unexpectedSuccesses']
        step_successes = summary['stat']['teststeps']['successes']
        # result = {'time': {'start_at': start_at, 'duration': duration}, 'success': status,
        #           'stat': {'testcases': {'total': total, 'success': success, 'fail': fail},
        #                    'teststeps': {'total': step_total, 'failures': step_failures, 'errors': step_errors,
        #                                  'successes': step_successes, 'expectedFailures': step_expectedFailures,
        #                                  'skipped': step_skipped, 'unexpectedSuccesses': step_unexpectedSuccesses}}}
        result = {'time': {'start_at': start_at, 'duration': duration}, 'success': status,
                  'stat': {'testcases': {'total': total, 'success': success, 'fail': fail},
                           'teststeps': {'total': step_total, 'failures': step_failures, 'errors': step_errors,
                                         'successes': step_successes, 'expectedFailures': step_expectedFailures,
                                         'skipped': step_skipped, 'unexpectedSuccesses': step_unexpectedSuccesses}}}
        return result

    @staticmethod
    def save_msg_to_database(db, table, time, type, method):
        sql = "insert into " + table + "(spend_time,type,method) values(" + str(time) + "," + str(type) + "," + str(
            method) + ")"
        DBOperate(db).execute_sql(sql)

    @staticmethod
    def get_value_from_env(key):
        value = ''
        with open(".env", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if key in line:
                    value = (line.split('='))[1]
        return value

    @staticmethod
    def save_report_to_database(db, table, data, branch):
        if data['success'] is True:
            success = "true"
        else:
            success = "false"
        field = "branch,success,case_total,case_success,case_fail,step_total,step_success,step_fail,step_error," \
                "step_skip,step_expectedFailures,step_unexpectedSuccesses"
        totalNum = str(data["stat"]["testcases"]["total"])
        successNum = str(data["stat"]["testcases"]["success"])
        failNum = str(data["stat"]["testcases"]["fail"])
        steps_totalNum = str(data["stat"]["teststeps"]["total"])
        steps_failNum = str(data["stat"]["teststeps"]["failures"])
        steps_errorNum = str(data["stat"]["teststeps"]["errors"])
        steps_skipNum = str(data["stat"]["teststeps"]["skipped"])
        steps_successNum = str(data["stat"]["teststeps"]["successes"])
        steps_expectedFailuresNum = str(data["stat"]["teststeps"]["expectedFailures"])
        steps_unexpectedSuccessesNum = str(data["stat"]["teststeps"]["unexpectedSuccesses"])
        value = "'"+branch+"','"+success+"','"+totalNum+"','"+successNum+"','"+failNum+"','"+steps_totalNum+"','"\
                +steps_successNum+"','"+steps_failNum+"','"+steps_errorNum+"','"+steps_skipNum+"','"\
                +steps_expectedFailuresNum+"','"+steps_unexpectedSuccessesNum+"'"
        sql = "insert into "+table+"("+field+") values("+value+")"
        DBOperate(db).execute_sql(sql)