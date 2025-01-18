#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import cv2

#get file names and threshold
fname_in  = sys.argv[1]
threshold = int( sys.argv[2] )
fname_out = sys.argv[3]

#load image
img = np.float32( cv2.imread(fname_in) )

height   = img.shape[0] # type: ignore
width    = img.shape[1] # type: ignore
img_gray = np.zeros((height, width), dtype=np.float32)



#!!ここを編集!!
#ヒント : 前課題のグレースケール化をそのまま使いつつ，
#        画素値がthreshold以上なら255を代入し，そうでなければ0を代入するとよい
for y in range(height) :
    for x in range(width) :
        #以下のコードでは，画像のr値をimg_grayに代入している(色はBGR順)
        blue: int  = img[y,x,0] # type: ignore
        green: int = img[y,x,1] # type: ignore
        red: int   = img[y,x,2] # type: ignore
        gray : int = ((red + green + blue) // 3)
        if gray >= threshold: img_gray[y][x] = 255
        else: img_gray[y][x] = 0


#save image
cv2.imwrite(fname_out, np.uint8(img_gray) )#type:ignore
