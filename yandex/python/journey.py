n_towns = int(input())

towns = []

for _ in range(n_towns):
    towns.append(tuple(map(int, input().split())))

max_dist = int(input())

i_start, i_finish = map(lambda s: int(s) - 1, input().split())

def calc_dist(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

MAX_HOPS = 1001

min_hops_found = MAX_HOPS

def find(start, finish, skip_towns, n_hops):
    global min_hops_found
    if  calc_dist(start, finish) <= max_dist:
        min_hops_found = min(n_hops + 1, min_hops_found)
        return
    for town in towns:
        if town in skip_towns:
            continue
        dist = calc_dist(start, town)
        if dist > max_dist or dist > (min_hops_found - 1) * max_dist:
            continue
        if n_hops + 1 < min_hops_found:
            find(town, finish, skip_towns + [town], n_hops + 1)

start = towns[i_start]
finish = towns[i_finish]

if start == finish:
    print(0)
else:
    find(start, finish, [start, finish], 0)
    print(min_hops_found if min_hops_found < MAX_HOPS else -1)




