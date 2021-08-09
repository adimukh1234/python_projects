# this program will print a pattern for you according to the number of rows you enter

def pattern(n):
    mist = []
    for i in range(1, n + 1):
        mist.append("*" * i)
    print("\n".join(mist))


pattern(int(input("Enter number of rows:")))
