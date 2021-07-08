# 2839 B1
weight = int(input())
result = 0

while weight >= 0:
    if weight % 5 == 0:
        result += weight // 5
        weight -= 5 * (weight // 5)
        print(result)
        break
    result += 1
    weight -= 3
    if weight < 0:
        print(-1)
