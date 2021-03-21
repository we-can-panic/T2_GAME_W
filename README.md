# T2_GAME

### 【コンセプト】
・自動で動くチェスをイメージ

・複数の駒を盤面に交互に配置していく．すべての駒が配置されたら，駒が自動で動き勝敗を決する．

・駒の動きは事前に決まっているので，（難易度は高いが）完全情報ゲームとなりうる．


### 【ゲームの流れ】
・プレイヤーは16個の駒(2個まで重複可)を持つ

・先攻（ランダム）のプレイヤーから順に，8×8の盤面に駒をセットしていく

・各プレイヤーが全ての駒を置き終わったら戦闘開始

・素早さの高い順に駒が行動してゆき、最終的に生き残った駒側のプレイヤーの勝ちとなる

・素早さが同順の場合は、早く置いた駒が先に動く


### 【駒のリスト】


|名前|素早さ|能力|
|---|---|---|
|ACCEL|9|直近の相手に向かい1マス移動する。(通り道の相手の駒は破壊される。)|
|BIRD|5|直近の相手方向に向かい縦横に2マス、進行方向斜めに1マス移動する。通り道の駒は飛び越えて移動する。|
|CYCLONE|9|直近の自分の駒の素早さを5上げる。|
|DUMMY|6|最遠の自分の駒に変身する。|
|ETERNAL|6|直近の相手の駒を破壊し、自身も破壊される。|
|FANG|0|自身を破壊する。この駒が破壊されたとき、破壊した駒を破壊する。|
|GENE|6|直近の自分の駒と同じ行動をする。|
|HEAT|5|周囲8マスの駒を破壊する。|
|ICEAGE|3|直近の未行動の相手の駒を、行動済みにする。|
|JOKER|5|直近の相手の駒に向かい2マス移動する。(通り道の相手の駒は破壊される。)|
|KEY|8|直近の自分の駒と場所を入れ替える。|
|LUNA|0|直近の自分の駒が破壊されたとき、破壊された駒に変身する。|
|METAL|4|直近の相手の駒に向かい2マス移動する。(通り道の相手の駒は破壊される。)nこのマスと周囲の9マスに相手の駒が存在しない場合、この駒は破壊されない。|
|NASCA|2|縦横の自分の駒を破壊する。破壊した駒の数だけランダムな相手の駒を破壊する。|
|OCEAN|8|周囲32マスに存在する相手の駒の素早さを下げる。|
|PUPPETEER|1|直近の相手の駒を自分のものにし、次に行動させる。|
|QUEEN|3|縦横斜め8方向の直線方向に移動する。n通り道に相手の駒がある場合、駒を破壊し、そこで止まる。|
|ROCKET|4|縦横斜め8方向の直線方向に移動する。通り道のすべての駒は破壊される。|
|SKULL|5|縦横の相手の駒に向かい3マス移動する。(通り道の相手の駒は破壊される。)|
|TRIGGER|6|直近の自分の駒の周囲8マスの相手の駒を破壊する。|
|UNICORN|5|直近の相手の駒に向かい2マス移動する。(通り道の相手の駒は破壊される。)nこの駒が相手の駒を破壊した場合、その駒 に変身する。|
|VIOLENCE|3|直近の相手の駒に向かい3マス移動する。(通り道の相手の駒は破壊される。)|
|WEATHER|4|直近の相手の駒と最遠の自分の駒を破壊する。|
|XTREME|3|二回行動でき、直近の駒の動きをする。|
|YESTERDAY|4|直前に移動していた自分の駒と同じ行動をする。|
|ZONE|2|直近の相手の駒と最遠の自分の駒の位置を入れ替える。|

### 【細かい仕様】
・移動先に自分の駒がいる場合、その1マス前で止まる。

・すべての駒が2回行動した後は、すべての駒が直近の相手の駒に向かい1マス移動してから行動するようになる。
