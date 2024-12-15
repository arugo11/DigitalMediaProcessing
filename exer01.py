#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import sys

#二つの数値をコマンドライン引数から受け取る
#sys.argv[1]は文字列なので　int( X ) 関数で型変換
a = int(sys.argv[1])
b = int(sys.argv[2])


# !!以下を編集!!

#a*b回だけ 　hello, world  と表示する
#余計なものは表示しないようにしてください
#(提出時に下のprint(a,b)は消してください)
[print("hello, world") for _ in range(a*b)]
