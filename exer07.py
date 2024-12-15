#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import cv2

#load image
fname_in  = sys.argv[1]
fname_out = sys.argv[2]

img    = cv2.imread(fname_in)

#!!ここを編集


#save image
cv2.imwrite(fname_out, img )
