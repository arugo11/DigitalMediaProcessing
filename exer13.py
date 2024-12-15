#
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
f.write("a"+str(5)) #このように書き込む (これは例なので削除してください)
f.write("b"+str(10)) #このように書き込む (これは例なので削除してください)
