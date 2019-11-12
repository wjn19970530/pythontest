import time

from httprunner.api import HttpRunner

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
        result = {'time': {'start_at': start_at, 'duration': duration}, 'success': status,
                  'stat': {'testcases': {'total': total, 'success': success, 'fail': fail},
                           'teststeps': {'total': step_total, 'failures': step_failures, 'errors': step_errors,
                                         'successes': step_successes, 'expectedFailures': step_expectedFailures,
                                         'skipped': step_skipped, 'unexpectedSuccesses': step_unexpectedSuccesses}}}
        return result

    @staticmethod
    def run_test(second, case):
        """
        :param second: 休眠时间
        :param case: 用例
        :return:
        """
        runner = HttpRunner(log_level="ERROR", failfast=True)
        runner.run(case)
