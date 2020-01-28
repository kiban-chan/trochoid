import numpy as np
import matplotlib.pyplot as plt

# rc : 定円の半径
# rm : 動円の半径
# rd : 描画点の半径
# theta : 回転角


def trochoid(rc, rm, rd):
  # 動円が定円の周りを何周するか
  n = arg_check(rc, rm, rd)

  # XY座標を入れとくヤツ
  point = np.empty((0,2), float)

  # 動円が一回転したときの角度 [rad]
  angle_of_a_loop = 2 * np.pi / n


  for rot in range(int(n)):
    if (rot % 2) == 0: # 外トロコイド
      for theta in np.arange(angle_of_a_loop * rot, angle_of_a_loop * (rot + 1), 0.01):
        x = (rc + rm) * np.cos(theta) - rd * np.cos((rc + rm) * theta / rm)
        y = (rc + rm) * np.sin(theta) - rd * np.sin((rc + rm) * theta / rm)
        point = np.append(point, np.array([[x, y]]), axis=0)
    #elif (rot % 2) != 0: # 内トロコイド
    else:
      for theta in np.arange(angle_of_a_loop * rot, angle_of_a_loop * (rot + 1), 0.01):
        x = (rc - rm) * np.cos(theta) + rd * np.cos((rc - rm) * theta / rm)
        y = (rc - rm) * np.sin(theta) - rd * np.sin((rc - rm) * theta / rm)
        point = np.append(point, np.array([[x, y]]), axis=0)

  return point

def save_and_visualize(data):
  np.savetxt("hoge.csv", data, delimiter=",")
  plt.plot(data[:,[0]], data[:,[1]])
  plt.axis("equal")
  plt.show()

# 引数チェックして，OKなら動円が定円の周りを何周するか返す
def arg_check(rc, rm, rd):
  # 動円が定円の周りを何周するか
  n = rc / rm

  # 全ての半径は零より大きい
  if (rc <= 0) or (rm <= 0) or (rd <= 0):
    print("All of radii must be larger than zero.")
    return

  # 動円は定円より小さい
  if (rc < rm):
    print("rc must be larger than rm.")
    return

  # 描画点は動円の中
  if (rd > rm):
    print("rd must be smaller than rm.")
    return

  # nは整数
  if (n % 1) != 0:
    print("rc must be divisible by rm.")
    return
  
  return n

def main():
  dc = input("基準円直径")
  z = input("歯数")
  rc = int(dc) / 2 # 定円の半径
  rm = rc / (int(z) * 2) # 動円の半径
  zahyo = trochoid(rc, rm, rm)
  save_and_visualize(zahyo)

if __name__ == '__main__':
  main()