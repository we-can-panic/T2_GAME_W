from T2_GAME_W.tools.gaming import *

def main():
  # デッキ選択
  for i in range(2):
    path = input("デッキのPathを入力してください：")
    if len(path)==0:
      path = None
    import_deck(i, path)

  # デッキ配置
  pass


if __name__ == '__main__':
  main()
