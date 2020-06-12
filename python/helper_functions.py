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
