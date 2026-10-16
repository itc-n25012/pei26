ip_address = '192.168.3.1'
ip_spl = ip_address.split('.')
bin_exp = ''
for num in ip_spl:
    bin_exp += bin(int(num))[2:] + '.'
print(bin_exp[:-1])
print(type(bin_exp))

'''メモ
splitメソッドは引数で指定された文字で分割し、リストを作る。
bin()関数とは2進数の文字列に変換する
int()関数とは文字列を整数に変換する

スライスについて[2:]はインデックス2以降を取得
スライスについて[:-1]は末尾1文字を取り除いて取得
'''
