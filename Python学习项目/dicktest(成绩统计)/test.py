"""
result[course][max/min/sum/count]
result["语文"]["max"] = 99
result["语文"]["min"] = 99
result["语文"]["sum"] = 99
result["语文"]["count"] = 99
result["数学"]["max"] = 99
result["数学"]["min"] = 99
result["数学"]["sum"] = 99
result["数学"]["count"] = 99
result["英语"]["max"] = 99
result["英语"]["min"] = 99
result["英语"]["sum"] = 99
result["英语"]["count"] = 99
"""
# a = open("testdata.txt",encoding='UTF-8')
# for yulan in a:
#     print(yulan)
result = {}
with open("testdata.txt",encoding='UTF-8') as fin:
    for line in fin:
        # line = line.strip()#删空格
        fields = line.split("\t")#分隔
        # print(fields)
        name,subject,score = fields#拆包
        if subject not in result:
            result[subject] = {}
            result[subject]["max"] = 0
            result[subject]["min"] = 999
            result[subject]["sum"] = 0
            result[subject]["count"] = 0

        score = int(score)
        if score > result[subject]["max"]:
            result[subject]["max"] = score
        elif score < result[subject]["min"]:
            result[subject]["min"] = score
        result[subject]["sum"] += score
        result[subject]["count"] += 1

for key,value in result.items():
    print(key,value)

    out_field = [
        key,
        value["max"],
        value["min"],
        value["sum"]/value["count"],
    ]
    print(out_field)