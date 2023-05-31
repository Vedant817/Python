def cal_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + cal_sum(n - 1)


Summation = cal_sum(4)
print(Summation)
