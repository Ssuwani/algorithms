# 1929 S2
import math
a, b = map(int, input().split())
def find(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


for num in range(a, b+1):
    if find(num):
        print(num)