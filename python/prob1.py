"""
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples_to_n(n_max:int, multiples:list) -> int:
    """
    Sums the multiples in the list up to n_max, doesn't include n_max
    """
    def divisible(val, multiples):
        for divisor in multiples:
            if val % divisor == 0:
                return val
        return 0
    n=1
    sum_n=0
    while n < n_max: 
        sum_n += divisible(n, multiples)
        n += 1
    return sum_n


if __name__ == "__main__":
    print("Ans is %s" %( sum_multiples_to_n(1000, [3,5]) ) )
