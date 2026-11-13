# 問４の(18)
a = 0b10111
b = 0b11101
c = a | b
print(c)

# 問４の(19)
a = 6
b = pow(a, 3) # 6の3乗
c = divmod(b, a)
print(c)

# 問４の(20)
num = 3
list_a = []
while num < 5:
    for i in range(num, 10, 3):
        i -= 6
        list_a.append(i)
    num += 1
print(sum(list_a))
'''計算欄
num=3のときのforループ処理
3,6,9それぞれ-6してappendするので、[-3, 0, 3]

num=4のときのforループ処理
4,7それぞれ-6してappendするので、[-2, 1]

最終的に、list_a = [-3, 0, 3, -2, 1]
sum(list_a) = -1
'''

# 問４の(21)
list_a = [4, 8, 3, 7, 9]
list_b = [10, 3, 6, 7, 2]
list_c = []
i = 0
while i < 5:
    if list_a[i] > list_b[i]:
        list_c.append(list_a[i] - list_b[i] ** 2)
    elif list_a[i] == list_b[i]:
        list_c.append(list_a[i] * 2 % 4)
    else:
        list_c.append((list_b[i] - list_a[i]) // 2)
    i += 1
print(max(list_c))
'''計算欄
4と10: (10 - 4) // 2 = 3
8と3 : (8 - 3 ** 2) = -1
3と6 : (6 - 3) // 2 = 1
7と7 : 7 * 2 % 4 = 14 % 4 = 2
9と2 : (9 - 2 ** 2) = 5
list_c = [3, -1, 1, 2, 5]
max(list_c) = 5
'''

# 問４の(22)


# 問４の(23)


# 問４の(24)
