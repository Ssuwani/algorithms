# 1003 S3

# 시간 초과가 뜰지라도 코드를 작성하고 점화식을 찾는것도 좋은 방법인듯하다!!
cnt_0 = [0]*41
cnt_1 = [0]*41
cnt_0[0] = 1
cnt_1[0] = 0
cnt_0[1] = 0
cnt_1[1] = 1
for i in range(2, 41):
    cnt_0[i] = cnt_0[i-2] + cnt_0[i-1]
    cnt_1[i] = cnt_1[i-2] + cnt_1[i-1]

for _ in range(int(input())):
    k = int(input())
    print(cnt_0[k], cnt_1[k])
