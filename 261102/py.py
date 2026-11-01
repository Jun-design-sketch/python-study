names = ["keyboard", "mouse", "monitor"]
prices = [12000, 4500, 28000]

def make_list(names, prices):
  ans = {}
  for name, price in zip(names, prices):
    # ans[name] = f"{price}Yen"
    # ans[name] = str(price) + "Yen"
    ans[name] = "{}Yen".format(price)
  return ans

print(make_list(names, prices))