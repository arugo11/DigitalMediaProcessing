#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# ハーフトーン処理(誤差拡散法)
import numpy as np
import cv2
import sys

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み、グレースケール化し、float型に変換
img = cv2.imread( fname_in  )
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)


#出力画像を準備
H = img.shape[0] # type: ignore
W = img.shape[1] # type: ignore
img_out = np.zeros((H,W), np.uint8)



#誤差拡散法の計算
THRESHOLD = 127
DIFFUSION_PIXELS: list[tuple[int, int, float]] = \
[(0, 1, 5/16), (1, -1, 3 / 16), (1, 0, 5 / 16), (1, 1, 3 / 16)]
for y in range(H)  :
	for x in range( W)  :
		#!!ここを編集!!
		#ヒント: 閾値処理部分と誤差拡散部分に分けて考えると分かりやすい
		#ヒント: 誤差は元画像 img に足していくとよいかも（好きにしてよい）
		if  img[y][x] > THRESHOLD: #type:ignore
			err: int = img[y][x] - 255 #type:ignore
			img[y][x] = 255 #type:ignore
		else:
			err: int = img[y][x] - 0 #type:ignore
			img[y][x] = 0 #type:ignore


		for dy, dx, weight in DIFFUSION_PIXELS:
			if 0 <= y+dy < H and 0 <= x+dx < W:
				img[y+dy][x+dx] += weight * err #type:ignore

img_out = np.array(img)



cv2.imwrite( fname_out, img_out)
