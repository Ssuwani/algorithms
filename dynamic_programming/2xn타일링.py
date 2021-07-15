# 11726 S3

seq = [0]*1001
seq[1] = 1
seq[2] = 2

n = int(input())
for i in range(3, n+1):
    seq[i] = seq[i-2]+seq[i-1]

print(seq[n] % 10007)
