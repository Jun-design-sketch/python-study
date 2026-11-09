orders = {
    "A-101": "3",
    "A-102": "unknown",
    "A-103": "0",
    "A-104": "-2",
    "A-105": None,
}

def checker(orders):
  m = []
  t = 0
  f = {}
  ids = []
  for k, v in orders.items():
    try:
      q = int(v)
    except (ValueError, TypeError) as e:
      m.append(f"{k}: {type(e).__name__}")
      f[k] = type(e).__name__
    else:
      if(q <= 0):
        m.append(f"{k}: validation error")
      else:
        m.append(f"{k}: {q}個")
        t += q
    finally:
      ids.append(f"{k} processed")
  return (m, t, f, ids)

print(checker(orders))
