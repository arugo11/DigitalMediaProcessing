#
#dm template
# これより上は編集しないこと

# 画像の離散フーリエ変換
#
# 画像のフーリエ変換結果は，Fuv = Ruv + i * Iuv と複素数画像となる
# 計算結果の Ruv と Iuv をそれぞれ画像として書き出す


import numpy as np
import sys
import cv2
import math

fname_in      = sys.argv[1]
fname_out_Rvu = sys.argv[2]
fname_out_Ivu = sys.argv[3]


#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)


#出力画像を準備(グレースケール，float型)
Rvu = np.zeros_like( img )
Ivu = np.zeros_like( img )

H = img.shape[0]
W = img.shape[1]



#!!以下のfor文の中身を編集する!!
for v in range( H ) :
    for u in range( W ) :
        Rvu[v,u] = 0
        Ivu[v,u] = 0
        #ヒント: 素朴に実装するならこの下にさらに2重ループを書く事になります
        #ヒント: pythonでfor文をまわすと速度が出ないです。小さい画像でテストしてください。




# 直流成分を0にする（他の画素に比べてここだけ非常に大きな値を持ち、正規化がうまくいかないため場当たり的な方法）
Rvu[0,0] = 0 #ここは編集しない！


#!!!ここも編集する!!!
# (値 – 最小値)/(最大値-最小値) * 255 という変換を施すことで，値の範囲を[0,255]にする
#（RvuとIvuをそれぞれ個別に正規化すること




#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out_Rvu, np.uint8( Rvu) )
cv2.imwrite(fname_out_Ivu, np.uint8( Ivu) )
