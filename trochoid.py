import math
import matplotlib.pyplot as plt

# rc : 定円の半径
# rm : 動円の半径
# rd : 描画点の半径
# theta : 回転角


def trochoid(rc, rm, rd):
  # 動円が定円の周りを何周するか
  n = arg_check(rc, rm, rd)

  # XY座標を入れとくヤツ
  point = []

  # 動円が一回転したときの角度 [rad]
  angle_of_a_loop = 2 * math.pi / n


  for rot in range(int(n)):
    angle_s_100 = int(angle_of_a_loop * rot * 100)
    angle_e_100 = int(angle_of_a_loop * (rot + 1) * 100)

    if (rot % 2) == 0: # 外トロコイド
      for theta in [i / 100 for i in range(angle_s_100, angle_e_100, 1)]:
        x = (rc + rm) * math.cos(theta) - rd * math.cos((rc + rm) * theta / rm)
        y = (rc + rm) * math.sin(theta) - rd * math.sin((rc + rm) * theta / rm)
        point.append([x, y])
    else: # 内トロコイド
      for theta in [i / 100 for i in range(angle_s_100, angle_e_100, 1)]:
        x = (rc - rm) * math.cos(theta) + rd * math.cos((rc - rm) * theta / rm)
        y = (rc - rm) * math.sin(theta) - rd * math.sin((rc - rm) * theta / rm)
        point.append([x, y])
  print(len(point))
  return point

def save_and_visualize(data):
  data_x = []
  data_y = []
  for i in range(len(data)):
    data_x.append(data[i][0])
    data_y.append(data[i][1])
  plt.plot(data_x, data_y)
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