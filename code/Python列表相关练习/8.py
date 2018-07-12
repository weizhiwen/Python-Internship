"""
8.使用列表完成杨辉三角形
"""

def printLine(list, n):
    list = [str(temp) for temp in list]
    print("%s%s" %(" " * (n - len(list)), " ".join(list)))

def triangle(n):
    for i in range(n):
        if i < 2:
            list = [1] * (i + 1)
        else:
            list[1:-1] = [(temp + list[j]) for j, temp in enumerate(list[1:])]
        printLine(list, n)

print("杨辉三角")
triangle(10)