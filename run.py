from httprunner.api import HttpRunner

from common.BaseCommon import BaseCommon

if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="DEBUG", log_file=log_file)
    # runner.run("testsuites/create_car.yml")
    # runner.run("testcases")
    runner.run("api")
    # runner.run("testcases/WEB/supply/create_car.yml")
    # 获取用例执行情况
    summary = runner.summary



