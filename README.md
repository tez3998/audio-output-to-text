# audio_output_to_text
スピーカーやヘッドフォンから出力される話し声のオフライン文字起こしです。
文字起こしされた結果はターミナルに表示されます。
音声認識にはVOSKを用いています。

# デモ動画
VOICEVOXから出力された音を文字起こししました。

＊480p以上でないと、文字起こしされた結果が見えにくいかもしれません。

[![](https://img.youtube.com/vi/8TGZBzI9u7E/0.jpg)](https://www.youtube.com/watch?v=8TGZBzI9u7E)

# 動作環境
Windows10とUbuntu18.04上での動作を確認しています。
macOSは手元に環境がないため、動作を確認できていません。

# 使用しているライブラリ
- copy
- json
- typing
- multiprocessing
- numpy
- soundcard
- sounddevice
- vosk

# 使用方法
```bash
python run.py
```

# その他
[Qiita](https://qiita.com/3998/items/a18b50aaf58e0176e6a5)の方で紹介しました。
