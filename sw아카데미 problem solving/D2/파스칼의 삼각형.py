T = int(input())
for tc in range(1, T + 1):
    cycle = int(input())  # 반복 횟수 입력
    numbers = []  # 출력 용 저장 리스트
    temp = []  # 계산용 임시 리스트

    for i in range(cycle):  # 반복문
        numbers.append(1)  # 첫부분 1 입력
        temp.append(1)  # 계산용도 동일하게 적용
        if i < 2:
            pass  # 2가 넘어갈 될 때까지 무시
        else:
            for j in range(1, len(numbers) - 1):  # 계산
                temp[j] = numbers[j - 1] + numbers[j]
        for j in range(len(numbers)):  # 계산 완료된 코드를 다시 저장
            numbers[j] = temp[j]
            print(str(numbers[j]) + " ", end="")  # 한줄로 출력

        print("")  # 줄 띄우기
