import io
import json
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def get_message():
    file = "summary.json"
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
    f.close()
    status = data["success"]
    totalNum = data["stat"]["testcases"]["total"]
    successNum = data["stat"]["testcases"]["success"]
    failNum = data["stat"]["testcases"]["fail"]
    if status == 0:
        status = 'Fail'
    if status == 1:
        status = 'Success'
    message = " 【自动化执行结果】-  RESULT: %s  -  TOTAL: %s  -  SUCCESS: %s  -  FAIL: %s" % (status, totalNum, successNum, failNum)
    return message


msg = get_message()
print(msg)

