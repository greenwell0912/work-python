import pathlib

data_path = pathlib.Path('data')

# iterate deirectory iterate:反復して
# ディレクトリにあるファイルの一覧取得(1階層まで)
for file_path in data_path.iterdir():
    print(file_path)


# 再帰的に
for file_path in data_path.glob('**/*.csv'):
    print(file_path)
