from httprunner.api import HttpRunner

from common.BaseCommon import BaseCommon
import json
import os

if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="DEBUG", log_file=log_file)
    tmp_file = "data/tmp.json"
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    # runner.run("testsuites/order.yml")
    # runner.run("testcases/web_login.yml")

    # runner.run("api/mall/car-items/GET_CarItemDetails.yml")
    # runner.run("api/mall/back-end/car-lease-plans/POST_Item.yml")


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


    # runner.run("api/mall/back-end/GET_CarTypesParams.yml")

    runner.run("testcases/transaction/create_car.yml")
    #
    # runner.run("testsuites/order.yml")

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
    # runner.run("testcases/order/test.yml")

    # 获取用例执行情况
    summary = runner.summary
    # print(summary)
    file = "summary.json"
    with open(file, "w", encoding='utf-8') as f:
        json.dump(summary, f)
    f.close()
