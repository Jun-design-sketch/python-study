def mask_customer_ids(customer_ids):
    masked_ids = []
    for customer_id in customer_ids:
        if(len(customer_id) <= 4):
            str = "*" * (len(customer_id))
        else:
            str = "*" * (len(customer_id)-4) + customer_id[-4:]
        masked_ids.append(str)
    return masked_ids

print(mask_customer_ids([
    "1234567890",
    "ABCD1234",
    "987654",
]))
# ['******7890', '****1234', '**7654']

print(mask_customer_ids([
    "1234",
    "AB",
    "1",
]))
# ['****', '**', '*']

print(mask_customer_ids([]))
# []