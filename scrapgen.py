# brute force generator, generates every combination from used charset
# charset is a string object, containing any characters we wish
# minlength is a minimum length of generated words, we can wish to 
# generate only 3 lettered combination, as i did - BBB then minlength
# and maxlength are equal.
# maxlength is maximum length of generated words

from itertools import chain, product
def bruteforce(charset, maxlength, minlength=0):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))

# parameter in square brackets can be used to take only specific range
# print(list(bruteforce('abcdefghijklmnopqrstuvwxyz', 3))[0:100])
# print(len(list(bruteforce('abcdefghijklmnopqrstuvwxyz', 3, 2))))