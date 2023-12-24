'''
Name: Shubham Mohole
Function: So basically I wrote out a bunch of powers of two so 2^0, 2^1, and 2^2 and I realized that each power
can be simplifed to basically 2 * 2^n-1 to find 2^n and that is recursive step. 2^0 is our base step and that is just 1.
'''

def exp(n):
    if n == 0:
        return 1
    else:
        return 2 * exp(n-1)

# TestDrive
print(exp(0))
print(exp(3))
print(exp(100))