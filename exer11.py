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
for y in range( 1, img.shape[0]-1 ) :
    for x in range( 1, img.shape[1]-1 ) :
        img_out[y,x] = 0
        #ヒント: gaussian filterとほとんど同じ
        #ヒント: 負値のときの処理と255を超えたときの処理を忘れずに！
        #ヒント: 負値でかつ絶対値が255を超える画素にも対応できるように (←例年間違い多いです)



#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
