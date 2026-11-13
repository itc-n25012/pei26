def func(a, b):
    if a ** b <= 64:
        return 1
    else: 
        return 0
x = func(4, 3) # 4 ** 3 = 64 return 1
y = func(3, 4) # 3 ** 4 = 81 return 0
a = func(-5, -6) # -5 ** -6 = -(1/5^6) 累乗**は単項マイナス-よりも優先順位が高い
z = [bool(x), bool(y), bool(a)] # ※ 基本的に、0や空の値ではないものはTrue
print(z) # z = [True, False, True]


