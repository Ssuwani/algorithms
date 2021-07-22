# 2581 S5

a = int(input())
b = int(input())
results = []
for i in range(a, b+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 2:
        results.append(i)

if results:
    print(sum(results))
    print(min(results))

else:
    print(-1)
