#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# 5x5メディアンフィルタ
import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )



#!!以下を編集!!(

#ヒント : img_outはゼロ初期化されているので周囲2画素分にはアクセスしない
#ヒント: numpyには中央値を出力する関数があるのでそれを利用するとよいかも
def median_filter(img, window_size = 5):

    result = np.zeros_like(img)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            window =img[y:y+window_size, x:x+window_size]
            result[y, x] = np.median(window)
    return result
#float型からuint8型に変換し、書き出し

img_out = median_filter(img)
cv2.imwrite(fname_out, img_out )

#? 先生の出力画像は周りに黒枠があるけどあれなんなんだろ
