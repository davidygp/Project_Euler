"""
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helper_functions import find_prime_nos2

def main():
    return sum(find_prime_nos2(2000000))

if __name__ == "__main__":
    ans = main()
    print("Ans is %s" % ( ans ) )
    # 142913828922 
