
def raise_to_Power(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result


print(raise_to_Power(2,3))
