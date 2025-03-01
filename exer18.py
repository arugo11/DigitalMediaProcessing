#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# ハーフトーン処理（濃度パターン法）
import numpy as np
import cv2
import sys


fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロードしてグレースケール化
img = cv2.imread( fname_in )
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#出力画像を準備
H = img.shape[0]
W = img.shape[1]
img_out = np.zeros((H,W), np.uint8)

#濃度パターン
pattern = np.array(
	[ [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], #0
	  [[1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], #1
	  [[1,0,0,0], [0,0,0,0], [0,0,0,0], [1,0,0,0]], #2
	  [[1,0,0,0], [0,0,0,0], [0,0,0,0], [1,0,1,0]], #3
	  [[1,0,0,0], [0,0,1,0], [0,0,0,0], [1,0,1,0]], #4
	  [[1,0,0,0], [1,0,1,0], [0,0,0,0], [1,0,1,0]], #5
	  [[1,0,0,0], [1,0,1,0], [0,1,0,0], [1,0,1,0]], #6
	  [[1,0,0,1], [1,0,1,0], [0,1,0,0], [1,0,1,0]], #7
	  [[1,0,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]], #8
	  [[1,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]], #9
	  [[1,1,0,1], [1,0,1,0], [0,1,0,1], [1,1,1,0]], #10
	  [[1,1,0,1], [1,0,1,1], [0,1,0,1], [1,1,1,0]], #11
	  [[1,1,0,1], [1,0,1,1], [0,1,0,1], [1,1,1,1]], #12
	  [[1,1,0,1], [1,1,1,1], [0,1,0,1], [1,1,1,1]], #13
	  [[1,1,0,1], [1,1,1,1], [1,1,0,1], [1,1,1,1]], #14
	  [[1,1,1,1], [1,1,1,1], [1,1,0,1], [1,1,1,1]], #15
	  [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]] ]) #16
pattern *= 255


#!!ここを編集!!
#ハーフトーン画像を作成計算
#img_outの各ブロックを埋める

def which_pattern(block) -> int:
    avg = np.mean(block)
    return int(avg / 255 * 17)

def density_pattern(img, block_size:int = 4):
    result = np.zeros_like(img)
    for y in range(0, img.shape[0] - block_size + 1, block_size):
        for x in range(0, img.shape[1] - block_size + 1, block_size):
            result[y:y+block_size, x:x+block_size] = \
            pattern[which_pattern(img[y:y+block_size, x:x+block_size])]
    return result


img_out = density_pattern(img)

#出力
cv2.imwrite( fname_out, img_out)
