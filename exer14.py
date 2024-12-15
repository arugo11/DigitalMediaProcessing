#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# ハフマン符号化
import numpy as np
import sys
import math

# 以下は木構造表現似関するヒントです。
# 解答時には不要な部分はすべて削除してください。

# ヒント : 木構造を表現するために下記のクラスを利用すると良いです（使わなくてもよいです）
# ヒント : 木構造のノードを表すクラスは以下のように定義できます。
class Node :
    def __init__(self, symbol , value) :
        self.symbol = symbol # このノードのシンボル（a~hのどれか）
        self.value  = value  # このノードの持つ値（出現確率）
        self.parent = None   # 親ノード（Noneで初期化）
        self.left   = None   # 左の子（Noneで初期化）
        self.right  = None   # 右の子（Noneで初期化）


node_a = Node("a", 0.1) #ヒント : シンボルa, 出現確率0.1のノードを初期化
node_b = Node("b", 0.3) #ヒント : シンボルb, 出現確率0.3のノードを初期化
node_c = Node("c", 0.5) #ヒント : シンボルc, 出現確率0.5のノードを初期化

# aがルート、aの左の子がb、aの右の子がcになるように木を構築
node_a.left = node_b
node_a.right = node_c
node_b.parent = node_a
node_c.parent = node_a


# 木をだどって中身を表示
print("a自身", node_a.value, node_a.symbol)
print("aの左の子", node_a.left.value, node_a.left.symbol)
print("aの右の子", node_a.right.value, node_a.right.symbol)
print("bの親", node_b.parent.value, node_b.parent.symbol)
