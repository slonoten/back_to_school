jevels = input()
stones = input()

jevel_set = set(jevels)

n_stones = sum(1 for s in stones if s in jevel_set)

print(n_stones)