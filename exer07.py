#
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
