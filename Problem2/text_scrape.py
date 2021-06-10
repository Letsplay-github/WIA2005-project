from bs4 import BeautifulSoup
import requests
import obo

def extractWord(link):

    url = requests.get(link).text

    soup = BeautifulSoup(url, 'lxml')
    
    fullArticle = []

    story = soup.select_one("#story-body, .td-post-content, .paragraph, .post-content, #post-6775, .entry-content")

    for p in story.find_all('p'):

        fullArticle += p.text.split()

    wordlist = []

    for w in range(len(fullArticle)):
        wordlist += obo.stripNonAlphaNum(fullArticle[w])

    space = ['']

    def removeSpace(list):
        return [w for w in list if w not in space]

    wordlist = removeSpace(wordlist)

    return wordlist