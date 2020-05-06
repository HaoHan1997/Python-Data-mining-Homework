from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = False
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = True
        break
if is_prime and num != 1:
    print('%d是质数' % num)
else:
    print('%d不是质数' % num)