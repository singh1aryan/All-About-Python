# binary table
# truth table 

def printBinary(digits, prefix):
    if digits == 0:
        print(prefix)

    else:
        printBinary(digits-1, prefix + "0")
        printBinary(digits-1, prefix+"1")

printBinary(3, "")
printBinary(4, "")
