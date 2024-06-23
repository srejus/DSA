'''
Find the sum of digits

num = 123
output = 1+2+3 = 6
'''

def sum_of_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_of_digits(num//10)


num = 123
print(sum_of_digits(num))