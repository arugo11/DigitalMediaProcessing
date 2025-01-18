#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# ハフマン符号化
import numpy as np
import sys
import math

class Node :
    def __init__(self, symbol , value) :
        self.symbol = symbol # このノードのシンボル（a~hのどれか）
        self.value  = value  # このノードの持つ値（出現確率）
        self.parent = None   # 親ノード（Noneで初期化）
        self.left   = None   # 左の子（Noneで初期化）
        self.right  = None   # 右の子（Noneで初期化）



def main() -> None:
    with open(sys.argv[1]) as f:
        s = f.read()
        print(s)

if __name__ == '__main__':
    main()
