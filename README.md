# 例の機械を作成

## 見た目の完成図
![structure_image](doc/structure.jpg)

## 概要
- 数秒に一度、複数のセンサーから値を取得する(MAC側)
- センサーの位置は変数(配列)で保存可能, 値は角度で保存(MAC側)
- センサーの位置を向く(回転する)機能がある(Raspberry pi側)
  - 機能としては、信号を受け取ったら〇〇度回転するというものだけ
- 台を何度回転させたかを保存しておき、向きたいセンサを指定しただけで自動計算されるようにする(Mac側)
