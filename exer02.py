#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import sys

#1つの数値をコマンドライン引数から受け取る
N = int(sys.argv[1])


# !!このfor文の中を編集!!
for i in range(1,N+1):
    if (i % 3 == 0) and (i % 5 == 0):print("hogefuga")
    elif i % 3 == 0:print("hoge")
    elif i % 5 == 0: print("fuga")
    else: print(i)