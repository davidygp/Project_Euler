"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import copy
from helper_functions import find_prime_nos, find_prime_factors_of_n

# Find the prime numbers from 1 to 20
prime_nos_2_to_20 = find_prime_nos([2], 20)

# Find all the numbers from 1 to 20
num_2_to_20 = list(range(2,21))

# method 1: break down all numbers from 1 to 20 into the prime factors (non-repeated)
# Find if the prime factors of the numbers from 1 to 20 can be constructed directly
# from the prime numbers from 1 to 20, else append to the list
# Final list, everything from 1 to 20 should be broken down into primes (sometimes multiple)
# This is so we won't have to muliply multiple times, e.g. 4=2*2, 8=2*2*2
prime_nos_2_to_20_added = prime_nos_2_to_20
for num in num_2_to_20[::-1]:
    checked_in_prime_nos_list = []
    prime_factors = find_prime_factors_of_n(num)
    tmp_prime_nos_2_to_20_added = copy.deepcopy(prime_nos_2_to_20_added)
    for prime in prime_factors:
        if prime in tmp_prime_nos_2_to_20_added:
            tmp_prime_nos_2_to_20_added.remove(prime)
        else:
            prime_nos_2_to_20_added.append(prime)
        
# Find the product of all in the final lsit
prod = 1
for num in prime_nos_2_to_20_added:
    prod *= num

# method 2: less efficient as it checks all
def check_divisible_by_list(check_no, num_list):
    for i in range(len(num_list)-1):
        #print(check_no, num_list[i])
        if check_no%num_list[i] != 0:
            return False
    #print(check_no, num_list[-1])
    if check_no%num_list[-1] == 0:
        return True
    return False

def smallest_no_divisible_by_list(num_list):
    check_no = num_list[-1] # Start checking from the last number 
    while True:
        if check_divisible_by_list(check_no, num_list):
            return check_no
        check_no += 1

#smallest_no_divisible_by_list(num_2_to_20)

if __name__ == "__main__":
    print("Ans is %s" % ( prod ) )
    # 232792560
