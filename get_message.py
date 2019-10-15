import json

def get_message():
    file = "summary.json"
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
    f.close()
    status = data["success"]
    totalNum = data["stat"]["testcases"]["total"]
    successNum = data["stat"]["testcases"]["success"]
    failNum = data["stat"]["testcases"]["fail"]
    message = "【自动化执行结果】： %s\r\nTOTAL: %s\r\nSUCCESS: %s\r\nFAIL: %s" %(status,totalNum,successNum,failNum)
    return message

#
# if __name__ == '__main__':
#     data = get_message()
#     print(data)


