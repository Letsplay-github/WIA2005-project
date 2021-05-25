from bs4 import BeautifulSoup
import requests
import obo

def extractWord(link):

    url = requests.get(link).text

    soup = BeautifulSoup(url, 'lxml')

    article = soup.find('div', class_='articleDetails')

    headline = article.find('div', class_='headline').h1.text

    fullArticle = headline.split()

    story = article.find('div', class_='story')

    for p in story.find_all('p'):

        fullArticle += p.text.split()

    wordlist = []

    for w in range(len(fullArticle)):
        wordlist += obo.stripNonAlphaNum(fullArticle[w])

    space = ['']

    def removeSpace(list):
        return [w.lower() for w in list if w not in space]

    wordlist = removeSpace(wordlist)

    return wordlist