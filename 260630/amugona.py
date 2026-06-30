from pathlib import Path
import pandas as pd
import numpy as np

# passing a list of values, letting pandas create a default RangeIndex
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print("s, index:", s.index)
print("表現：", s.describe())
print(type(s))
# Seriesは型に縛られずなんでも１次元で入れられるのだ。

with_str = pd.Series(["a","555", 1, 8, 5255, -99, np.nan])
print("文字列も要約")
print(with_str.describe(include="all"))

# Series:a one-dimensinal labeled array holding data of any type
# DataFrame:a tow-dimensional data structure that holds data like a two-dimension array or a table with rows and coulmns.
BASE_PATH = Path(__file__).resolve().parent
DATA = pd.read_csv(BASE_PATH / "input/注文.csv")
print(DATA.head)
print("DATAの型はもちろん　", type(DATA))
print("DATAがDataFrameだから列は　", type(DATA["注文日"]))

# Seriesはindexを持つし、indexの指定もできるし、indexの重複もできる
print(pd.Series(np.random.randn(5), index=["x","y","z","a","a"]))

# dictionary with Series
s2 = pd.Series({"a":0.0, "b":3, "c":6})
print("s2", s2)
print(type(s2))
# 新たなindexにするには、値配列だけ抽出して再度Seriesする
print(s2.to_numpy())
s3 = pd.Series(s2.to_numpy(), index=["newA","newB","newC"])
print("s3", s3)
#Seriesは、index_labelにマッチし移動できる
s4 = pd.Series(s2, index=["c","d","b","a"])
print("s4", s4)

li = ["a", "b"]
di = {"a":1, "b":2}
se = {"a", "b"}
tu = ("a", "b")


