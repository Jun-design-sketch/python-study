import json

# s = "ABCDEFGH"
# print(s[:3])   # ABC
# print(s[3:])   # DEFGH
# print(s[:-3])  # ABCDE
# print(s[-3:])  # FGH

def parse_logs(logs):
    result = []
    for log in logs:
        s = log.strip()
        if s[8:12] not in ("INFO", "WARN", "ERRO"):
            continue
        if len(s) > 12:
            element = {
                "date": s[0:8],
                "level": s[8:12],
                "message": s[12:]
            }
            result.append(element)
    return json.dumps(result, indent=4)

print(parse_logs([
    "20261128INFOApplication started",
    "20261128ERROConnection failed",
]))
# [
#     {
#         "date": "20261128",
#         "level": "INFO",
#         "message": "Application started"
#     },
#     {
#         "date": "20261128",
#         "level": "ERRO",
#         "message": "Connection failed"
#     }
# ]

print(parse_logs([
    "",
    "invalid",
    "20261128INFO",
    "20261128TESTHello",
    "  20261128WARNMemory usage high  ",
]))
# [
#     {
#         "date": "20261128",
#         "level": "WARN",
#         "message": "Memory usage high"
#     }
# ]

print(parse_logs([]))
# []