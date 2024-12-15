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

height   = img.shape[0]
width    = img.shape[1]
img_gray = np.zeros((height, width), dtype=np.float32)



#!!ここを編集!!
#ヒント : 前課題のグレースケール化をそのまま使いつつ，
#        画素値がthreshold以上なら255を代入し，そうでなければ0を代入するとよい




#save image
cv2.imwrite(fname_out, np.uint8(img_gray) )
