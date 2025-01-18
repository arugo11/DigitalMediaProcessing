#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード、グレースケール化して, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )


#!!以下を編集する!!
kernel = np.array([[1/16, 2/16, 1/16],
                   [2/16, 4/16, 2/16],
                   [1/16, 2/16, 1/16]])

for y in range( 1, img.shape[0]-1 ) :
    for x in range( 1, img.shape[1]-1 ) :
        img_out[y,x] = (img[y-1, x-1] * kernel[0, 0] + img[y-1, x] * kernel[0, 1] + img[y-1, x+1] * kernel[0, 2] +
                         img[y, x-1] * kernel[1, 0] + img[y, x] * kernel[1, 1] + img[y, x+1] * kernel[1, 2] +
                         img[y+1, x-1] * kernel[2, 0] + img[y+1, x] * kernel[2, 1] + img[y+1, x+1] * kernel[2, 2])



#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
