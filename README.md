# カテゴリ別におけるVTuberとYouTuberの配信スタイルによる印象評価 アンケート結果検定
論文「カテゴリ別におけるVTuberとYouTuberの配信スタイルによる印象評価」のアンケート結果検定用プログラムです。

## 環境構築
anaconda/miniconda で、 root ディレクトリで次のコマンドを実行してください
```bash
$ conda env create -f conda_env.yml
```

## 構成
```
root
├─ questionnaire  # アンケート結果の CSV
├─ src            # ソースコード
├─ .gitignore     # Gitでバージョン管理しないファイル一覧
├─ conda_env.yml  # 環境設定ファイル
├─ README.md      # 説明書（このファイル）
└─ tasks.py       # invoke のタスクを記述するファイル
```

## 使い方
root ディレクトリで次のコマンドを実行してください
```
$ inv run
```
