'''
1.打印1~100的偶数和奇数的和
'''

evenSum = 0
oddSum = 0
i = 0

for i in range(1, 101):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i

print("1~100 的偶数和为",evenSum)
print("1~100 的奇数和为",oddSum)