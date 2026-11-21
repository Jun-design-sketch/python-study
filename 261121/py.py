orders = [
    {"id": "A-101", "quantity": 3},
    {"id": "A-102", "quantity": 0},
    {"id": "A-103", "quantity": 2},
]
orders2 = [
    {"id": "A-101", "quantity": 3},
    {"id": "A-102", "quantity": 9},
    {"id": "A-103", "quantity": 2},
]
def has_invalid_order(orders):
  for order in orders:
    if order['quantity'] == 0: return True
    try: int(order['quantity'])
    except ValueError: return True
  return False

print(has_invalid_order(orders))
print(has_invalid_order(orders2))