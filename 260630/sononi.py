import pandas as pd
import numpy as np

# Seriesはindexがある
s = pd.Series(data=["1","2","9","2222"])
print(s.iloc[3])
# TypeError: 'median' withn string dtype
# print(s.median())
print(s.dtype)

# TypeError: 'set' type is unordered
# s = pd.Series(data={"1","2","9","2222"})

# ndarray == N-dimensinal array(numpy)
# 値の羅列になる
print(s.to_numpy())

