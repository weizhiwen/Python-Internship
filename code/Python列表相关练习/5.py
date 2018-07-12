"""
5.使用函数完成斐波拉契的输出前10个数
"""

def fibonacci(n):
    a = 0
    b = 1
    list = []
    list.append(b)
    for i in range(1, n):
        c = a + b
        list.append(c)
        a = b
        b = c
    return list

if __name__ == "__main__":
    print("前10个斐波拉契数为：", fibonacci(10))
