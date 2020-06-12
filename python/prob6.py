"""
Problem 6:

The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# from https://www.themathpage.com/Arith/asquares.htm
# Formular for sum of 1^2 + 2^2 + ... n^2 = (2n + 1)*(n)*(n+1)/6

def sum_squares_to_n(n: int) -> int:
    """
    The sum of the squared values from 1 to n.
    i.e. 1^2 + 2^2 + 3^2 + ... (n-1)^2 + n^2
    """
    return int((2*n+1)*n*(n+1)/6)

difference = (sum(range(1,100+1)))**2 - sum_squares_to_n(100)


if __name__ == "__main__":
    print("Ans is %s" % ( difference ) )
    # 24164150
