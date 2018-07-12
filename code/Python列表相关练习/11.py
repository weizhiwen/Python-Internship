"""
11.创建列表，随机生成1000个1~100范围的数值放入列表中，统计列表中每个元素在列表中出现的频数。
"""

import random
list = [random.randint(0,100) for i in range(1000)]
print(list)
count = []
for a in list:
    if a not in count:  # 去重
        count.append("%s:%s" %(a, list.count(a)))
print("每个元素在列表中出现的频数", count)