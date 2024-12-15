#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# モザイク画像の作成
# 第2引数はモザイクのサイズ
# この課題は, nparrayの[スライス表現]を使うと非常に簡単にかける（使わなくともよい）

import numpy as np
import sys
import cv2

#ファイル名と窓サイズRをコマンドライン引数より取得
fname_in  = sys.argv[1]
R         = int(sys.argv[2])
fname_out = sys.argv[3]

#画像をロードしfloat型へ変換
img = cv2.imread(fname_in)
img = np.float64(img)



#モザイク画像の作成

#!!以下 for文を編集!!

#ヒント : 以下のfor文の中身を編集すれば実現できるはず
#（必用ならfor文の範囲を編集してもＯＫ）
#このfor分自体を削除してもOK
for y in range( int( img.shape[0] / R + 1) ) :
    for x in range( int( img.shape[1] / R + 1) ) :

        #ヒント：スライス表現により画像の矩形領域を取り出せる
        # 以下はヒントなので提出時には削除してください

        # 以下のようにすると[y*R, (y+1)*R) x [x*R, (x+1)*R) の矩形領域のrチャンネルを取り出せる
        rectR = img[y*R:(y+1)*R, x*R:(x+1)*R, 2]

        print(rectR)

        #代入もできる (x=1, y=3のブロックのみに代入している)
        if( x == 1 and y == 3) :
            img[y*R:(y+1)*R, x*R:(x+1)*R, 2] = 100

        # ヒントここまで－－－－－－ 提出時には削除する



#最後に画像を出力して終了
cv2.imwrite(fname_out, np.uint8( img) )
