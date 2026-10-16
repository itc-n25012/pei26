animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
    is_long = len(animal) > 5
    if from_D and is_long: # from_DがTrueかつis_longがTrue
        break
    elif not from_D and is_long: # from_DがFalseかつis_longがTrue
        total += animal.find('b')
    else:
        total += len(animal)
    print(f'totalの値は{total}')
print(total)

'''メモ
startwith('D')メソッドについて、今回は'D'で始まっていたらTrue、そうでなければFalseを返す
find('b')メソッドについて、bが最初に見つかったインデックスを返す。見つからなければ、-1を返す
'''
