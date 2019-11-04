import datetime
import io
import json
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def get_message():
    file = "summary.json"
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
    f.close()
    start_at = data['time']['start_at']
    timeArray = time.localtime(start_at)
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
    duration = data['time']['duration']
    status = data["success"]
    totalNum = data["stat"]["testcases"]["total"]
    successNum = data["stat"]["testcases"]["success"]
    failNum = data["stat"]["testcases"]["fail"]
    steps_totalNum = data["stat"]["teststeps"]["total"]
    steps_failNum = data["stat"]["teststeps"]["failures"]
    steps_errorNum = data["stat"]["teststeps"]["errors"]
    steps_skipNum = data["stat"]["teststeps"]["skipped"]
    steps_successNum = data["stat"]["teststeps"]["successes"]
    steps_expectedFailuresNum = data["stat"]["teststeps"]["expectedFailures"]
    steps_unexpectedSuccessesNum = data["stat"]["teststeps"]["unexpectedSuccesses"]
    if status == 0:
        status = 'Fail'
    if status == 1:
        status = 'Success'
    message = "【自动化执行结果】=  RESULT: %s  =  TOTAL: %s  =  SUCCESS: %s  =  FAIL: %s  =  TESTSTEPS：total-%s  success-%s " \
              "fail-%s  error-%s  skip-%s  expectedFailures-%s  unexpectedSuccesses-%s " \
              % (status, totalNum, successNum, failNum, steps_totalNum, steps_successNum, steps_failNum,
                 steps_errorNum, steps_skipNum, steps_expectedFailuresNum, steps_unexpectedSuccessesNum)
    # message = "【自动化执行结果】=  RESULT: %s  =  TOTAL: %s  =  SUCCESS: %s  =  FAIL: %s  =  TESTSTEPS：total-%s  success-%s " \
    #           "fail-%s  error-%s  skip-%s  expectedFailures-%s  unexpectedSuccesses-%s = start_time:%s = " \
    #           "duration:%sS" % (status, totalNum, successNum, failNum, steps_totalNum, steps_successNum, steps_failNum,
    #                             steps_errorNum, steps_skipNum, steps_expectedFailuresNum, steps_unexpectedSuccessesNum,
    #                             start_time, round(duration, 2))
    return message


msg = get_message()
print(msg)

