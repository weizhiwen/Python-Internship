"""
6.编写一个函数，计算字符串中字符的个数
"""

def countChar(str):
    count={}
    for i in str:
        count[i] = str.count(i)
    return count

str=input("请输入一串字符:")
print(countChar(str))