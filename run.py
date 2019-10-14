from httprunner.api import HttpRunner

from common.BaseCommon import BaseCommon

from time import sleep

if __name__ == '__main__':
    log_file = BaseCommon.get_logfile()
    runner = HttpRunner(log_level="DEBUG", log_file=log_file)
    # runner.run("testsuites/order.yml")
    # runner.run("testsuites")
    # runner.run("testcases/supply")
    # runner.run("testcases/WEB/app_login.yml")

    # runner.run("api/mall/user-senior/car-early-repayments/POST_Confirm.yml")


    # runner.run("testcases/usercenter/clean_customerInfo.yml")
    # runner.run("testcases/usercenter/add_customer.yml")
    # runner.run("testcases/usercenter/purchase_certification.yml")
    # runner.run("testcases/supply/create_car.yml")
    # runner.run("testcases/order/APP_create_order.yml")
    # runner.run("testcases/usercenter/perfect_userInfo.yml")
    # runner.run("testcases/order/audit_order.yml")
    # runner.run("testcases/order/perfect_repayment_info.yml")
    # runner.run("testcases/contracts/sign_contract.yml")
    # runner.run("testcases/order/mention_car.yml")


    # runner.run("api/supplychain/POST_Cars.yml")

    runner.run("testcases/transaction/create_car.yml")

    # runner.run("testcases/contracts/sign_contract.yml")
    # runner.run("api/usercenter/credit/custom-check/GET_VerifyCode.yml")
    # runner.run("api/usercenter/credit/custom-check/POST_Universal.yml")
    # runner.run("api/usercenter/back-end/users/PUT_SkipFaceCertV2.yml")
    # runner.run("api/mall/orders/PUT_ComfirmOrder.yml")

    # runner.run("api/mall/back-end/POST_CarItemSkus2.yml")
    # runner.run("api/usercenter/users/PUT_CleanUserInfo.yml")
    # runner.run("api/usercenter/users/PUT_CleanUserId.yml")


    # 获取用例执行情况
    # summary = runner.summary
    # print(summary)