# 1316 S5
def group_number(word):
    appear = []
    prev = ''
    for w in word:
        if w == prev:
            continue
        if w in appear:
            return False
        appear.append(w)
        prev = w
    return True


n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    cnt += group_number(word)

print(cnt)