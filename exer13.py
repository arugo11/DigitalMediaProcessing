#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

import numpy as np
import sys
import math

fname_in = sys.argv[1]
fname_out = sys.argv[2]

#read text and counte alphabet
f = open(fname_in, "r")
trgt_string = ""
for line in f.readlines():
    if len(line) > 0 :
        trgt_string += line
f.close()



f = open(fname_out, "w")

# !! TODOここを編集 !!
cnt:int  = 1
ans: str = ""
for i in range(len(trgt_string) - 1):
    if trgt_string[i] != trgt_string[i + 1]:
        ans += trgt_string[i] + str(cnt)
        cnt = 0
    cnt += 1
ans += trgt_string[-1] + str(cnt)
with open(fname_out, 'w') as f:
    f.write(ans)