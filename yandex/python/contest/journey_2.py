n_towns = int(input())

towns = []

for _ in range(n_towns):
    towns.append(tuple(map(int, input().split())))

max_dist = int(input())

i_start, i_finish = map(lambda s: int(s) - 1, input().split())

def calc_dist(i, j):
    return abs(towns[i][0] - towns[j][0]) + abs(towns[i][1] - towns[j][1])


visited = [(i == i_start)  for i in range(len(towns))]
queue = [(i_start, 1)]
queue_head = 0

while queue_head < len(queue):
    i, hops = queue[queue_head]
    queue_head += 1
    for j, v in enumerate(visited):
        if v:
            continue
        dist = calc_dist(i, j)
        if dist > max_dist:
            continue
        if j == i_finish:
            print(hops)
            exit(1)
        queue.append((j, hops + 1))
        visited[j] = True
print(-1)

