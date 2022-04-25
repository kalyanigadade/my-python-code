def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()
def pattern2(n):
    for i in range(n):
        for j in range(n):
            print('$',end=' ')
        print()
def pattern3(n):
    for i in range(n):
        for j in range(n):
            print('#',end=' ')
        print()
def pattern4(n):
    for i in range(n):
        for j in range(n):
            print('7',end=' ')
        print()
def pattern5(n):
    for i in range(n):
        for j in range(n):
            print('PYTHON',end=' ')
        print()

def pattern6(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
def pattern7(n):
    for i in range(n):
        for j in range(i+1):
            print('#',end=' ')
        print()
def pattern8(n):
    for i in range(n):
        for j in range(i+1):
            print('$',end=' ')
        print()
def pattern9(n):
    for i in range(n):
        for j in range(i,n):
            print('*',end=' ')
        print()

def pattern10(n):
    for i in range(n):
        for j in range(i,n):
            print('#',end=' ')
        print()
def pattern11(n):
    for i in range(n):
        for j in range(i,n):
            print('$',end=' ')
        print()
def pattern12(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i+1):
            print('*',end=' ')
        print()
def pattern13(n):
    for i in range(n):
        for j in range(i, n):
            print(' ', end=' ')
        for j in range(i + 1):
            print('3', end=' ')
        print()
def pattern14(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i+1):
            print('$',end=' ')
        print()
def pattern15(n):
    for i in range(n):
        for j in range(i+n):
            print(' ',end=' ')
        for j in range(i,n):
            print('*',end=' ')
        print()
def pattern16(n):
    for i in range(n):
        for j in range(i+n):
            print(' ',end=' ')
        for j in range(i,n):
            print('$',end=' ')
        print()
def pattern17(n):
    for i in range(n):
        for j in range(i+n):
            print(' ',end=' ')
        for j in range(i,n):
            print('#',end=' ')
        print()
def pattern18(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i):
            print('*',end=' ')
        for j in range(i+1):
            print('*',end=' ')
        print()
def pattern19(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i):
            print('$',end=' ')
        for j in range(i+1):
            print('$',end=' ')
        print()
def pattern20(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(i,n-1):
            print('$',end=' ')
        for j in range(i,n):
            print('$',end=' ')
        print()
def pattern21(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(i,n-1):
            print('*',end=' ')
        for j in range(i,n):
            print('*',end=' ')
        print()
def pattern22(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(i,n-1):
            print('#',end=' ')
        for j in range(i,n):
            print('#',end=' ')
        print()
n=int(input("Enter number of rows::"))
pattern15(n)


