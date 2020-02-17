'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

def equalK(alist, k):
    for i in alist:
        for n in alist:
            if i+n == k:
                return True


    return False

assert(equalK([10, 15, 3, 7], 17) == True)
assert(equalK([1], 1) == False )
assert(equalK([], 0) == False)


