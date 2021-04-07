''' You can find this exercise at the following website: https://www.practicepython.org/

6. String Lists:

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.) '''

# Input
word = input("Enter a word: ")
wordInList = [element for element in word.lower()]
print()

# Processing and Output
print("  Original list: " + str(wordInList))
print("List in reverse: " + str(wordInList[::-1]))
print()

if wordInList == wordInList[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome!")