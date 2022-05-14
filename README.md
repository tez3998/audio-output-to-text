# audio_output_to_text
スピーカーやヘッドフォンから出力される話し声のオフライン文字起こしです。
文字起こしされた結果はターミナルに表示されます。
音声認識にはVoskを用いています。

# デモ
[![](https://img.youtube.com/vi/8TGZBzI9u7E/0.jpg)](https://www.youtube.com/watch?v=8TGZBzI9u7E)

# 動作環境
Windows10とUbuntu16.04上での動作を確認しています。

# 使用しているライブラリ
- copy
- json
- typing
- multiprocessing
- numpy
- soundcard
- sounddevice
- vosk

# Linux上で動かす場合
Pythonのsoundcardライブラリを使うためにはlibsndfileが必要です。
aptのようなパッケージマネージャーを使用してインストールしてください。

# 使用方法
```bash
python run.py
```
