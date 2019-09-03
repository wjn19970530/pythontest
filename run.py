import subprocess
import os
from httprunner.api import HttpRunner

from common.BaseCommon import BaseCommon

if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="DEBUG", log_file=log_file)
    # runner.run(path_or_tests='testsuites/create_car.yml')
    runner.run(path_or_tests='api/WEB')
    # runner.run(path_or_tests='testcases/create_car.yml')
    # 获取用例执行情况
    summary = runner.summary



