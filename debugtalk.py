import time
from common.BaseCommon import BaseCommon as BCommon
from common.CsvOperate import CsvOperate
from common.DBOperate import DBOperate
from config import *

log = BCommon.log()
file = 'data/tmp.json'


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


def tmp_file_get_brand_id():
    """
    从data/tmp.json读取brandId
    :return: brand_id
    """
    message = BCommon.read_tmp_file("data/tmp.json")
    brand_id = message["brand_id"]
    return brand_id


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


def add(x, y) -> str:
    """
    对两个数相加
    :param x:
    :param y:
    :return:
    """
    return str(int(x)+y)


def sql_get_user_id(phone_num):
    """
    获取用户id
    操作：通过数据库搜索user_id
    :param: phone_num 手机号
    :return:user_id
    """
    sql = "SELECT user_id from tq_user where phone_num='"+phone_num+"'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    return user_id


def sql_get_seller_id(phone_num):
    """
    获取用户id
    操作：通过数据库搜索user_id
    :param: phone_num 手机号
    :return:user_id
    """
    sql = "SELECT user_id from tq_user where phone_num='"+phone_num+"'"
    user_id = str(DBOperate(uaa_authority).query_sql(sql)[0])
    return user_id


def sql_init_order(phone_num):
    """
    创建订单前，让用户无已付款有效订单
    操作：修改订单状态为取消
    :param: phone_num 手机号
    :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='"+phone_num+"'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    DBOperate(mall).execute_sql("update tq_order set status='12' where user_id='"+user_id+"'")


def sql_init_contract(response):
    """
        跳过签署合同步骤
        操作：将订单中的sub_status值改为61
        :param: order_id 订单号
        :return:
    """
    order_id = response_order_id(response)
    sql = "update tq_order set sub_status='61' where id='"+order_id+"'"
    DBOperate(mall).execute_sql(sql)

def sql_init_repayment(phone_num):
    """
        完善还款信息前，设置为未开卡过
        操作：将sign_agreement_info表中userId修改为无效id
        :param: phone_num 手机号
        :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='"+phone_num+"'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    DBOperate(mall).execute_sql("update sign_agreement_info set user_id='"+user_id+"01' where user_id='"+user_id+"'")

def sql_init_contract_info(phone_num):
    """
        完善个人信息前将数据库中已有的联系人信息删除
        操作：将tq_user_contact_info表中相关的信息删除
        :param: phone_num 手机号
        :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='" + phone_num + "'"
    user_id = str(DBOperate(usercenter).query_sql(sql)[0])
    DBOperate(usercenter).execute_sql("delete from tq_user_contact_info where user_id='"+user_id+"'")

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
    message = BCommon.read_tmp_file(file)
    response = response.json
    for item in response:
        if keyword == item["fullName"]:
            message["seriesId"] = item["seriesId"]
            message["typeId"] = item["typeId"]
    BCommon.write_tmp_file(file, message)


def get_car_full_name(brand_name, series_name, type_name):
    """
    拼接车辆全名
    :param brand_name:
    :param series_name:
    :param type_name:
    :return:
    """
    return brand_name + series_name + type_name


def save_car_info(response, brand_name, series_name, type_name):
    """

    :param response:
    :param brand_name:
    :param series_name:
    :param type_name:
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


def get_series_id():
    """
    从tmp文件读取保存的series_id
    :return: series_id
    """
    message = BCommon.read_tmp_file(file)
    series_id = message["seriesId"]
    return series_id


def get_type_id():
    """
    从tmp文件读取保存的type_id
    :return: type_id
    """
    message = BCommon.read_tmp_file(file)
    type_id = message["typeId"]
    return type_id


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
    if key == "addCarFullName":
        value = addCarFullName
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
    value = ""
    message = BCommon.read_tmp_file(file)
    value = message[keyword]
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
    BCommon.write_tmp_file(file,message)


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
    key = "vin"
    message = BCommon.read_tmp_file(file)
    message[key] = 123
    BCommon.write_tmp_file(file, message)


