#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# 勾配強度画像を作成する
# I = math.sqrt(fx^2 + fy*2)
# 画素値は[0,255]の範囲に切り詰める

import numpy as np
import sys
import cv2
import math

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )


#!!ここを編集する!! img_outの各画素における勾配強度を計算する
height, width = img.shape


for y in range(1, height - 1):
    for x in range(1, width - 1):
        fx = img[y, x + 1] - img[y, x - 1]
        fy = img[y + 1, x] - img[y - 1, x]
        
        intensity = math.sqrt(fx ** 2 + fy ** 2)
        
        img_out[y, x] = min(intensity, 255)



#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
