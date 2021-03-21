from T2_GAME_W.assets.assets import piece

def core_piece():
  p1 = piece(0)
  p1.move()
  print(p1.calc_next_position())

def import_deck():
  from T2_GAME_W.tools import gaming
  res = gaming.import_deck(1)
  for r in res:
    print(r.name)


if __name__ == '__main__':
  #core_piece()
  import_deck()
