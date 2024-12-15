#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import cv2

#load image
fname_in  = sys.argv[1]
fname_out = sys.argv[2]
img = np.float32( cv2.imread(fname_in) )

#grayscale画像の作成
H   = img.shape[0]
W   = img.shape[1]
img_gray = np.zeros((H,W), dtype=np.float32) #型はnp.float32



#!!ここを編集!!
for y in range(H) :
    for x in range(W) :
        #以下のコードでは，画像のr値をimg_grayに代入している(色はBGR順)
        brue  = img[y,x,0]
        green = img[y,x,1]
        red   = img[y,x,2]
        img_gray[y,x] = red


#save image
cv2.imwrite(fname_out, np.uint8(img_gray) )


#解説 :
#  画像を8bit int(uint8)で持ってしまうと，オーバフローや切捨て誤差が出る可能性が有ります．
#  そのため画像を一度float値にして，計算をしてからint8に戻しています．
#　float型のnumpy arrayは画像としてセーブできないのでセーブ時にuint8に変換しなおす必用が有ります
#  またcv2.imwrite は，カラー（3channel）とグレースケール(1channel)の配列に対して利用可能です．
