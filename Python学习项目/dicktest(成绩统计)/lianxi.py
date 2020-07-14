result = {}
with open("testdata.txt",encoding="UTF-8") as data:
    for line in data:
        Achievement_statistics = line.strip().split("\t")
        name,subject,score = Achievement_statistics
        score = int(score)
        if subject not in result:
            result[subject] = {}
            result[subject]["max"] = 0
            result[subject]["min"] = 999
            result[subject]["sum"] = 0
            result[subject]["count"] = 0
        if score > result[subject]["max"]:
            result[subject]["max"] = score
        elif score < result[subject]["min"]:
            result[subject]["min"] = score
        result[subject]["sum"] += score
        result[subject]["count"] += 1

for key,value in result.items():
    print(key,value)
    out_Achievement_statistics = [
    key,
    value["max"],
    value["min"],
    value["sum"]/value["count"]
    ]
    print(out_Achievement_statistics)