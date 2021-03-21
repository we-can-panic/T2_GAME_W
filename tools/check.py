import random

import T2_GAME_W as T2

def deck_volume(res: list):
  if len(res) > T2.assets.env.deck.max:
    print("!デッキ規定枚数を上回っています")
    print("!デッキを間引きます")
    res = random.sample(res, T2.assets.env.deck.max)

  if len(res) < T2.assets.env.deck.max:
    print("!デッキ規定枚数を下回っています")
    print("!デッキを水増しします")
    while len(res) < T2.assets.env.deck.max:
      res.append(random.sample(res, 1)[0])

  return res
