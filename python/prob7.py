"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from helper_functions import find_prime_nos

some_prime_nos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \
                  31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, \
                  79, 83, 89, 97]

prime_no_cnt = len(some_prime_nos)
while prime_no_cnt <= 10001:
    num = some_prime_nos[-1]*10
    some_prime_nos = find_prime_nos(some_prime_nos, num)
    prime_no_cnt = len(some_prime_nos)
    print("We currently have %s prime numbers" %(prime_no_cnt) )

prime_no_1001 = some_prime_nos[10000]

# Inefficient thou.
if __name__ == "__main__":
    print("Ans is %s" % ( prime_no_1001 ) )
    # 104743
