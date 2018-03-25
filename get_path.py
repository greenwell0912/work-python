import pathlib

# python3.5以前は os.pathモジュールがおすすめ

# ファイル名のPathオブジェクトを作成
root = pathlib.Path(__file__)
print(root)
# 絶対パス取得
abs_root = root.resolve()
print(abs_root)
# スクリプトファイルのディレクトリ取得
parent = abs_root.parent
print(parent)

# パスを作成　例
# このように実行環境に依存しないようにパスを作成する
csv_path = parent / '..' / 'data'
file_path = csv_path / 'hoge.csv'
print(csv_path)
print(file_path)
