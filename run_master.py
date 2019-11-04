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

    runner.run("testcases/order/master/nonaudit_order_count.yml")
    times = get_value_from_tmp("length")
    if times != 0:
        for i in range(times):
            runner.run("testcases/order/master/audit_order_without_sleep.yml")

    runner.run("testcases/login/master_login.yml")
    summary = runner.run("testsuites/master/transaction/order.yml")

    # summary = runner.run("testcases/order/master/release_car/immediately_release.yml")

    # runner.run("testcases/transaction/master/create_car.yml")
    # runner.run("testcases/order/master/system_lock_car.yml")
    # runner.run("testcases/order/master/vin_lock_car.yml")
    # runner.run("api/mall/salesman/POST_Order.yml")
    # runner.run("testcases/order/master/create_order.yml")
    # runner.run("testsuites/login/order.yml")
    # runner.run("testcases/web_login.yml")
    # runner.run("api/mall/back-end/orders/POST_Params.yml")

    # runner.run("testcases/supply/add_car.yml")
    # runner.run("testcases/supply/generate_inventory.yml")
    # runner.run("testcases/supply/confir*m_inventory.yml")
    # runner.run("api/mall/back-end/car-item-skus/GET_Generate.yml")
    # runner.run("api/mall/back-end/car-items/POST_CreateEmpty.yml")


    # runner.run("testcases/usercenter/clean_customerInfo.yml")
    # runner.run("testcases/usercenter/add_customer.yml")
    # runner.run("testcases/usercenter/purchase_certification.yml")
    # runner.run("testcases/usercenter/perfect_userInfo.yml")
    # runner.run("testcases/supply/create_car.yml")
    # runner.run("testcases/order/APP_create_order.yml")
    # runner.run("testcases/order/master/audit_order.yml")
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
    result = BaseCommon.get_result(summary)
    file = "summary.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(result, f)
    f.close()
    gen_html_report(summary, report_template=r"./template/report_template.html")


