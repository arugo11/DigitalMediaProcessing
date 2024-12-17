#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

#雛形特になし、自由に書いてみてください
"""
Q-tableを用いた簡単な強化学習
"""
import numpy as np
import cv2
import sys

# 行動の定義
UP   :int = 0
RIGHT:int = 1
DOWN :int = 2
LEFT :int = 3

# 配列と迷路の状況の対応付け
WALL :np.ndarray = np.array([0, 0, 0])
AISLE:np.ndarray = np.array([255, 255, 255])
START:np.ndarray = np.array([255, 0 , 0])
GOAL :np.ndarray = np.array([0, 0, 255])

class Env:
    def __init__(self):
        self._maze = np.uint8( cv2.imread(sys.argv[1]) )
        self.reset()

    # 盤面の初期化
    def reset(self):


        # スタートポジション
        #NOTE: なんかこの書き方よくないらしい
        self._state = list(map(int,np.where(np.all(self._maze == START, axis=-1))))
        return np.array(self._state)
    
    # 行動
    def step(self, action: int) -> tuple[np.ndarray, int]:
        reward: int = 0

        if action == UP: #up
            self._state[0] -= 1
        elif action == RIGHT:
            self._state[1] += 1
        elif action == DOWN:
            self._state[0] -= 1
        elif action == LEFT:
            self._state[1] -= 1
        else:
            exit("予期しないアクション")

        tile_statue: np.ndarray = self._maze[self._state[0], self._state[1]] #type:ignore

        if np.all(tile_statue == WALL):
            reward -= 1
        elif np.all(tile_statue == AISLE):
            reward += 0
        elif np.all(tile_statue == GOAL):
            reward += 1
        return np.array(self._state,), reward
    
    # Q値の設定
    class Q_tabel:
        def __init__(self):
            _maze = np.uint8( cv2.imread(sys.argv[1]) )
            H, W = _maze.shape[:2] #type:ignore
            self._Qtable = np.zeros((H, W, 4)) # 4はアクションの種類

        # 行動の選択
        def get_action(self, state:list[int] , epsilon: float) -> int:
            if epsilon > np.random.uniform(0,1):
                next_action:int = np.random.choice([UP,LEFT])
            else:
                next_action:int  = np.random.choice(
                    np.where(
                    self._Qtable[:,state[0],state[1]]
                    ==self._Qtable[:,state[0],state[1]].max()
                )[0]
                ) 
            return next_action

        # Q値の更新
        def update_Qtable(self, 
                          state:list[int],      # 現在の状況
                          action: int,          # 行動(0 .. 3)
                          reward: int,          # 報酬(-1 .. 1)
                          next_state:list[int]  # 次の状況
                          
                          ) -> np.ndarray:
    
            return self._Qtable



def main() -> None:
    env = Env()
    print(env._state)

if __name__ == "__main__":
    _maze = np.uint8( cv2.imread(sys.argv[1]) )
    H, W = _maze.shape[:2] #type:ignore
    print(H,W)