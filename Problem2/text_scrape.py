from bs4 import BeautifulSoup
import requests
import obo

def extractWord(link):

    url = requests.get(link).text

    soup = BeautifulSoup(url, 'lxml')
    
    fullArticle = []

# Select one HTML element based on CSS selector (#item -> CSS id selector, .item -> CSS class selector)
    story = soup.select_one("#story-body, .td-post-content, .paragraph, .post-content, #post-6775, .entry-content")

# Extract and create word list from <p> element
    for p in story.find_all('p'):

        fullArticle += p.text.split()

    wordlist = []

# Remove Non-Alphanumerical characters from items in word list
    for w in range(len(fullArticle)):
        wordlist += obo.stripNonAlphaNum(fullArticle[w])

# Remove remaining whitespace from items in word list
    space = ['']

    def removeSpace(list):
        return [w for w in list if w not in space]

    wordlist = removeSpace(wordlist)

    return wordlist