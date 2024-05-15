
## 実行

1. /data/ にissue.xlsxを作成する (issues.sample.xlsxを複製してリネーム)
2. /src/config.pyを作成する (config.sample.pyを複製してリネーム)
3. `$ python src/main.py` を実行する

---

## 開発環境

### 仮想環境の作成

```
$ python -m venv {name}
```

### 仮想環境の立ち上げ

```
$ . {name}/bin/activate
```

### 仮想環境の終了

```
$ deactivate
```

### ライブラリの保存

```
$ pip freeze > requirements.txt
```

### ライブラリの復元

```
$ pip install -r requirements.txt
```