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
    steps_totalNum = data["stat"]["teststeps"]["total"]
    steps_failNum = data["stat"]["teststeps"]["failures"]
    steps_errorNum = data["stat"]["teststeps"]["errors"]
    steps_skipNum = data["stat"]["teststeps"]["skipped"]
    steps_successNum = steps_totalNum - steps_failNum - steps_errorNum - steps_skipNum
    if status == 0:
        status = 'Fail'
    if status == 1:
        status = 'Success'
    message = "【自动化执行结果】=  RESULT: %s  =  TOTAL: %s  =  SUCCESS: %s  =  FAIL: %s  =  TESTSTEPS：total-%s  success-%s  " \
              "fail-%s  error-%s  skip-%s" % (status, totalNum, successNum, failNum, steps_totalNum, steps_successNum,
                                              steps_failNum, steps_errorNum, steps_skipNum)
    return message


msg = get_message()
print(msg)

