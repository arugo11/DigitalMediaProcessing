#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
d  = int(sys.argv[2])
sc = float(sys.argv[3])
ss = float(sys.argv[4])
fname_out = sys.argv[5]

#以下を編集 (2~3行で書けると思います)
img = cv2.imread(fname_in)
img_out = cv2.bilateralFilter(img, d, sc, ss)
cv2.imwrite(fname_out, img_out )

