def sum_valid_numbers(values):
    s = 0
    for value in values:
        try: s += int(value)
        except (ValueError, TypeError): continue
    return s


print(sum_valid_numbers(["10", "20", "abc", "30"])) # 60
print(sum_valid_numbers(["-5", "hello", "15", "3.5"])) # 10
print(sum_valid_numbers(["a", "b", "c"])) # 0
print(sum_valid_numbers([])) # 0