import sys

n = int(sys.stdin.readline())

alpha = []
alpha_dict = {}
numList = []

for i in range(n):
    alpha.append(sys.stdin.readline().rstrip())

# 모든 단어에 대해서
for i in range(n):
    # 단어의 길이만큼 실행
    for j in range(len(alpha[i])):
        # 단어의 알파벳이 이미 dict에 있으면
        if alpha[i][j] in alpha_dict:
            # 자리에 맞게 추가 ( 1의 자리면 1 )
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)

        # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

# dict에 저장된 수들을 모두 리스트에 추가
for val in alpha_dict.values():
    numList.append(val)

# 수들을 내림차순 정렬
numList.sort(reverse=True)

sum = 0
pows = 9
# 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
for i in numList:
    sum += pows * i
    pows -= 1
print(sum)