# this is NOT an actual bruteforce tool, it just finds the given target
import itertools

def alphabetical_bruteforce(target=False, print_attempts=True, length=1, charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if target == False:
        target = input("Enter target word: ")
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
    if print_attempts:
        result = withPrintAttempts()
    else:
        result = silent()
    return result
