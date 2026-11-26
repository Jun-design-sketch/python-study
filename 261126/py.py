import re

def normalize_emails(mails):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    s = set()
    for mail in mails:
        mail = mail.strip().lower()
        if re.fullmatch(pattern, mail):
            s.add(mail)
    return list(s)

print(normalize_emails([
    " Alice@Example.com ",
    "BOB@example.com",
    "alice@example.com",
    "  Charlie@example.com  ",
]))
# ['alice@example.com', 'bob@example.com', 'charlie@example.com']

print(normalize_emails([
    "invalid",
    "@example.com",
    "alice@",
    "a@@example.com",
    "bob@example.com",
]))
# ['bob@example.com']

print(normalize_emails([
    "",
    "   ",
    " DEV@company.com ",
]))
# ['dev@company.com']

print(normalize_emails([]))
# []