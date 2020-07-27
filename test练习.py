page_info_dict = {}
with open("page_info.txt",encoding="utf-8") as fin:
    for line in fin:
        line = line.strip()
        page_name,page_phone = line.split("、")
        page_info_dict[page_name] = page_phone
print (page_info_dict)


# 获取日期
str = "2019-01-03 23:00:47"
a = str.split(" ")[0]
print(a)



"""
result = {{pdate,page_id}:{"pv":123,"uv":123}}
"""
with open("blog_access.log") as fin:
   for line in fin:
       line = line.strip()
       pdatetime,user_id,page_id,event = line.split(/t)
       if event = "click":
           continue
        pdatetime = "2020-07-19 17:49"
        pdate = pdatetime.split(" ")[0]
        print(pdate)
       Key = (pdate,page_id)