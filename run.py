from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

from common.BaseCommon import BaseCommon
import json
import os

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
    # summary = runner.run("testsuites/develop/transaction/repayment_method.yml")
    # summary = runner.run("testcases/order/repayment_info/JHHK.yml")
    # summary = runner.run("testsuites/develop/supply/car.yml")
    # summary = runner.run("testcases/supply/generate_inventory.yml")
    # summary = runner.run("testcases/order/release_car/timed_release.yml")
    # summary = runner.run("testcases/order/repayment_info/XXFTL.yml")
    # summary = runner.run("testcases/order/lock_car/vin_lock_car.yml")
    # summary = runner.run("testcases/order/repayment_info/ZYR.yml")
    # summary = runner.run("testcases/order/release_car/timed_release.yml")
    # summary = runner.run("testcases/transaction/create_car.yml")
    # runner.run("testcases/login/master_login.yml")
    # runner.run("testcases/login/web_login.yml")
    # summary = runner.run("api/mall/mallSignAgreementInfo/tqtl/POST_SaveCommonTonglianInfo.yml")


    # runner.run("testcases/supply/add_car.yml")
    # runner.run("api/contract/GET_ContractTemplateSuites.yml")
    # runner.run("api/mall/back-end/car-lease-plans/POST_Item.yml")
    # runner.run("testcases/supply/generate_inventory.yml")
    # runner.run("api/usercenter/organizations/GET_Root.yml")
    # runner.run("api/usercenter/organization-cars/POST_Bind.yml")

    # runner.run("api/mall/back-end/car-items/POST_CreateEmpty.yml")
    # runner.run("api/mall/back-end/car-items/PUT_UpdateStatus.yml")
    # runner.run("api/mall/back-end/car-lease-plans/POST_Item.yml")
    # runner.run("api/mall/back-end/GET_CarTypesParams.yml")
    # runner.run("api/mall/back-end/POST_CarItemsBaseInfo.yml")

    # runner.run("testcases/order/refund/confirm_return.yml")

    # runner.run("testcases/supply/save_inventory.yml")
    # runner.run("api/supplychain/GET_Cars.yml")




    # runner.run("testsuites/supply/car.yml")
    # runner.run("testcases/order/nonaudit_order_count.yml")

    # 获取用例执行情况
    # summary = runner.summary
    result = BaseCommon.get_result(summary)
    file = "summary.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(result, f)
    f.close()
    gen_html_report(summary, report_template=r"./template/report_template.html")


