#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# ハーフトーン処理（ディザ法）
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



#!!ここを編集!! : ハーフトーン画像を作成計算
#ヒント: ディザパターンは次のような２次元配列で表現できます
mask = np.array([[15,7,13,1], [4,11,5,9], [12,3,14,6], [0,8,2,10]])




#出力
cv2.imwrite( fname_out, img_out);
