from httprunner.api import HttpRunner

from common.BaseCommon import BaseCommon
import json
import os


def get_result(summary):
    status = summary['success']
    total = summary['stat']['testcases']['total']
    success = summary['stat']['testcases']['success']
    fail = summary['stat']['testcases']['fail']
    step_total = summary['stat']['teststeps']['total']
    step_failures = summary['stat']['teststeps']['failures']
    step_errors = summary['stat']['teststeps']['errors']
    step_skipped = summary['stat']['teststeps']['skipped']
    res = {'success': status, 'stat': {'testcases': {'total': total, 'success': success, 'fail': fail},
                                          'teststeps': {'total': step_total, 'failures': step_failures,
                                                        'errors': step_errors, 'skipped': step_skipped}}}
    return res


if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="DEBUG", log_file=log_file, failfast=True,report_template=r"./template/report_template.html")
    tmp_file = "data/tmp.json"
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    runner.run("testcases/login/web_login.yml")
    runner.run("testsuites/develop/")
    # runner.run("testsuites/order.yml")
    # runner.run("testcases/login/master_login.yml")
    # runner.run("testcases/login/web_login.yml")
    # runner.run("api/account/GET_TransactionNo.yml")

    # runner.run("testcases/supply/add_car.yml")
    # runner.run("testcases/supply/generate_inventory.yml")
    # runner.run("testcases/supply/confirm_inventory.yml")
    # runner.run("api/mall/back-end/car-item-skus/GET_Generate.yml")
    # runner.run("api/mall/back-end/car-items/POST_CreateEmpty.yml")


    # runner.run("testcases/usercenter/clean_customerInfo.yml")
    # runner.run("testcases/usercenter/add_customer.yml")
    # runner.run("testcases/usercenter/purchase_certification.yml")
    # runner.run("testcases/usercenter/perfect_userInfo.yml")
    # runner.run("testcases/supply/create_car.yml")
    # runner.run("testcases/order/APP_create_order.yml")
    # runner.run("testcases/order/audit_order.yml")
    # runner.run("testcases/order/perfect_repayment_info.yml")
    # runner.run("testcases/contracts/sign_contract.yml")
    # runner.run("testcases/order/mention_car.yml")


    # runner.run("api/mall/orders/release-car/PUT_Manual.yml")
    # runner.run("api/mall/orders/PUT_ReUpdateLockApply.yml")
    # runner.run("testcases/order/system_lock_car.yml")
    # runner.run("testcases/order/vin_lock_car.yml")

    # runner.run("testcases/transaction/create_car.yml")



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
    # runner.run("testsuites/transaction/order.yml")

    # 获取用例执行情况
    summary = runner.summary
    result = get_result(summary)
    file = "summary.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(result, f)
    f.close()


