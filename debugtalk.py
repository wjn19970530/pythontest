import time

from httprunner.api import HttpRunner
from common.BaseCommon import BaseCommon as BCommon
from common.CsvOperate import CsvOperate
from common.DBOperate import DBOperate
from config import *

log = BCommon.log()
file = 'data/tmp.json'
runner = HttpRunner(log_level="ERROR", failfast=True)


def sleep(n_secs):
    time.sleep(n_secs)


def get_file_name(file_name):
    """
    获取文件名称
    :param file_name: like car03.jpg
    :return: car03
    """
    return file_name.split('.')[0]


def refresh_token(source, accesstoken, refreshtoken):
    """
    每次调用登录接口都更新一次csv的token
    :param source：平台 APP或WEB
    :param accesstoken:
    :param refreshtoken:
    :return:
    """
    # 获取需要写入的内容
    content = CsvOperate().generate_text('data/token.csv', source, accesstoken, refreshtoken)
    # 写入csv文件中
    CsvOperate().write_token_csv('data/token.csv', content)


def get_token(token_type, source='WEB'):
    """
    从csv文件获取最新的token值
    :param token_type:"access_token"或"refresh_token"
    :param source:平台，"WEB"或"APP"，默认WEB
    :return: token值
    """
    if token_type == 'access_token':
        access_token_value: str = CsvOperate().read_row_csv('data/token.csv', source, 'access_token')
        return access_token_value
    elif token_type == 'refresh_token':
        refresh_token_value: str = CsvOperate().read_row_csv('data/token.csv', source, 'refresh_token')
        return refresh_token_value
    else:
        log.error('仅支持获取"access_token"和"refresh_token"，请检查输入')


def response_get_car_brand_id(response, keyword):
    """
    从response中提取制定的brandId并写入data/tmp.json
    :param keyword: 车型品牌
    :param response:接口返回数据
    :return:
    """
    data = response.json["content"]
    brand_id = ''
    for item in data:
        if item["name"] == keyword:
            brand_id = item['id']
    message = BCommon.read_tmp_file(file)
    message["brand_id"] = brand_id
    BCommon.write_tmp_file(file, message)


# def tmp_file_get_brand_id():
#     """
#     从data/tmp.json读取brandId
#     :return: brand_id
#     """
#     message = BCommon.read_tmp_file("data/tmp.json")
#     brand_id = message["brand_id"]
#     return brand_id


def response_refresh_token(response, endpoint):
    """
    获取登录接口的token，并更新csv中的token信息
    :param response:
    :param endpoint:'pc-web'或'mobile'
    :return:
    """
    accesstoken = response.json["access_token"]
    refreshtoken = response.json["refresh_token"]
    if str(endpoint).lower() == 'pc-web':
        refresh_token('WEB', accesstoken, refreshtoken)
    elif str(endpoint).lower() == 'mobile':
        refresh_token('APP', accesstoken, refreshtoken)
    else:
        log.error("平台来源无法识别，请检查")


def generate_number() -> str:
    """
    生成时间戳
    :return: str，如20190906104443
    """
    now_time = BCommon.get_time()['now_time']
    now_time = str(now_time).replace('-', '').replace(':', '').replace(' ', '')
    return now_time


def add(x, y):
    """
    对两个数相加
    :param x:
    :param y:
    :return:
    """
    sum = int(x) + int(y)
    return sum


def sql_get_user_id(phone_num):
    """
    获取用户id
    操作：通过数据库搜索user_id
    :param: phone_num 手机号
    :return:user_id
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    return user_id


def sql_get_seller_id(phone_num):
    """
    获取用户id
    操作：通过数据库搜索user_id
    :param: phone_num 手机号
    :return:user_id
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(uaa_authority).query_sql(sql)[0])
    return user_id


def sql_init_order(phone_num):
    """
    创建订单前，让用户无已付款有效订单
    操作：修改订单状态为取消
    :param: phone_num 手机号
    :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    DBOperate(mall).execute_sql("update tq_order set status='12' where user_id='" + user_id + "'")


def sql_delete_car_item(car_name):
    """
    创建车辆前，确保数据库无此车辆
    操作：删除数据库中的额车辆
    :param: car_name    车辆名称
    :return:
    """
    sql = "delete from tq_car_item where name='" + car_name + "'"
    DBOperate(mall).execute_sql(sql)


def sql_init_contract(response):
    """
        跳过签署合同步骤
        操作：将订单中的sub_status值改为61
        :param: order_id 订单号
        :return:
    """
    order_id = response_order_id(response)
    sql = "update tq_order set sub_status='61' where id='" + order_id + "'"
    DBOperate(mall).execute_sql(sql)


def sql_init_repayment(phone_num):
    """
        完善还款信息前，设置为未开卡过
        操作：将sign_agreement_info表中userId修改为无效id
        :param: phone_num 手机号
        :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    DBOperate(mall).execute_sql("update sign_agreement_info set user_id='" + user_id + "01' where user_id='" + user_id + "'")


def sql_init_tqtl_repayment(phone_num):
    """
    淘汽通联还款方式完善还款信息前，设置为未开卡过
    操作：将sign_agreement_info表中userId修改为无效id
    :param: phone_num 手机号
    :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    # DBOperate(mall).execute_sql("update tq_tonglian_info set user_id='" + user_id + "01' where user_id='" + user_id + "'")
    DBOperate(mall).execute_sql("delete from tq_tonglian_info where user_id='" + user_id + "'")


def sql_init_tonglian_pay(phone_num, type):
    """
    删除通联开户信息
    :param phone_num:客户手机号
    :return:
    """
    if type.upper() == 'XXF':
        pay_flatform = pay + '1004'
    if type.upper() == 'LG':
        pay_flatform = pay + '1002'
    if type.upper() == 'WX' or type.upper() == 'TQ':
        pay_flatform = pay + '1001'
    # if type.upper() == 'HX':
    #     pay_flatform = pay + '1002'
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    sql_delete_open = "delete from open_account_flow_major_record where customer_id='" + user_id + "'"
    sql_delete_sub = "delete from sub_account where target_id='" + user_id + "'"
    sql_delete_bank = "delete from bank_account where target_id='" + user_id + "'"
    DBOperate(pay_flatform).execute_sql(sql_delete_open)
    DBOperate(pay_flatform).execute_sql(sql_delete_sub)
    DBOperate(pay_flatform).execute_sql(sql_delete_bank)


def sql_init_contract_info(phone_num):
    """
        完善个人信息前将数据库中已有的联系人信息删除
        操作：将tq_user_contact_info表中相关的信息删除
        :param: phone_num 手机号
        :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    DBOperate(usercenter).execute_sql("delete from tq_user_contact_info where user_id='" + user_id + "'")


def sql_get_verify_code(transaction_no):
    """
        从数据库获取验证码
        操作：CommponentCenter.captcha表中根据transaction_no查询answer
        :param: transaction_no 接口返回transactionNo
        :return:answer
    """
    # if environment.upper() == "DEVELOP":
    #     CC = "ComponentCenter"
    # if environment.upper == "MASTER":
    CC = "saas-componentcenter"
    sql = "SELECT answer from captcha where transaction_no='" + transaction_no + "'"
    answer = str(DBOperate("saas-componentcenter").query_sql_get_verify_code(sql)[0])
    return answer


def response_order_id(response):
    """
        获取response中的order_id
        :param response:
        :return: order_id 订单号
    """
    response = response.json
    data = response[0]
    order_id = data['order']['id']
    return order_id


def save_seller_id_form_response(response):
    """
    从获取账户信息接口获取sellerId
    :param response: 接口响应
    :return:
    """
    message = BCommon.read_tmp_file(file)
    response = response.json
    sellerId = response['userId']
    message['sellerId'] = sellerId
    BCommon.write_tmp_file(file, message)

def save_carLicenseNumber_form_response(carLicenseNumber):
    """
    从获取账户信息接口获取lockCarId
    :param carLicenseNumberF: 车架号
    :return:
    """
    message = BCommon.read_tmp_file(file)
    value = carLicenseNumber
    message['carLicenseNumber'] = value
    BCommon.write_tmp_file(file, message)

def response_get_outer_key(response, phone):
    """
    获取response中的outerKey
    :param name: 客户名称
    :param response: 接口response
    :return:
    """
    message = BCommon.read_tmp_file(file)
    response = response.json
    for item in response:
        if item["phoneNum"] == phone:
            message["outerKey"] = item['outerKey']
            message["userId"] = item['userId']
            message["sellerId"] = item['sellerId']
    if len(response) == 0:
        message['skip_CleanUserId'] = True
    else:
        message['skip_CleanUserId'] = False
    BCommon.write_tmp_file(file, message)


def save_car_details_info(response, keyword):
    """
    保存车辆seriesId、typeId
    :param keyword: 车辆全称
    :param response: 接口响应
    :return:
    """
    # print('keyword', keyword)
    message = BCommon.read_tmp_file(file)
    response = response.json
    if type(response) is dict:
        message["seriesId"] = response["seriesId"]
        message["typeId"] = response["typeId"]
    elif type(response) is list:
        for item in response:
            if keyword == item["fullName"]:
                message["seriesId"] = item["seriesId"]
                message["typeId"] = item["typeId"]
    BCommon.write_tmp_file(file, message)


def get_car_full_name(brand_name, series_name, type_name):
    """
    拼接车辆全名
    :param brand_name:  品牌名
    :param series_name: 系列名
    :param type_name:   车型名
    :return:    全名
    """
    return brand_name + series_name + type_name


def save_car_info(response, brand_name, series_name, type_name):
    """
    根据name保存相关id
    :param response:    接口响应
    :param brand_name:  车辆品牌名称
    :param series_name: 车辆系列名称
    :param type_name:   车辆车型名称
    :return:
    """
    message = BCommon.read_tmp_file(file)
    response = response.json
    keyword = get_car_full_name(brand_name, series_name, type_name)
    for item in response:
        if keyword == item["fullName"]:
            message["seriesId"] = item["seriesId"]
            message["typeId"] = item["typeId"]
    BCommon.write_tmp_file(file, message)


def get_config(key):
    """
    根据key返回config.py中配置的内容
    :param key:
    :return:
    """
    value = ''
    if key == "carBrandName":
        value = carBrandName
    if key == "carFullName":
        value = carFullName
    if key == "carSeriesName":
        value = carSeriesName
    if key == "carTypeName":
        value = carTypeName
    return value


def save_contract_suite_info(response, contract_name):
    """
    保存合同套件信息
    :param contract_name: 合同套件名称
    :param response: 接口响应
    :return:
    """
    message = BCommon.read_tmp_file(file)
    contract_data = response.json
    for item in contract_data:
        if item["title"] == contract_name:
            message["contract_id"] = item["id"]
            message["contract_title"] = item["title"]
            message["contract_fundCompanyId"] = item["fundCompanyId"]
            message["contract_fundCompanyName"] = item["fundCompanyName"]
            message["contract_fundRepaymentMethod"] = item["fundRepaymentMethod"]
            message["contract_needConfirmErTable"] = item["needConfirmErTable"]
            message["contract_organizationCode"] = item["organizationCode"]
            message["contract_gmtCreate"] = item["gmtCreate"]
            message["contract_gmtModified"] = item["gmtModified"]
            message["contract_bindContractTemplates"] = item["bindContractTemplates"]
            message["contract_bindContractTemplatesDesc"] = item["bindContractTemplatesDesc"]
            message["contract_remark"] = item["remark"]
            contractFields = item["contractFields"]
            contractFields = contractFields.replace('\"value\":\"\"', '\"value\":100')
            message["contract_contractFields"] = contractFields
            message["contract_organizationCount"] = item["organizationCount"]
            message["contract_contractSuiteId"] = item["contractSuiteId"]
    BCommon.write_tmp_file(file, message)


def get_value_from_tmp(keyword):
    """
    从data/tmp.json中读取所要数据
    :param keyword: 关键字
    :return: value
    """
    # value = ""
    message = BCommon.read_tmp_file(file)
    value = message[keyword]
    print(keyword, value)
    return value


def save_organizations_info(response, keyword):
    """
    保存渠道信息到data/tmp.json
    :param response: 接口响应
    :param keyword: 要保存的参数名称
    :return:
    """
    message = BCommon.read_tmp_file(file)
    response = response.json
    organizations_info = []
    for item in response:
        organizations_info.append(item[keyword])
    message["organizations_info"] = organizations_info
    BCommon.write_tmp_file(file, message)


def save_car_id_from_response(response, keyword):
    """
    从response中提取carId保存至data/tmp.json
    :param response: 响应
    :param keyword: 车辆全名
    :return:
    """
    print('keyword', keyword)
    response = response.json
    for item in response:
        if item['name'] == keyword:
            carId = item['id']
            print(keyword, "carId:", carId)
            save_message_to_tmp("carId", carId)


def save_skip_create_car(response):
    """
    根据待售车辆数量确认是否跳过用例
    :param response: 接口响应
    :return:
    """
    message = BCommon.read_tmp_file(file)
    response = response.json
    if len(response) == 0:
        message["skip"] = False
        carNum = 1
    else:
        message["skip"] = True
        message["vin"] = response[0]["vin"]
        carNum = len(response) + 1
    message["carNum"] = carNum
    BCommon.write_tmp_file(file, message)


def save_message_to_tmp(key, value):
    """
    将键值对保存至data/tmp.json
    :param response: 接口响应
    :param key: 保存的Key
    :param value: 保存的value
    :return:
    """
    message = BCommon.read_tmp_file(file)
    message[key] = value
    BCommon.write_tmp_file(file, message)


def save_skip(response):
    """
    根据接口响应内容长度判断是否跳过接口，长度为1跳过，长度为0不跳过
    :param response: 接口响应
    :return:
    """
    response = response.json
    if len(response) == 1:
        save_message_to_tmp("skip", True)
    if len(response) == 0:
        save_message_to_tmp("skip", False)

def save_skip_CarNo(response,orderId):
    """
    根据接口响应内容判读订单所在车辆列表位置，在第一条为true,非首条记录为false
    :param response: 接口响应
    :param orderId:当前用例订单号
    :return:
    """
    response = response.json
    responseId=response[0]["orderId"]
    if responseId == orderId:
        save_message_to_tmp("skip", True)
    else :
        save_message_to_tmp("skip", False)

def save_task_process(response):
    """
    保存skus任务号
    :param response:
    :return:
    """
    response = response.json
    save_message_to_tmp("sku_process", response)


def save_selling_inventory_from_headers(response):
    """
    保存未锁定车辆数量
    :param response:
    :return:
    """
    headers = response.headers
    num = headers["X-Total-Count"]
    num = int(num)
    save_message_to_tmp("selling_inventory", num + 1)


def save_trial_token(response):
    """
    保存审核账号token至data/tmp.json文件
    :param response:    接口响应
    :return:
    """
    response = response.json
    token = response["access_token"]
    save_message_to_tmp("token", token)


def save_response_length(response):
    """
    保存response数据长度
    :param response: 接口响应
    :return:
    """
    response = response.json
    length = len(response)
    save_message_to_tmp("length", length)
    if length == 0:
        save_message_to_tmp("skip", True)
        # print("skip:true")
    else:
        save_message_to_tmp("skip", False)
        # print("skip:False")


def get_release_time():
    """
    获取车源释放时间，时间为一分钟后
    :return: release_time
    """
    timestamp = BCommon.get_time()['timestamp']
    timestamp = timestamp - 28740
    now_time = time.strftime('%Y-%m-%d%H:%M:%S', time.localtime(timestamp))
    str_date = now_time[:10]
    str_time = now_time[10:]
    release_time = str_date + "T" + str_time + ".464Z"
    return release_time


def run_master_audit_order(second=1):
    """
    master分支跑审核订单用例
    :param:second 跑用例前休眠时间
    :return:
    """
    test_login = 'testcases/order/master/nonaudit_order_count.yml'
    test_audit = 'testcases/order/master/audit_order_without_sleep.yml'
    sleep(second)
    runner.run(test_login)
    if get_value_from_tmp('skip') is False:
        runner.run(test_audit)


def run_audit_order(second=1):
    """
    develop/test分支跑审核订单用例
    :param:second 跑用例前休眠时间
    :return:
    """
    test_login = 'testcases/order/nonaudit_order_count.yml'
    test_audit = 'testcases/order/audit_order_without_sleep.yml'
    sleep(second)
    runner.run(test_login)
    if get_value_from_tmp('skip') is False:
        runner.run(test_audit)


def run_refund_order():
    """
    订单发起退款
    :return:
    """
    test_refund_release_car = 'testcases/order/master/refund_release_car.yml'
    test_refund_for_sale = 'testcases/order/master/refund_for_sale.yml'
    sleep(1)
    runner.run(test_refund_release_car)
    runner.run(test_refund_for_sale)


def run_refund_for_sale(second=1):
    """
    车辆状态为“待售”的订单发起退款
    :param second: 跑用例前休眠时间
    :return:
    """
    test = 'testcases/order/master/refund_for_sale.yml'
    sleep(second)
    runner.run(test)


def run_refund_for_release(second=1):
    """
    车辆状态为“释放车源”的订单发起退款
    :param second: 跑用例前休眠时间
    :return:
    """
    test = 'testcases/order/master/refund_release_car.yml'
    sleep(second)
    runner.run(test)


def run_get_user_message():
    """
    获取userId、outerKey等信息并保存至data/tmp.json
    :return:
    """
    test_sellerId = 'api/account/GET_Account.yml'
    test_outerKey = 'api/usercenter/users/POST_Customer.yml'
    runner.run(test_sellerId)
    runner.run(test_outerKey)


def get_value_from_response(response, key):
    """
    从接口响应中提取key对应的value保存至data/tmp.json
    :param key:
    :return:
    """
    # print(key)
    response = response.json
    value = response[key]
    # print(key, value)
    save_message_to_tmp(key, value)


def get_outer_key(response, method=1):
    """
    从完善还款信息二维码接口获取outerKey
    :param response: 接口响应
    :return:
    """
    # print(method,type(method))
    response = response.json
    value = response['url']
    if method != 1:
        start_index = value.index('outerKey=') + 8
        # end_index = value.index("'")
        outerKey = value[start_index + 1:]
        save_message_to_tmp("outerKey", outerKey)
        # print(outerKey)
    else:
        start_index = value.index('=')
        end_index = value.index('&')
        outerKey = value[start_index + 1:end_index]
        save_message_to_tmp("outerKey", outerKey)


def sql_delete_customer_info(phone_num, IDNum):
    """
    数据库中删除客户相关信息
    :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    delete_tq_dc_call_log = "delete from tq_dc_call_log where query_params_info like '%" + phone_num + "%'"
    DBOperate(usercenter).execute_sql(delete_tq_dc_call_log)
    delete_tq_marketing_info = "delete from tq_marketing_info where user_phone='" + phone_num + "'"
    DBOperate(usercenter).execute_sql(delete_tq_marketing_info)
    delete_tq_user = "delete from tq_user where phone_num='" + phone_num + "'"
    DBOperate(usercenter).execute_sql(delete_tq_user)
    delete_tq_user_seller = "delete from tq_user_seller where user_id='" + user_id + "'"
    DBOperate(usercenter).execute_sql(delete_tq_user_seller)
    select_count = "select count from tq_id_generator"
    count = str((DBOperate(usercenter).query_sql(select_count)[0]) - 1)
    print(count)
    update_count = "update tq_id_generator set count='" + count + "' where id='1'"
    DBOperate(usercenter).execute_sql(update_count)
    delete_skip_face_auth_info = "delete from skip_face_auth_info where user_id='" + user_id + "'"
    DBOperate(usercenter).execute_sql(delete_skip_face_auth_info)
    delete_tq_user_cert_detail_info = "delete from tq_user_cert_detail_info where user_id='" + user_id + "'"
    DBOperate(usercenter).execute_sql(delete_tq_user_cert_detail_info)
    delete_tq_user_contact_info = "delete from tq_user_contact_info where user_id='" + user_id + "'"
    DBOperate(usercenter).execute_sql(delete_tq_user_contact_info)
    delete_tq_user_detail_info = "delete from tq_user_detail_info where user_id='" + user_id + "'"
    DBOperate(usercenter).execute_sql(delete_tq_user_detail_info)
    delete_auth_info = "delete from auth_info where phone='" + phone_num + "'"
    DBOperate(entry_sheet).execute_sql(delete_auth_info)
    delete_tq_auth_info = "delete from tq_auth_info where customer_id_card='" + IDNum + "'"
    DBOperate(entry_sheet).execute_sql(delete_tq_auth_info)
    delete_tq_dc_call_log = "delete from tq_dc_call_log where query_params_info like '%" + phone_num + "%'"
    DBOperate(mall).execute_sql(delete_tq_dc_call_log)


def save_value_from_response(respons, num, key):
    """
    保存接口响应中第num个数据中的key关键字对应的value值至data/tmp.json
    :param respons: 接口响应
    :param num: 数据下标
    :param key: 关键字
    :return:
    """
    respons = respons.json
    data = respons[num]
    value = data[key]
    save_message_to_tmp(key, value)


def release_car(time=2):
    """
    取消订单后释放车源
    :return:
    """
    sleep(time)
    testcase = 'testcases/supply/release_car.yml'
    runner.run(testcase)


if __name__ == '__main__':
    c = CsvOperate()
    # access_token = '111222333'
    # refresh_token = '444555666'
    # CsvOperate.write_token_csv('data/token.csv', access_token, refresh_token)
    # print(CsvOperate().read_row_csv('data/token.csv', 1, 'access_token'))
    # refresh_token(source='WEB', accesstoken='111222333', refreshtoken='444555666')
    # APP = get_token('access_token',source='APP')
    # print(APP)
    # content = c.generate_text('data/token.csv', 'WEB', access_token, refresh_token)
    # c.write_token_csv('data/token.csv', content)
    # print(get_token('refresh_token'))
    # sql_init_order('15012340001')
    # sql_init_contract_info('15060138093')
    # print(type(sell), sell)
    # transcation_no = "a7767b33ecef4abb8157a522fc935401"
    # print(sql_get_verify_code(transcation_no))
    sql_init_order('16621368448')
    release_car()
