from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
from common.BaseCommon import BaseCommon
import json
import os
from debugtalk import get_value_from_tmp


if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="DEBUG", log_file=log_file, failfast=True)
    tmp_file = "data/tmp.json"
    if os.path.exists(tmp_file):
        os.remove(tmp_file)

    summary = runner.run("testcases/order/master/nonaudit_order_count.yml")
    times = get_value_from_tmp("length")
    if times != 0:
        for i in range(times):
            runner.run("testcases/order/master/audit_order_without_sleep.yml")

    summary = runner.run("testcases/login/master_login.yml")
    summary = runner.run("testsuites/master/")
    # summary = runner.run("testcases/supply/create_car.yml")
    # summary = runner.run("testcases/order/master/change_car/not_change.yml")
    # summary = runner.run("testcases/order/master/release_car/")
    # summary = runner.run("testcases/transaction/master/create_car.yml")
    # summary = runner.run("testcases/order/master/vin_lock_car.yml")
    # summary = runner.run("testcases/supply/master/confirm_inventory.yml")


    # 获取用例执行情况
    result = BaseCommon.get_result(summary)
    file = "summary.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(result, f)
    f.close()
    gen_html_report(summary, report_template=r"./template/report_template.html")


