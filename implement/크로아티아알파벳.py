# 2941 S5

replace_dict = [
    "c=",
    "c-",
    "dz=",
    "d-",
    "lj",
    "nj",
    "s=",
    "z="
]
word = input()
for r in replace_dict:
    print(r)
    word = word.replace(r, " ")
print(len(word))