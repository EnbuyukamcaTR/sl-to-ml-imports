# this is NOT an actual bruteforce tool, it just finds the given target
# `join()` per loop avoided for maximum efficiency
import itertools
import time

def alphabetical_bruteforce(target=False, print_attempts="UNSET", length=1, charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if target == False:
        target = input("Enter target word: ")
    if print_attempts != True or print_attempts != False:
        while True:
            print_attempts = input("Print attempts? (True/False, case sensitive): ")
            if print_attempts == True or print_attempts == False:
                break
    def silent():
        nonlocal length
        while True:
            for current in list(map(''.join, itertools.product(charset, repeat=length))):
                if current == target:
                    print("Found!")
                    return current
            print("Length increased to: {}".format(length))
            length += 1
    def withPrintAttempts():
        nonlocal length
        while True:
            for current in list(map(''.join, itertools.product(charset, repeat=length))):
                print("Trying: {}".format(current))
                if current == target:
                    print("Found!")
                    return current
            length += 1
            print("Length increased to: {}".format(length))
    start = time.time()
    if print_attempts:
        result = withPrintAttempts()
    else:
        result = silent()
    print("Time elapsed: {}".format(time.time() - start))
    return result
