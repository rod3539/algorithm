def bin_search(l, r, x, count):
    m = int((l+r)/2)
    if m == x:
        return count
    if x > m:
        return bin_search(m, r, x, count + 1)
    else:
        return bin_search(l, m, x, count + 1)


T = int(input())
for tc in range(1, T + 1):
    p, pa, pb = map(int, input().split())
    ra = bin_search(1, p, pa, 0)
    rb = bin_search(1, p, pb, 0)
    if ra > rb:
        print(f'#{tc} B')
    elif ra < rb:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

