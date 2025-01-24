#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

# *txtファイルから複素数列を読み込み，逆フーリエ変換して出力する
# 入力・出力ともに複素数列であり，以下のフォーマットにて保存されているものとする (sample_Fk.txt参照)
#
# ------fname_out.txt ------
# R0 I0
# R1 I0
# R2 I0
#   :
# Rk Ik
#   :
# --------------------------
#
# pythonには複素数型が用意されているが今回は利用しない

import numpy as np
import sys
import math
# 確認用
import matplotlib.pyplot as plt

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#数列データファイル(txt)を開く
Rk, Ik = [], []
for line in open(fname_in).readlines():
    data = line[:-1].split(' ')
    Rk.append( float(data[0]) )
    Ik.append( float(data[1]) )
print(Rk, Ik)


#fourie transform
#計算結果を入れる配列を0初期化
#（exer16.pyでは空の配列に追加していたが、ここでは長さNの配列を値０で初期化する）
N = len(Rk)
rl, il = [0]*N, [0]*N


#!!ここを編集する!!(現在は０を配列に代入している)
for l in range(N):
    for k in range(N):
        angle = 2 * math.pi * k * l / N
        rl[l] += (Rk[k] * math.cos(angle) + Ik[k] * math.sin(angle)) / N
        il[l] += (-Rk[k] * math.sin(angle) + Ik[k] * math.cos(angle)) / N




# rlとilをテキストに書き出し
file_out = open(fname_out, 'w')
for i in range( N ) :
    file_out.write( str( rl[i] ) + " " + str( il[i] ) + "\n")
file_out.close()

"""
# 以下確認用
plt.figure(figsize=(20, 5)) #これしないと見づらい

plt.subplot(1, 4, 1)
plt.plot(Rk)
plt.title("Sample_Fk(Rk)")
plt.xlabel("k")
plt.ylabel("Rk")

plt.subplot(1, 4, 2)
plt.plot(Ik)
plt.title("Sample_Fk(Ik)")
plt.xlabel("k")
plt.ylabel("Ik")

plt.subplot(1, 4, 3)
plt.plot(Rk)
plt.title("Sample_Fk_Inv(Re)")
plt.xlabel("Index")
plt.ylabel("Value")


plt.subplot(1, 4, 4)
plt.plot(Ik)
plt.title("Sample_Fk_Inv(Im)")
plt.xlabel("Index")
plt.ylabel("Value")

plt.tight_layout()
plt.show()
"""