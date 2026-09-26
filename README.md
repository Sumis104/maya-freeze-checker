# maya-freeze-checker

Mayaシーン内で、Freeze Transformations が適用されていないオブジェクトを検出するツールです。

## できること
- シーン内のオブジェクト(カメラ・ライトを除く)を対象に、Translate・Scale・Rotate が初期値になっているかを確認します
- 適用されていないオブジェクトの名前を、スクリプトエディタに出力します

## 使い方
1. `freezeChecker.py` の中身を、Mayaのスクリプトエディタ(Python)にコピーする
2. 実行する
