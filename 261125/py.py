def summarize_hours(records):
    answer = {}
    for department, work_hours in records:
        try:
            hours = int(work_hours)
            if hours >= 0:
                answer[department] = answer.get(department, 0) + hours
        except (ValueError, TypeError):
            continue
    return answer

records1 = [
    ("dev", "8"),
    ("sales", "7"),
    ("dev", "6"),
    ("sales", "abc"),
    ("dev", None),
    ("hr", "-3"),
]
print(summarize_hours(records1)) # {'dev': 14, 'sales': 7}

print(summarize_hours([
    ("dev", "0"),
    ("hr", "5"),
    ("hr", "3"),
])) # {'dev': 0, 'hr': 8}

print(summarize_hours([
    ("dev", "error"),
    ("hr", None),
    ("sales", "-1"),
]))
# {}

print(summarize_hours([]))
# {}