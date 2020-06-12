"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def find_max_palin_product() -> int:
    """
    Find the largest palindrome made from the product of two 3-digit numbers
    """
    max_palin_product = 0
    for _, val1 in enumerate(range(100, 1000), 1):
        for _, val2 in enumerate(range(100, 1000), 1):
            if val1 > val2:
                product = str(val1 * val2)
                reverse_product = "".join(list(product)[::-1])
                if product == reverse_product and int(product) > max_palin_product:
                    max_palin_product = int(product)
    return max_palin_product




if __name__ == "__main__":
    print("Ans is %s" % ( find_max_palin_product() ) )
    # 9066909
