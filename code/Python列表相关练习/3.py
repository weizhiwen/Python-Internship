'''
3.设计一个猜数字游戏，每次随机生成一个1~20的秘密数字，玩家有6次猜测机会，如果猜测数大于秘密数字，则提示猜测数字太大，
  如果猜测数字小于秘密数字，则提示猜测数字太小，如果刚好猜测就提示猜测成功，如果6次都未猜测则告知实际数字。
'''

import random

randomNum = random.randint(1, 20)
# print(randomNum)
print("欢迎来到猜数字游戏")
i = 0
for i in range(0, 6):
    try:
        guessNum = int(input("请输入 1~20 的整数"))
        if guessNum == randomNum:
            print("恭喜你，猜对啦！")
            break
        elif guessNum < randomNum:
            print("猜小啦，继续努力！")
        elif guessNum > randomNum:
            print("猜大啦，继续努力！")
    except Exception:
        print("输入为非整数！")

print("已猜次数 %d"%(i + 1))
if i == 6:
    print("已经猜错 6 次，正确数字为 %d" %randomNum)
print("游戏结束")
