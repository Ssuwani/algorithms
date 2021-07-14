# 1463 S3

n = int(input())
seq = [0] * 1000001

for i in range(2, n+1):
    seq[i] = seq[i-1] + 1
    if i % 3 == 0:
        seq[i] = min(seq[i], seq[i//3] + 1)
    if i % 2 == 0:  # elif 로 하면 위의 if가 실행되면 실행되지 않기 때문에 if로 해야한다..!!
        seq[i] = min(seq[i], seq[i//2] + 1)


print(seq[n])
