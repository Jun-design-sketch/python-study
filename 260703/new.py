import pandas as pd
import numpy as np

# Scalar value: 全部同じ値入れるのも簡単
s = pd.Series(5.0, index=["a","b","c","d","e"])
print(s)

# Sequence value
s = pd.Series([5.0, 4.0, 3.0], index=["c", "o", "u"])
print(s)

# dictionary-like`
print(s["c"])

# exception
# print(s["f"])

# no exception!
print(s.get("f"))