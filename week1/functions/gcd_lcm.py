# 12. Write a python module with two functions:
# a. GCD
# b. LCM

def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)

def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)


if __name__ == '__main__':
    a = 10
    b = 2
    print (f'GCD of {a} and {b} is {gcd(a, b)}')
    print (f'LCM of {a} and {b} is {lcm(a, b)}')