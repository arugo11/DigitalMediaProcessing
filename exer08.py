#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import cv2

#load image
img_size  = int(sys.argv[1])
fname_out = sys.argv[2]

#真っ黒な画像を作成
img = np.zeros((img_size, img_size), dtype = np.uint8)


#!!ここを編集
# 素数判定関数
def is_prime(n):
    if isinstance(n, np.ndarray):
        return np.array([is_prime(x) for x in n.flat]).reshape(n.shape)
    if n < 2: return False
    return not any(n % i == 0 for i in range(2, int(np.sqrt(n)) + 1))

# インデックス行列の生成
index_mat = np.zeros((img_size, img_size), dtype=int)
num = 1

# 左下から右上への斜めパターンで値を設定
for sum_idx in range(2 * img_size - 1):
    for i in range(img_size):
        j = sum_idx - i
        if 0 <= j < img_size:
            index_mat[img_size - 1 - i][j] = num
            num += 1

# 素数の位置を白(255)に設定
prime_positions = is_prime(index_mat)
img[prime_positions] = 255
#save image
cv2.imwrite(fname_out, img )
