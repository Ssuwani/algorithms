# 1978 S4
n = int(input())
seq = list(map(int, input().split()))


def find(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0

for s in seq:
    if find(s):
        count += 1
print(count)
