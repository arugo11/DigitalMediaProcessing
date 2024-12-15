#
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
for y in range( 1, img.shape[0]-1 ) :
    for x in range( 1, img.shape[1]-1 ) :
        img_out[y,x] = 0
        #ヒント: 注目画素の値は img[y,x]で参照できる
        #ヒント: 注目画素(y,x)の左の画素値は img[y,x-1]で参照できる
        #ヒント: 注目画素(y,x)の上の画素値は img[y-1,x]で参照できる




#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
