'''
4.与电脑玩剪刀石头布，玩家选择：1.石头，2.剪刀，3布，电脑随机选择石头、剪刀、布。判断输赢。
'''

import random

def judge(x, y):
    if(x == y):
        return 0
    elif ((x == "石头" and y == "剪刀") or (x == "剪刀" and y == "布") or (x == "布" and y == "石头")):
        return 1
    else:
        return -1

print("欢迎来到石头剪刀布游戏\n"
      "输入规则如下：\n"
      "1.石头"
      "2.剪刀"
      "3.布"
      )

list = ["石头", "剪刀", "布"]
playerOut = 0

while 1:
    try:
        playerOut = int(input("你出"))
        playerOut = list[playerOut - 1]
    except ValueError:
        print("输入为非整数！")
    except IndexError:
        print("没有按规则输入")
    else:
        computerOut = random.choice(list)
        flag = judge(playerOut, computerOut)
        if flag == 0:
            print("平局，你和电脑都是出的 ", playerOut)
        elif flag == 1:
            print("你赢了，你出的", playerOut, "，电脑出的", computerOut)
        elif flag == -1:
            print("你输了，你出的", playerOut, "，电脑出的", computerOut)
        isContinue = input("是否继续游戏？y/n")
        if(isContinue == "n" or isContinue == "N"):
            break
print("游戏结束，欢迎下次再玩！")

