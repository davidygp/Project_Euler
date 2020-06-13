"""
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    all_a_b_c = list(range(1,500))
    product = 1
    for i in range(len(all_a_b_c)):
        for j in range(len(all_a_b_c)):
            for k in range(len(all_a_b_c)):
                a = all_a_b_c[i]
                b = all_a_b_c[j]
                c = all_a_b_c[k]
                if a < b  and b < c:
                    if a**2 + b**2 == c**2:
                        print("Found Pythagorean triplet in %s %s %s" %(a, b, c) )
                        print("%s + %s = %s" %(a**2, b**2, c**2) )
                        if a + b + c == 1000:
                            product = a*b*c
                            print("Found ans: %s" %(product) )
                            return product
    

if __name__ == "__main__":
    ans = main()
    print("Ans is %s" % ( ans ) )
    # 31875000 
