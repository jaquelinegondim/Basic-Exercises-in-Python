''' You can find this exercise at the following website: https://www.practicepython.org/

17. Decode a Web Page

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage. '''

from bs4 import BeautifulSoup
import requests
url = "https://divyanshushekhar.com/python-beautifulsoup-find-findall/"
url_html = requests.get(url) # getting the syntax for how to load the webpage
url_text = url_html.text # getting the text from the webpage

soup = BeautifulSoup(url_text, 'html.parser') # parsing the page


for findClass in soup.find_all('h2', class_="uagb-heading-text"): # finding h2 elements with this specific class
    print(findClass.get_text()) # printing the text it found

# When I tried to webscrape the NYTimes website, I could get all the elements from a tag, but I couldn't get any output when specifying a class.

# One hypothesis is that, since it is a news website, its content is dynamically generated using JavaScript. Therefore, its data cannot be retrieved with this tool. I would have to get the data straight from the API, or use a tool that is JavaScript capable such as Selenium. 

# See: https://stackoverflow.com/questions/58069514/soup-findclass-not-working-and-return-nonetype-in-this-case-how-to-scra?rq=1