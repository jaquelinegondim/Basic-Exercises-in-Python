''' You can find this exercise at the following website: https://www.practicepython.org/

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

* Use binary search. '''

# First 10 values of Fibonacci Sequence
def Fibonacci():
    series = [1, 1]
    for i in range(2, 10):
        previous1 = series[i - 1]
        previous2 = series[i - 2]
        new = previous1 + previous2
        series.append(new)
    return(series) 
    
def Searching(values, guess):
    print(values, guess) # To make testing easier
    for i in values:
        if guess == i:
            return True
            break
    return False

def BinarySearch(values, guess):
    left = 0
    right = len(values) - 1
    while(left <= right):
        mid = (left + right) // 2
        if(values[mid] == guess):
            return True
        elif(guess < values[mid]):
            right = mid - 1
        elif(guess > values[mid]):
            left = mid + 1
    return False

if __name__=="__main__":
    num = int(input("Enter a number: ")) # Receiving an input
    firstTen = Fibonacci()
    print(Searching(firstTen, num))
    print(BinarySearch(firstTen, num))

    ''' Testing different values
    l = [2, 4, 6, 8, 10]
    print(Searching(l, -1))
    print(BinarySearch(l, -1))
    print(Searching(l, 0))
    print(BinarySearch(l, 0)) 
    print(Searching(l, 2))
    print(BinarySearch(l, 2)) 
    print(Searching(l, 3))
    print(BinarySearch(l, 3))
    print(Searching(l, 4))
    print(BinarySearch(l, 4)) 
    print(Searching(l, 5))
    print(BinarySearch(l, 5)) 
    print(Searching(l, 6))
    print(BinarySearch(l, 6)) 
    print(Searching(l, 7))
    print(BinarySearch(l, 7)) 
    print(Searching(l, 8))
    print(BinarySearch(l, 8)) 
    print(Searching(l, 9))
    print(BinarySearch(l, 9)) 
    print(Searching(l, 10))
    print(BinarySearch(l, 10))
    print(Searching(l, 11))
    print(BinarySearch(l, 11)) 
    print(Searching(l, 6.4))
    print(BinarySearch(l, 6.4))  '''   