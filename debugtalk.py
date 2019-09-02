from common.CsvOperate import CsvOperate
import time


def sleep(n_secs):
    time.sleep(n_secs)


def refresh_token(accesstoken, refreshtoken):
    """
    每次调用登录接口都更新一次csv的token
    :param access_token:
    :param refresh_token:
    :return:
    """
    # 获取当前日期
    # now_date = get_time()['now_date']
    # 获取csv中当前日期
    CsvOperate().write_token_csv('data/token.csv', accesstoken, refreshtoken)


def get_token(token_type):
    """
    从csv文件获取最新的token值
    :param token_type:"access_token"或"refresh_token"
    :return: token值
    """
    if token_type == 'access_token':
        access_token_value: str = CsvOperate().read_row_csv('data/token.csv', 1, 'access_token')
        return access_token_value
    elif token_type == 'refresh_token':
        refresh_token_value: str = CsvOperate().read_row_csv('data/token.csv', 1, 'refresh_token')
        return refresh_token_value
    else:
        print('仅支持获取"access_token"和"refresh_token"，请检查输入')


if __name__ == '__main__':
    # access_token = '111222333'
    # refresh_token = '444555666'
    # CsvOperate.write_token_csv('data/token.csv', access_token, refresh_token)
    # print(CsvOperate().read_row_csv('data/token.csv', 1, 'access_token'))
    refresh_token(accesstoken='111222333', refreshtoken='444555666')
    get_token('access_token')

