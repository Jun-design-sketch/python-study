payments = [
    {"name": "田中", "amount": 1200},
    {"name": "佐藤", "amount": 800},
    {"name": "田中", "amount": 2300},
    {"name": "佐藤", "amount": 700},
    {"name": "鈴木", "amount": 1500},
]

totals = {}

for payment in payments:
  name = payment.get("name")
  if name in totals:
    totals[name] += payment.get("amount")
  else:
    totals[name] = payment.get("amount")

print(totals)

prices = {
    "keyboard": 12000,
    "mouse": 4500,
    "monitor": 28000,
}

sorted_prices = sorted(
  prices.items(),
  key=lambda item:item[1],
  reverse=True
)
print(sorted_prices)