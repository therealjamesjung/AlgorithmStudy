import sys
input = sys.stdin.readline

N = int(input().strip())
Alist = list(map(int, input().strip().split()))
answer = [0 for _ in range(N)]

for i in range(N) :
    tmp = []
    for j in range(i) :
        if Alist[i] < Alist[j] :
            tmp.append(answer[j])

    if tmp and max(tmp) > answer[i]:
        answer[i] = max(tmp)
    answer[i]+=1

print(max(answer))

