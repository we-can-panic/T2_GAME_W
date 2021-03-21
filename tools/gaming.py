"""
ゲームの進行を助ける関数群（start.pyが使う）
"""

import T2_GAME_W as T2

from T2_GAME_W.tools import check
from T2_GAME_W.pieces import pieces1



def import_deck(player_side, path=None):
  """
  引数のcsvを読み込んで、
  pieceのリストを返す
  """
  if path is None:
    from T2_GAME_W.test.sampledeck import _import
    datas = _import()
  else:
    datas = open(path).readlines()

  res = []
  for r in datas:
    r = r.strip().split(",")
    if len(r)==1:
      res.append(make_instance(player_side, r[0]))
    else:
      for i in range(int(r[1])):
        res.append(make_instance(player_side, r[0]))

  # デッキの枚数を調整
  res = check.deck_volume(res)

  return res



def make_instance(player_side: int, name: str):
  piece_dic = {v: k for k, v in pieces1.names().items()}

  return piece_dic[name](player_side)
