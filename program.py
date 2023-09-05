def main():

    print(factorial(5))
    print(factorial(6))
    print(factorial(7))
    print(factorial(8))
    
    sum = 0
    for i in range(101):
        sum += i
    print(sum)

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
if __name__ == "__main__":
    main()