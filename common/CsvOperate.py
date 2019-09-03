import csv
import os

from common.BaseCommon import BaseCommon


class CsvOperate(BaseCommon):
    def read_csv(self, file_name):
        """
        读取csv文件
        :param:file_name,文件路径
        :return:content list，读取的文件内容
        """
        with open(file_name, 'r+') as f:
            try:
                render = csv.DictReader(f)
                return [row for row in render]
            finally:
                f.close()

    def read_row_csv(self, file_name, row_num, field):
        """
        获取csv文件第row_num行数据的某个字段
        :param file_name:文件路径文件名
        :param row_num: 第几行数据，从1开始
        :param field:读取的列名
        :return:字段值
        """
        csv_dict = self.read_csv(file_name)
        value = csv_dict[int(row_num-1)][field]
        self.log().debug("获取字段【%s】的值是【%s】" % (field, value))
        return value

    def write_token_csv(self, file_name, source, access_token, refresh_token):
        """
        写入token信息到csv文件
        :param file_name:文件路径
        :param access_token:写入access_token
        :param refresh_token:写入refresh_token
        :param source:平台来源：app/web
        :return:
        """
        now_time = self.get_time()['now_time']
        now_day = self.get_time()['now_date']
        self.log().debug('写入的平台是：【%s】,access_token是:【%s】, refresh_token是:【%s】' % (source, access_token, refresh_token))
        content_dict = [{'create source': source, 'create time': now_time,
                         'access_token': access_token, 'refresh_token': refresh_token}]
        with open(file_name, 'w+') as f:
            try:
                lines = f.readlines()
                # 如果文件是空的，则增加文件头
                if lines < 1:
                    headers = [k for k in content_dict[0]]
                    writer = csv.DictWriter(f, fieldnames=headers)
                    writer.writeheader()
                for line in lines:


                    for item in content_dict:
                        writer.writerow(item)
            finally:
                f.close()







