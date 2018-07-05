'''
2.使用for循环打印九九乘法表
'''

# 方法一
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d " %(j, i, i * j), end=" ")
    print("\n")

# 方法二
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d * %d = %d " %(j, i, i * j), end=" ")
        j += 1
    i += 1
    print("\n")
