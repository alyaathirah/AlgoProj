import Tries
import requests
from bs4 import BeautifulSoup

class Website():
    title = ""
    textArr = []
    positive = []
    negative = []
    neutral = []
    stop = []

    def __init__(self, url):
        self.url = url
        self.title = ""
        self.textArr = []
        self.positive = []
        self.negative = []
        self.neutral = []
        self.stop = []

    def read(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.title = soup.find("title")
        self.title = self.title.text.strip()

        t = soup.find("article")
        text = t.text.strip()

        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        characters = "!()?@\"#”“’-,\'%.*&\\:"
        for c in characters:
            text = text.replace(c, "")
        text = text.lower()
        text = text.split(' ')

        self.stopword(text) #returned array

    def stopword(self, text):
        file = open("stopword.txt", "r")
        str = file.read()
        str = str.lower()
        stopword = str.split('\n')
        for i in range(len(stopword)):
            try:
                while True: #the loop stop when it encounters error anyway
                    text.remove(stopword[i])
                    self.stop.append(stopword[i])

            except:
                continue

        self.textArr = text #return cleaned array

    def Print(self):
        print()
        print("Article:", self.title)
        print("Positive:", end="")
        for i in self.positive:
            print(i, end=",")
        print()
        print("Negative:", end="")
        for i in self.negative:
            print(i, end=",")
        print()
        print("Positive Words Count:", len(self.positive))
        print("Negative Words Count:",len(self.negative))

        print("Stopwords:", end="")
        for i in self.stop:
            print(i, end=",")

    def PosiNeg(self):
        #positive words store
        posiTree = Tries.Tries()
        posi = open("positive.txt", "r")
        text = posi.read()
        text = text.lower()
        key = text.split('\n')

        for i in range(len(key)):#insert
            posiTree.insert(key[i])


        #negative words store
        negTree = Tries.Tries()
        neg = open("negative.txt", "r")
        text = neg.read()
        text = text.lower()
        key = text.split('\n')

        for i in range(len(key)):#insert
            negTree.insert(key[i])
        for i in range(len(self.textArr)):
            if (negTree.search(self.textArr[i])):
                self.negative.append(self.textArr[i])
            elif (posiTree.search(self.textArr[i])):
                self.positive.append(self.textArr[i])
            else:
                self.neutral.append(self.textArr[i])
