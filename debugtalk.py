from common.CsvOperate import CsvOperate
import time
from common.BaseCommon import BaseCommon
from common.DBOperate import DBOperate

log = BaseCommon().log()


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


def sql_init_order(phone_num):
    """
    创建订单前，让用户没有订单信息
    操作：修改订单中的用户id为无效id
    :param: phone_num 手机号
    :return:
    """
    sql = "SELECT user_id from tq_user where phone_num='"+phone_num+"'"
    user_id = str(DBOperate("usercenter_1001").query_sql(sql)[0])
    DBOperate("mall_1001").execute_sql("update tq_order set user_id='"+user_id+"01' where user_id='"+user_id+"'")


if __name__ == '__main__':
    c = CsvOperate()
    # access_token = '111222333'
    # refresh_token = '444555666'
    # CsvOperate.write_token_csv('data/token.csv', access_token, refresh_token)
    # print(CsvOperate().read_row_csv('data/token.csv', 1, 'access_token'))
    # refresh_token(source='WEB', accesstoken='111222333', refreshtoken='444555666')
    # get_token('access_token')
    # content = c.generate_text('data/token.csv', 'WEB', access_token, refresh_token)
    # c.write_token_csv('data/token.csv', content)
    # print(get_token('refresh_token'))
    sql_init_order('15060138093')


