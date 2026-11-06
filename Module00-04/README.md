## Python00 — Growing Code

> 42 Python Module 00「Python Fundamentals Through Garden Data」の学習記録

| 項目 | 内容 |
|---|---|
| テーマ | 基本構文・変数・関数・条件分岐・ループ・再帰・型ヒント |
| 期間 | 2026/11/02 〜 2026/11/06 |
| 使用ツール | Python 3.x / flake8 / mypy / venv（WSL Ubuntu + VS Code） |

---

## 📁 構成

```
Module00/
├── ex0/ft_hello_garden.py
├── ex1/ft_garden_name.py
├── ex2/ft_plot_area.py
├── ex3/ft_harvest_total.py
├── ex4/ft_plant_age.py
├── ex5/ft_water_reminder.py
├── ex6/ft_count_harvest_iterative.py
│   ft_count_harvest_recursive.py
└── ex7/ft_seed_inventory.py
```

---

## 📝 各課題のまとめ

| Ex | 関数 | 内容 | 学んだこと |
|---|---|---|---|
| 0 | `ft_hello_garden` | 固定メッセージを表示 | 関数定義の書き方、文字列はクォートで囲む |
| 1 | `ft_garden_name` | 名前を入力して表示 | `input()` のプロンプト、`print()` を分けて改行 |
| 2 | `ft_plot_area` | 縦×横で面積を計算 | `input()` は文字列を返す → `int()` で変換 |
| 3 | `ft_harvest_total` | 3日分の収穫量の合計 | 使える関数が限られる中での書き方 |
| 4 | `ft_plant_age` | 60日より多いか判定 | `if` / `else`、`>` と `>=` の違い |
| 5 | `ft_water_reminder` | 2日より多いか判定 | **more than = 「より多い」（以上ではない）** |
| 6 | `ft_count_harvest_*` | 1〜N日を数える（ループ版・再帰版） | `range()` は終わりを含まない、再帰の3要素 |
| 7 | `ft_seed_inventory` | 単位ごとに表示を分ける | 引数で値を受け取る、`if/elif/else`、`capitalize()` |

---

## 💡 学んだこと

### 1. `input()` は必ず文字列を返す

```python
length = input("Enter length: ")       # "5"（文字列）
length = int(input("Enter length: "))  # 5（数値）
```

### 2. `print()` のカンマ区切りは自動でスペースが入る

`str()` を使わずに、数値と文字列を並べて表示できる。

```python
print("Plot area:", 15)        # → Plot area: 15
print("Plot area: ", 15)       # → Plot area:  15（スペース2つになる！）
print("a", "b", sep="-")       # → a-b（区切り文字は sep で変更できる）
```

### 3. 比較の英語表現

| 英語 | 意味 | 演算子 |
|---|---|---|
| more than 2 | 2 より多い | `>` |
| 2 or more / at least 2 | 2 以上 | `>=` |
| less than 2 | 2 未満 | `<` |

### 4. `range()` は終わりの値を含まない

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 5)       # 1, 2, 3, 4
range(1, n + 1)   # 1 〜 n
```

- Python の `for` は「`range` が作った値を順番に取り出す」だけ。C のように自分で `i++` する必要はない（そもそも `++` は存在しない）。

### 5. 再帰の3要素

```python
def count_day(day: int, last: int) -> None:
    if day > last:              # ① 終了条件
        return
    print("Day", day)           # ② やること
    count_day(day + 1, last)    # ③ 次の呼び出し（値を変えて自分を呼ぶ）
```

- `input()` は1回だけにしたいので、「入力する関数」と「再帰する補助関数」に分ける。
- 引数の中に `day += 1` は書けない（`+=` は文なので）。`day + 1` と書く。
- ループ版は `range` が終わりを含まないので `+ 1` が必要。再帰版は `day > last` で止めるので終わりを含む → `+ 1` は不要。

### 6. 型ヒント

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name: str = input("Enter garden name: ")
```

- 変数は `変数名: 型 = 値`（C のような `str name` という書き方はない）
- 何も返さない関数は `-> None`

### 7. 文字列メソッド

```python
"tomato".capitalize()          # → "Tomato"（残りは小文字になる）
"cherry tomato".title()        # → "Cherry Tomato"（単語ごとに先頭を大文字）
```

---

## 🧹 flake8 でつまずいたところ

| コード | 内容 | 対策 |
|---|---|---|
| E111 | インデントが4の倍数でない | スペース4個にそろえる |
| W191 / TabError | タブを使っている、タブとスペースが混ざっている | VS Code で「Indent Using Spaces」に設定 |
| E225 | 演算子の前後にスペースがない | `name = input(...)`、`-> None` |
| E231 | カンマのあとにスペースがない | `print("Day", day)` |
| E203 | コロンの前にスペースがある | `days_limit: int` |
| E501 | 1行が79文字を超えている | カッコの中で改行する |
| W292 / W391 | ファイル末尾の改行がない／空行が多い | 最後は改行1つだけ |

---

## 🛠 開発環境

```bash
# 仮想環境
python3 -m venv .venv-basics
source .venv-basics/bin/activate
pip install flake8 mypy

# チェック
flake8 .
mypy .
```

- 仮想環境の正体はただのディレクトリ。`activate` は `PATH` の先頭に `bin/` を足しているだけ。
- `.mypy_cache/`、`__pycache__/`、`.venv*/` は `.gitignore` で除外する。

---

##  つまずいたこと・気づき

-Cとの違いが割とはっきりしているなと改めて感じた
-型ヒントが結構便利
