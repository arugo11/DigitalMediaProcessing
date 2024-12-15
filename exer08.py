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
# N = 100程度の入力であれば、速度は気にせず実装しても問題なく動作するはずです。


#save image
cv2.imwrite(fname_out, img )
