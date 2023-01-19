T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station_numbers = list(map(int, input().split()))
    count = 0
    point = 0

    while point + K < N:
        for drive_distance in range(K, 0, -1):
            if (point + drive_distance) in station_numbers:
                point += drive_distance
                count += 1
                break
        else:
            count = 0
            break

    print('#{} {}'.format(tc, count))
