from T2_GAME_W.assets import env


class board():
  def __init__(self):
    h = env.board.height
    w = env.board.weight
    self.board = [[None for i in range(w)] for j in range(h)]



class piece:
  def __init__(self, player_side: int):
    # プレイヤー（0 or 1）
    self.player_side = player_side

  def calc_next_position(self):
    # 移動規則
    # これは盤上にランダムに出現する動き
    from T2_GAME_W.assets.env import board as b
    from random import randint
    i = randint(0, b.height)
    j = randint(0, b.width)
    return (i, j)

  def move(self):
    # 動くときの効果
    pass

  def touch(self):
    # 移動中、別の駒に触れたら
    pass

  def touched(self):
    # 移動中の別の駒に触れられたら
    pass

  def destroy(self, enemy):
    # 破壊するときの効果
    pass

  def destroyed(self, enemy):
    # 破壊時効果
    pass
