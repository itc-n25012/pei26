days = ['月', '月', '火', '水', '木', '金', '金']

for cd in ['月', '金']:
    days.remove(cd) # 重複している曜日を1つ削除

days.insert(0, '日') # インデックス0に'日'を挿入
days.insert(6, '土') # インデックス6に'土'を挿入

print(days)
