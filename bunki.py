import os

#分岐確認
var_ = 9
if var_ < 10:
    print("10未満")
else:
    print("10以上")

#現在ディレクトリの一つ上のディレクトリ一覧を取得
for i in os.listdir("../"):
    print(i)