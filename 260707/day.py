# 2x
Q1 = 3;
A1 = "奇数" if Q1 % 2 == 1 else "偶数"
print(A1)

# Sum
Q2 = 5;
def A2(val):
  if(val > 1): return val + A2(val-1)
  else: return val
print(A2(Q2))

# Maximum
Q3 = [3, 8, 2, 10, 5]
Q3.sort(reverse=True)
print(Q3[0])

# str rev
Q4 = "Python"
print(Q4[::-1])

# cal
Q5 = 7
def A5(val):
  for i in range(1,10): print(f"{val} * {i} = {val*i}")
A5(Q5)