#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import sys
import math
import statistics

#ファイル名をコマンドライン引数から受け取る
file_in  = sys.argv[1]
file_out = sys.argv[2]

# 先ずファイルを読み込む(今回は雛形に書いておきます)
data_array: list[float] = [] #dataを入れる配列

f = open(file_in, "r")
lines = f.readlines()
for line in lines:
    data_array.append( float(line) ) #本来は例外処理が必要ですが省略



# !!ここを編集!!
# ヒント : ライブラリ関数を使ってもOK，for文を使ってもOK
# print(data_array)
maxV: float = max(data_array)
meanV: float = sum(data_array) / len(data_array)

data_array.sort()

print(maxV, meanV)
print( str(data_array[0]) + " " + str(data_array[1]) + " " + str(data_array[2]))



#fileにmaxV minV, meanVを書き出す
# (ヒントを出しすぎかもしれませんが)今回は雛形に書いておきます
f = open(file_out, "w")
f.write( str(maxV) + " " + str(meanV) )
f.write( str(data_array[0]) + " " + str(data_array[1]) + " " + str(data_array[2]) )
f.close()
