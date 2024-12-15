#
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
H = img.shape[0]
W = img.shape[1]
img_out = np.zeros((H,W), np.uint8)



#誤差拡散法の計算
for y in range(H)  :
	for x in range( W)  :
		#!!ここを編集!!
		#ヒント: 閾値処理部分と誤差拡散部分に分けて考えると分かりやすい
		#ヒント: 誤差は元画像 img に足していくとよいかも（好きにしてよい）





cv2.imwrite( fname_out, img_out);
