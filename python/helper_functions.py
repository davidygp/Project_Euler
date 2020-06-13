# Puts the helper functions which are used for multiple problems

def find_prime_nos(prime_nos, n) -> list:
    """
    Given an initial list of prime numbers, find the other prime numbers up to n
    """
    start = prime_nos[-1] + 1
    for i in range(start, n+1):
        #print(i)
        possible = True
        for prime in prime_nos:
            if i % prime == 0:
                possible = False
                break
        #print(possible)
        if possible:
            prime_nos.append(i)
    return prime_nos

def find_prime_nos2(n:int) -> list:
    """
    Find all prime numbers up to n.
    Use the Sieve of Eratosthenes method.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    import math
    if n <= 1:
        return [0]
    A = [0, 0] + (n-1)*[1] 
    sqrt_n = math.sqrt(n)
    for i in range(2, math.floor(sqrt_n)+1):
        if A[i]:
            #print("i is %s" %(i))
            for j in range(2*i, n+1, i):
                #print("j is %s" %(j))
                if i != j:
                    A[j] = 0
    prime_nos = []
    for i in range(len(A)):
        if A[i] == 1:
            prime_nos.append(i)
    return prime_nos

def find_prime_factors_of_n(n: int) -> list:
    """
    Find the prime factors of n
    """
    prime_no_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \
                     31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, \
                     79, 83, 89, 97]
    remainder = n
    prime_factors = []
    while True:
        remainder_old = remainder
        if remainder in prime_no_list:
            prime_factors.append(remainder)
            break
        for prime in prime_no_list:
            if remainder%prime == 0:
                remainder = int(remainder/prime)
                prime_factors.append(prime)
                break
        if remainder_old == remainder:
            # i.e. we couldn't find a prime factor, need to enlarge out list
            prime_no_list = find_prime_nos(prime_no_list, prime_no_list[-1]*2)
            #print("Enlarged list to %s" %(prime_no_list))
    return prime_factors
