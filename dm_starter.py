#
#
import glob
import time
import hashlib


if __name__ == '__main__':

    key = str(time.time())
    hashval = hashlib.sha256(key.encode()).hexdigest()

    for path in glob.glob("./exer*.py"):
        with open(path, encoding="utf-8") as f:
            s = f.read()
        if s[:7] == '#dm2024':
            print("初期化は実行済みです。最初に実行した際の出力を提出してください。")
            print("最初に実行した際のデータをなくした場合は、templateをもう一度ダウンロードしてください。")
            exit()

        s1 = "#dm2024 " + str(hashval)
        s = s1 + s

        with open(path, 'w',  encoding="utf-8") as f:
            f.write(s)

    print("initialize success" + key)
