''' You can find this exercise at the following website: https://www.practicepython.org/

Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.
 '''

with open("names-list.txt") as open_file:
    test = {} # create the dictionary
    line = open_file.read() # put the text into a string variable
    for name in line.split('\n'): # split the string according to the line break
        if name in test: # test if the string is in the dictionary
            test[name] += 1 # if it is, add 1
        else:
            test[name] = 1 # if it is not, create the key and add value = 1

print(test)

with open("images-list.txt") as open_file:
    test2 = {}
    line = open_file.read()
    for name in line.split('\n'):
        line = name[3:-25] # remove unnecessary characters
        if line in test2:
            test2[line] += 1
        else:
            test2[line] = 1

for key, value in test2.items(): # use for loop to improve readability
	print(key, ':', value)