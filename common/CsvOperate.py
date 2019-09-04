import csv
from common.BaseCommon import BaseCommon


class CsvOperate(BaseCommon):
    def read_csv(self, file_name):
        """
        读取csv文件
        :param:file_name,文件路径
        :return:content list，读取的文件内容
        返回格式：[OrderedDict([('create source', 'WEB'), ('create time', '22'),
                ('access_token', '333'), ('refresh_token', '444')]),
                OrderedDict([('create source', 'APP'), ('create time', 'aaa'),
                ('access_token', 'bbb'), ('refresh_token', 'ccc')])]
        """
        with open(file_name, 'r') as f:
            try:
                render = csv.DictReader(f)
                return [row for row in render]
            finally:
                f.close()

    def read_row_csv(self, file_name, source, field):
        """
        获取csv文件第row_num行数据的某个字段
        :param file_name:文件路径文件名
        :param row_num: 第几行数据，从1开始
        :param field:读取的列名
        :return:字段值
        """
        csv_list = self.read_csv(file_name)
        for item_list in csv_list:
            # 如果是传入的平台，则更新
            if item_list["create source"] == str(source).upper():
                value = item_list[field]
        self.log().debug("获取字段【%s】的值是【%s】" % (field, value))
        return value

    def generate_text(self, file_name, source, access_token, refresh_token):
        """
        生成需要写入csv的文本内容
        :param file_name:
        :param source:平台 WEB或APP
        :param access_token:  需要更新的access_token
        :param refresh_token: 需要更新的refresh_token
        :return:文本内容
        返回格式：[{'create source': 'WEB', 'create time': '2019-09-04 15:24:01', 'access_token': '111', 'refresh_token': '222'},
                 {'create source': 'APP', 'create time': '2019-09-04 15:14:05', 'access_token': '555', 'refresh_token': '666'}]
        """
        csv_list: list = self.read_csv(file_name)
        self.log().debug("读取的内容是：【%s】" % csv_list)
        self.log().debug("需要更新的平台是：【%s】" % source)
        dict1 = {}
        dict2 = {}
        for item_list in csv_list:
            # 如果是传入的平台，则更新
            if item_list["create source"] == str(source).upper():
                now_time = self.get_time()['now_time']
                self.log().debug('写入的access_token是:【%s】, refresh_token是:【%s】' % (access_token, refresh_token))
                item_list["access_token"] = access_token
                item_list["refresh_token"] = refresh_token
                item_list["create time"] = now_time
                for item in item_list:
                    dict1[item] = item_list[item]
            else:
                for item in item_list:
                    dict2[item] = item_list[item]
        return [dict1, dict2]

    def write_token_csv(self, file_name, content):
        """
        读取的内容写入文件
        :param file_name: 文件路径
        :param content: 需要写入的内容，格式为[{'create source': 'WEB'},{'create source': 'APP'}]
        :return:
        """
        with open(file_name, 'w+') as f:
            try:
                headers = [k for k in content[0]]
                w_csv = csv.DictWriter(f, fieldnames=headers)
                # 写入文件头
                w_csv.writeheader()
                for item in content:
                    w_csv.writerow(item)
            finally:
                f.close()

