import numpy as np
from cv2 import imread
import sys
from collections import deque

# 配列と迷路の状況の対応付け
WALL = np.array([0, 0, 0])
AISLE = np.array([255, 255, 255])
START = np.array([0, 0, 255])
GOAL = np.array([255, 0, 0])

def main() -> None:
    maze = np.uint8(imread(sys.argv[1]))
    # print(maze)

    # スタートとゴールの位置を取得
    start_pos = (int(np.where(np.all(maze == START, axis=-1))[0][0]),int(np.where(np.all(maze == START, axis=-1))[1][0]))
    goal_pos = (int(np.where(np.all(maze == GOAL, axis=-1))[0][0]),int(np.where(np.all(maze == GOAL, axis=-1))[1][0]))
    print(start_pos,goal_pos)
    # 最短距離を保存したリスト
    H, W, _ = maze.shape#type:ignore
    distance = [[-1] * W for _ in range(H)]

    dh = [-1, 1, 0, 0]
    dw = [0, 0, 1, -1]

    Q = deque()

    # スタート位置を設定してキューに追加
    start_h, start_w = start_pos[0], start_pos[1]
    distance[start_h][start_w] = 0
    Q.append((start_h, start_w))

    while Q:
        h, w = Q.popleft()
        # print(h,w)
        for i in range(4):
            next_h = h + dh[i]
            next_w = w + dw[i]
            if (0 <= next_h < H and
                0 <= next_w < W and
                np.array_equal(maze[next_h, next_w], AISLE)):
                if distance[next_h][next_w] == -1:  # 未探索
                    distance[next_h][next_w] = distance[h][w] + 1
                    Q.append((next_h, next_w))
                    print(Q)


    goal_h, goal_w = goal_pos[0], goal_pos[1]
    print(distance[goal_h][goal_w])

if __name__ == "__main__":
    main()