def merge_dicts(d1, d2):
    return {**d1, **d2}          # yoki d1 | d2 (Python 3.9+)

def count_keys(d):
    return len(d)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = merge_dicts(d1, d2)
print(merged)           # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(count_keys(merged))  # 4
