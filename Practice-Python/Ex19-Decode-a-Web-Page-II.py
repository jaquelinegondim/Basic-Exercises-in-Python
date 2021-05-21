''' You can find this exercise at the following website: https://www.practicepython.org/

19. Decode a Web Page Two

Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons. '''

from bs4 import BeautifulSoup
import requests
url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
url_html = requests.get(url) # getting the syntax for how to load the webpage
url_text = url_html.text # getting the text from the webpage

soup = BeautifulSoup(url_text, 'html.parser') # parsing the page

findElem = soup.select('div.grid--item.body.body__container.article__body.grid-layout__content > p')

for result in findElem: # finding p elements 
    print(result.get_text()) # printing the text it found