"""
9.有一列表，列表中的元素全部为无序大小各不相同的整形数值，使用循环，将列表中的元素从小到大或从大到小排列。
"""

def sortFromSmallToLarge(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def sortFromLargeToSmall(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i -1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

if __name__ == "__main__":
    list = [3, 1, 12, 8, 5, 7]
    print("从小到大排序为：", sortFromSmallToLarge(list))
    print("从大到小排序为：", sortFromLargeToSmall(list))