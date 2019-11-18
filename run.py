from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
from common.BaseCommon import BaseCommon
import json

from debugtalk import get_value_from_tmp

if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="INFO", log_file=log_file, failfast=True)
    tmp_file = "data/tmp.json"
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    summary = runner.run("testcases/order/nonaudit_order_count.yml")
    times = get_value_from_tmp("length")
    if times != 0:
        for i in range(times):
            runner.run("testcases/order/audit_order_without_sleep.yml")

    summary = runner.run("testcases/login/web_login.yml")
    summary = runner.run("testsuites/develop/")
    # summary = runner.run("testsuites/develop/transaction/lock_car.yml")
    # summary = runner.run("testcases/order/repayment_info/JHHK.yml")
    # summary = runner.run("testcases/order/pay_beforehand/purchase_certification.yml")
    # summary = runner.run("testcases/usercenter/add_customer.yml")
    # summary = runner.run("testcases/usercenter/purchase_certification.yml")
    # summary = runner.run("testcases/usercenter/perfect_userInfo.yml")
    # summary = runner.run("testcases/supply/generate_inventory.yml")
    # summary = runner.run("testcases/order/release_car/immediately_release.yml")
    # summary = runner.run("testcases/order/repayment_info/XXFTL.yml")
    # summary = runner.run("testcases/order/lock_car/system_lock_car.yml")
    # summary = runner.run("testcases/order/repayment_info/ZYR.yml")
    # summary = runner.run("testcases/order/release_car/timed_release.yml")
    # summary = runner.run("testcases/transaction/create_car.yml")
    # runner.run("testcases/login/master_login.yml")
    # summary = runner.run("testcases/transaction/create_car.yml")
    # summary = runner.run("testcases/order/refund/wait_audit_refund.yml")

    # 获取用例执行情况
    result = BaseCommon.get_result(summary)
    file = "summary.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(result, f)
    f.close()
    gen_html_report(summary, report_template=r"./template/report_template.html")


