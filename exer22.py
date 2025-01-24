#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
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

H = img.shape[0] #type:ignore
W = img.shape[1] #type:ignore



#!!以下のfor文の中身を編集する!!
for v in range( H ) :
    for u in range( W ) :
        Rvu[v,u] = 0
        Ivu[v,u] = 0
        #ヒント: 素朴に実装するならこの下にさらに2重ループを書く事になります
        #ヒント: pythonでfor文をまわすと速度が出ないです。小さい画像でテストしてください。

        # メモ化 (真鍋先生はこれで高速化してた気がする,ベクトル化はわすれた)
        cos_cache = np.array([[math.cos(2 * math.pi * (u*x/W + v*y/H))
                             for x in range(W)] for y in range(H)])
        sin_cache = np.array([[math.sin(2 * math.pi * (u*x/W + v*y/H))
                             for x in range(W)] for y in range(H)])
        
        sum_real = np.sum(img * cos_cache)
        sum_imag = -np.sum(img * sin_cache)
        
        Rvu[v,u] = sum_real / (W*H)
        Ivu[v,u] = sum_imag / (W*H)


# 直流成分を0にする（他の画素に比べてここだけ非常に大きな値を持ち、正規化がうまくいかないため場当たり的な方法）
Rvu[0,0] = 0 #ここは編集しない！


#!!!ここも編集する!!!
# (値 – 最小値)/(最大値-最小値) * 255 という変換を施すことで，値の範囲を[0,255]にする
#（RvuとIvuをそれぞれ個別に正規化すること

Rvu_min = np.min(Rvu)
Rvu_max = np.max(Rvu)
Ivu_min = np.min(Ivu)
Ivu_max = np.max(Ivu)

Rvu = ((Rvu - Rvu_min) / (Rvu_max - Rvu_min) * 255)
Ivu = ((Ivu - Ivu_min) / (Ivu_max - Ivu_min) * 255)


#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out_Rvu, np.uint8( Rvu) ) #type:ignore
cv2.imwrite(fname_out_Ivu, np.uint8( Ivu) ) #type:ignore
