n_nums = int(input())

numbers_seen = set()

for _ in range(n_nums):
    n = int(input())
    if n not in numbers_seen:
        print(n)
        numbers_seen.add(n)
