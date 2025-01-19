#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# ハフマン符号化
import numpy as np
import sys
import math

class Node :
    def __init__(self, symbol , value)  -> None:
        self.symbol:str|None = symbol # このノードのシンボル（a~hのどれか）
        self.value:int  = value  # このノードの持つ値（出現確率）
        self.parent:Node|None = None   # 親ノード（Noneで初期化）
        self.left:Node|None   = None   # 左の子（Noneで初期化）
        self.right:Node|None  = None   # 右の子（Noneで初期化）



def main() -> None:
    with open(sys.argv[1]) as f:
        s:str = f.read()
    # print(s)


    table: dict[str, int] = {key:0 for key in set(list(s))}

    for i in s:
        table[i] += 1

    nodes: list[Node] = []
    for symbol, value in table.items():
        nodes.append(Node(symbol=symbol,value=value))

    while len(nodes) > 1:
        nodes.sort(key = lambda x:x.value)
        # left_node < right_node
        left_node:Node = nodes.pop(0)
        right_node:Node = nodes.pop(0)

        parent_node:Node = Node(
            symbol=None,
            value=(right_node.value + left_node.value)
        )

        parent_node.left = left_node
        parent_node.right = right_node
        left_node.parent = parent_node
        right_node.parent = parent_node

        nodes.append(parent_node)


    def generate_codes(node: Node, code: str = "") -> None:
        if node.symbol is not None:
            huffman_coding[node.symbol] = code
            return

        if node.left:
            generate_codes(node.left, code + "1")
        if node.right:
            generate_codes(node.right, code + "0")

    huffman_coding:dict[str,str] = {}
    root_node = nodes[0]
    generate_codes(root_node)

    with open(sys.argv[2], mode='w') as f:
        for _, value  in sorted(huffman_coding.items()):
            f.write(f"{value}\n")
if __name__ == '__main__':
    main()
