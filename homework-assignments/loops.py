# Fizz Buzz + Primes
# Written by Franz A. Tapia Chaca
# on 15 January 2021
# Hoped to use break / continue, but not wasn't sure how. Suggestion appreciated!

# isPrime function: determine if number is a prime number
    # if prime, i.e. divisible only by itself and one
    # for all numbers 1 to 100
    # calculate modulus with itself and every other number lower
    # if modulus 0, collect
    # if divisible items are 2, prime
def isPrime(n):
    divisibleItems = []
    # say n is 10
    # 10%1 == 0 --> append
    # 10%2 == 0 --> append
    # 10%3 != 0 --> no append
    #...
    # 10%10 == 0 --> append
    for m in range(1, n+1, 1):
        if n % m == 0:
            divisibleItems.append(m)
    if len(divisibleItems) == 2:
        return True
    else:
        return False


for n in range(1,101,1):
    if n % 3 == 0 and n % 5 != 0:  # if multiple of 3 but not of 5
        if isPrime(n):             # and if a Prime
            #print(str(n) + ": Fizz, Prime")
            print("Fizz, Prime")
        else:
            #print(str(n) + ": Fizz")
            print("Fizz")
    elif n % 3 != 0 and n % 5 == 0:  # if multiple of 5 but not of 3
        if isPrime(n):
            #print(str(n) + ": Buzz, Prime")
            print("Buzz, Prime")
        else:
            #print(str(n) + ": Buzz")
            print("Buzz")
    elif n % 3 == 0 and n % 5 == 0:  # if multiple of both 3 and 5, not prime by definition
        #print(str(n) + ": FizzBuzz")
        print("FizzBuzz")
    elif isPrime(n):
        #print(str(n) + ": Prime")
        print("Prime")
    else:
        print(n)
