"""
10.使用input()在控制台接收三次输入的网站地址，使用列表模拟浏览器的前进后退功能，按照输入的网站地址顺序，可进行前进或后退。
"""

list = []
for i in range(3):
    list.append(input("请输入网站地址："))
index = 2
print("模拟浏览器行为\n"
      "1: 前进\n"
      "-1: 后退n\n"
      "0: 关闭浏览器")
while True:
    flag = input("你想做什么")
    if(flag == "1"):
        if(index >= 2):
            print("已经是最后一个网址，不能前进")
        else:
            print("当前网址为", list[index + 1])
            index += 1
    elif(flag == "-1"):
        if(index <= 0):
            print("已经是第一个网址，不能后退")
        else:
            print("当前网址为", list[index - 1])
            index -= 1
    elif(flag == "0"):
        print("已关闭浏览器")
        break
    else:
        print("没有按照规则输入")