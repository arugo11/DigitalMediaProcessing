#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# 画像に縦方向sobel filterをかける
#  - 負値となる画素は-1倍，
#  - 255を超える画素には，オーバーフローを避けるため255を代入
import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )


#!!以下を編集する!!
kernel = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])

for y in range( 1, img.shape[0]-1 ) :
    for x in range( 1, img.shape[1]-1 ) :
        val = 0
        for j in range(kernel.shape[0]):
            for i in range(kernel.shape[1]):
                val += img[y + j - 1, x + i - 1] * kernel[j, i]
        
        if val < 0:
            val *= -1
        if val > 255:
            val = 255

        img_out[y, x] = val



#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
