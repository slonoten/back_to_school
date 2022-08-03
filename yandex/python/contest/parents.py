def width(n):
    if n == 0:
        yield ""
    else:
        for i in range(n):
            for left in width(n - 1 - i):
                for right in width(i):
                    yield f"({left}){right}"

n = int(input())

ans = [*width(n)]

for s in sorted(ans):
    print(s)

