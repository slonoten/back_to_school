s1 = input()
s2 = input()

s1 = bytes(s1, "ascii")
s2 = bytes(s2, "ascii")

def count(s):
    counter = [0] * 256
    for b in s:
        counter[b] += 1
    return counter

print(int(len(s1) == len(s2) and count(s1) == count(s2)))