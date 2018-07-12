"""
7.编写一个函数，输入一个字符串内容，返回反转的字符
"""

def myReverse(str):
    return str[::-1]

if __name__ == "__main__":
    str = input("请输入一个字符串")
    print("字符串反转后的字符为", myReverse(str))