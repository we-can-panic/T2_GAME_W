from T2_GAME_W.assets.assets import piece



def names():
  return {
    A: "Accel",
    B: "Bird",
    C: "Cyclone",
    D: "Dummy",
    E: "Eternal",
    F: "Fang",
    G: "Gene",
    H: "Heat",
    I: "Iceage",
    J: "Joker",
    K: "Key",
    L: "Luna",
    M: "Metal",
    N: "Nasca",
    O: "Ocean",
    P: "Puppeteer",
    Q: "Queen",
    R: "Rocket",
    S: "Skull",
    T: "Trigger",
    U: "Unicorn",
    V: "Violence",
    W: "Weather",
    X: "Xtreme",
    Y: "Yesterday",
    Z: "Zone"
  }

class A(piece):
  """
  直近の相手の駒に向かい1マス移動する。(通り道の相手の駒は破壊される。)
  素早さ：9
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Accel"
    self.speed = 9

  def move(self):
    p = findMostRecent(self)
    position=self.position
    for i in range(2):
      if p.position[i]>self.position[i]: position[i]+=1
      elif p.position[i]<self.position[i]: position[i]-=1
    while True:
      try:
        super().move(position)
        break
      except RuntimeError as position:
        if board[position[0]][position[1]].player!=self.player:
          super().destroy(board[position[0]][position[1]])
        else:
          break


class B(piece):
  """
  縦横に2マス、進行方向斜めに1マス進んだ場所移動する。通り道の駒は飛び越えて移動する。
  素早さ：5
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Bird"
    self.speed = 5

  def move(self):
    p = findMostRecent(self)
    # 進む方向を決める
    if abs(p.position[0]-self.position[0])<abs(p.position[1]-self.position[1]):
      if p.position[1]>self.position[1]:
        vec = 1 if p.position[1]<self.position[1] else 2
      else:
        vec = 5 if p.position[1]<self.position[1] else 6
    else:
      if p.position[0]>self.position[0]:
        vec = 7 if p.position[1]<self.position[1] else 8
      else:
        vec = 4 if p.position[1]<self.position[1] else 3
    # 移動
    while True:
      try:
        position = self.position
        if vec in (1,2): position[1]+=3
        elif vec in (5,6): position[1]-=3
        elif vec in (3,4): position[0]+=3
        elif vec in (7,8): position[0]-=3
        if vec in (3,8): position[1]+=1
        elif vec in (4,7): position[1]-=1
        elif vec in (2,5): position[0]+=1
        elif vec in (1,6): position[0]-=1
        super().move(position)
        break
      except RecursionError as position:
        if board[position[0]][position[1]].player==self.player:
          vec = vec%8+1
        else:
          super().destroy(board[position[0]][position[1]])
      except IndexError:
        vec = vec%8+1

class C(piece):
  """
  直近の自分の駒の素早さを5上げる。
  素早さ：9
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Cyclone"
    self.speed = 9

class D(piece):
  """
  最遠の自分の駒に変身する。
  素早さ：6
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Dummy"
    self.speed = 6


class E(piece):
  """
  直近の相手の駒を破壊し、自身も破壊される。
  素早さ：6
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Eternal"
    self.speed = 6


class F(piece):
  """
  自身を破壊する。この駒が破壊されたとき、破壊した駒を破壊する。
  素早さ：0
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Fang"
    self.speed = 0


class G(piece):
  """
  直近の自分の駒と同じ行動をする。
  素早さ：8
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Gene"
    self.speed = 8


class H(piece):
  """
  周囲8マスの駒を破壊する。
  素早さ：5
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Heat"
    self.speed = 5


class I(piece):
  """
  直近の未行動の相手の駒を、行動済みにする。
  素早さ：3
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Iceage"
    self.speed = 3


class J(piece):
  """
  直近の相手の駒に向かい2マス移動する。(通り道の相手の駒は破壊される。)
  素早さ：5
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Joker"
    self.speed = 5


class K(piece):
  """
  直近の自分の駒と場所を入れ替える。
  素早さ：8
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Key"
    self.speed = 8


class L(piece):
  """
  直近の自分の駒が破壊されたとき、破壊された駒に変身する。
  素早さ：0
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Luna"
    self.speed = 0


class M(piece):
  """
  直近の相手の駒に向かい2マス移動する。(通り道の相手の駒は破壊される。)このマスと周囲の9マスに相手の駒が存在しない場合、この駒は破壊されない。
  素早さ：4
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Metal"
    self.speed = 4


class N(piece):
  """
  縦横の自分の駒を破壊する。破壊した駒の数だけランダムな相手の駒を破壊する。
  素早さ：2
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Naska"
    self.speed = 2


class O(piece):
  """
  周囲32マスに存在する相手の駒の素早さを下げる。
  素早さ：8
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Ocean"
    self.speed = 8


class P(piece):
  """
  直近の相手の駒を自分のものにし、次に行動させる。
  素早さ：1
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Puppeteer"
    self.speed = 1


class Q(piece):
  """
  縦横斜め8方向の直線方向に移動する。通り道に相手の駒がある場合、駒を破壊し、そこで止まる。
  素早さ：3
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Queen"
    self.speed = 3


class R(piece):
  """
  縦横斜め8方向の直線方向に移動する。通り道のすべての駒は破壊される。
  素早さ：4
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Rocket"
    self.speed = 4


class S(piece):
  """
  縦横の相手の駒に向かい3マス移動する。(通り道の相手の駒は破壊される。)
  素早さ：5
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Skull"
    self.speed = 5


class T(piece):
  """
  直近の自分の駒の周囲8マスの相手の駒を破壊する。
  素早さ：6
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Trigger"
    self.speed = 6


class U(piece):
  """
  直近の相手の駒に向かい2マス移動する。(通り道の相手の駒は破壊される。)この駒が相手の駒を破壊した場合、その駒に変身する。
  素早さ：5
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Unicorn"
    self.speed = 5


class V(piece):
  """
  直近の相手の駒に向かい3マス移動する。(通り道の相手の駒は破壊される。)
  素早さ：3
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Violence"
    self.speed = 3


class W(piece):
  """
  直近の相手の駒と最遠の自分の駒を破壊する。
  素早さ：4
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Weather"
    self.speed = 4


class X(piece):
  """
  二回行動でき、直近の駒の動きをする。
  素早さ：3
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Xtreme"
    self.speed = 3


class Y(piece):
  """
  直前に移動していた自分の駒と同じ行動をする。
  素早さ：4
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Yesterday"
    self.speed = 4


class Z(piece):
  """
  直近の相手の駒と最遠の自分の駒の位置を入れ替える。
  素早さ：2
  """
  def __init__(self, player_side):
    super().__init__(player_side)
    self.name = "Zone"
    self.speed = 2
