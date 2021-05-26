''' You can find this exercise at the following website: https://www.practicepython.org/

Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved. '''

from bs4 import BeautifulSoup
import requests
url = "https://divyanshushekhar.com/python-beautifulsoup-find-findall/"
url_html = requests.get(url) # getting the syntax for how to load the webpage
url_text = url_html.text # getting the text from the webpage

soup = BeautifulSoup(url_text, 'html.parser') # parsing the page

text = ""

for findClass in soup.find_all('h2', class_="uagb-heading-text"): # finding h2 elements with this specific class
    text += findClass.get_text() + "\n" # setting a string variable to store the text

fileName = str(input("Name the text file: ")) + ".txt" # asking the user to name the file

with open(fileName, 'w') as openFile: # creating a .txt file with the text saved into fileName
    openFile.write(str(text)) # 'w' means write only mode

# openFile represents the name of the file object