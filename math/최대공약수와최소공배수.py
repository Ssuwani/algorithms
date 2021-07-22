# 2609 S5
import math


n, m = map(int, input().split())
gcd_num = math.gcd(n, m)
lcd_num = n * m // gcd_num
print(gcd_num)
print(lcd_num)

