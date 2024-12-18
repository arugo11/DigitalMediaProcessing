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

# ハイパーパラメータ
GAMMA :float = 0.9  # 割引率
ALPHA :float = 0.5  # 学習率

class Env:
    def __init__(self):
        self._maze = np.uint8( cv2.imread(sys.argv[1]) )
        self.reset()

    # 盤面の初期化
    def reset(self) -> list[int]:
    # スタートポジション
        start_pos = np.where(np.all(self._maze == START, axis=-1))
        self._state = [int(start_pos[0][0]), int(start_pos[1][0])] 
        return self._state

    # 行動
    def step(self, action: int) -> tuple[list[int], float]:
        reward: float = 0.0
        next_state = self._state.copy() 

        if action == UP:
            next_state[0] -= 1
        elif action == RIGHT:
            next_state[1] += 1
        elif action == DOWN:
            next_state[0] += 1
        else:
            next_state[1] -= 1

        tile_status: np.ndarray = self._maze[next_state[0], next_state[1]] # type: ignore

        if np.all(tile_status == WALL):
            reward = -1
            return self._state, reward
        elif np.all(tile_status == GOAL):
            reward = 100
            self._state = next_state
        else:  # 通路の場合
            reward = -0.1
            self._state = next_state
        
        return self._state, reward

    
    # Q値の設定
class Q_tabel:
    def __init__(self):
        _maze = np.uint8( cv2.imread(sys.argv[1]) )
        H, W = _maze.shape[:2] #type:ignore
        self._Qtable = np.zeros((4, H, W)) # 4はアクションの種類

    # 行動の選択
    def get_action(self, state:list[int], epsilon: float) -> int:
        if epsilon > np.random.uniform(0,1):
            next_action:int = np.random.choice([UP, RIGHT, DOWN, LEFT])  
            next_action:int = np.random.choice(
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
                        reward: float,        # 報酬(-1 .. 1)
                        next_state:list[int]  # 次の状況
                        ) -> np.ndarray:
        next_maxQ = max(
            self._Qtable[:,next_state[0], next_state[1]]
        )
        self._Qtable[action, state[0], state[1]] = \
            (1 - ALPHA) * self._Qtable[action, state[0], state[1]] \
            + ALPHA * (reward + GAMMA * next_maxQ)

        return self._Qtable



def main() -> None:

    _maze = np.uint8( cv2.imread(sys.argv[1]) )
    H, W = _maze.shape[:2] #type:ignore
    is_reachable : bool = False
    num_episodes :int = 1000
    max_number_of_steps :int = 100

    epsilon = np.linspace(start=0.9, stop=0.1, num=num_episodes)
    
    env = Env()
    table = Q_tabel()
    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0
        
        for t in range(max_number_of_steps):
            action = table.get_action(state=state, epsilon=epsilon[episode])
            next_state, reward = env.step(action)
            total_reward += reward
            
            table.update_Qtable(
                state=state,
                action=action,
                reward=reward,
                next_state=next_state
            )
            
            state = next_state
            
            if np.all(env._maze[state[0], state[1]] == GOAL): # type: ignore
                is_reachable = True
                break
            
        print(f"Episode:{episode:4.0f}, Step:{t:3.0f}, Total Reward:{total_reward:3.0f}")

    if not is_reachable:
        print(-1)
        exit()

    # 最短をQ-tableから求める
    minimum_step:int = 0
    maze:np.uint8 = np.uint8(cv2.imread(sys.argv[1]))
    start_pos = np.where(np.all(maze == START, axis=-1))
    state = [int(start_pos[0][0]), int(start_pos[1][0])]  
    
    for t in range(1000):
        # Q-tableから最もQ値が高い行動を選択する
        actions = np.where(
            table._Qtable[:,state[0], state[1]] == table._Qtable[:,state[0], state[1]].max()
        )[0]
        action = actions[0]

        if action == UP:
            state[0] -= 1
        elif action == RIGHT:
            state[1] += 1
        elif action == DOWN:
            state[0] += 1
        elif action == LEFT:
            state[1] -= 1
        
        minimum_step += 1

        if np.all(maze[state[0],state[1]] == GOAL): # type: ignore
            print("最小歩数は:", minimum_step)
            break

if __name__ == "__main__":
    main()