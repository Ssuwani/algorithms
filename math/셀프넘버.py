# 4673 S5

seq = list(range(1, 10000))
for num in range(1, 10000):
    make_num = 0
    for index, i in enumerate(str(num)):
        if index == 0:
            make_num += int(num)
        make_num += int(i)

    try:
        seq.remove(make_num)
    except:
        pass

[print(s) for s in seq]
