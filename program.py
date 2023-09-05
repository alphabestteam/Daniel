def main():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)


def isPrimaryNum(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(isPrimaryNum(5))
print(isPrimaryNum(6))
print(isPrimaryNum(7))
print(isPrimaryNum(14))
print(isPrimaryNum(152))
print(isPrimaryNum(60693))



def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))

if __name__ == "__main__":
    main()
