import urllib.request, urllib.error, urllib.parse
import web
import trie

url = ['https://www.dailymail.co.uk/news/article-2889112/A-million-parcels-stuck-depots-failure-courier-City-Link.html', 'https://www.independent.co.uk/news/business/news/city-link-hopelessly-insolvent-christmas-court-told-a6723556.html',
         'https://www.thestar.com.my/business/business-news/2007/02/02/courier-tieup-sri-lanka-firm-appoints-citylink-express']

tword = []
tstop = []
neu = []
pov = []
neg = []

for i in url:
    print('Article', i,
          '\n-------------------------------------------------------\n')
    response = urllib.request.urlopen(i)
    html = response.read()
    text = web.stripTags(html).lower()

    fullwordlist = web.stripNonAlphaNum(text)
    wordlist1 = web.remove(fullwordlist)
    stopwordCount = web.calculateStopWord(wordlist1)  #calculate
    wordlist2 = web.removeStopwords(wordlist1, web.stopwords)
    dictionary = web.wordListToFreqDict(wordlist2)
    sorteddict = web.sortFreqDict(dictionary)

    #for s in sorteddict:
    #    print(str(s))

    #print(dictionary.items())
    #print(wordlist2)
    sumWord = 0
    for i in dictionary.values():
        sumWord += i
    print("Total Words:", sumWord)
    print("Total Stop Words:", stopwordCount, "\n")
    tword.append(sumWord)
    tstop.append(stopwordCount)

    tr = trie.Trie()

    for key, value in dictionary.items():
        tr.insert(key, value)

    key1 = []
    #badWord
    with open("badWord.txt", "r") as a_file:
        total = []
        for line in a_file:
            for currentline in line.strip().split(', '):
                output = tr.search(currentline)
                if output:
                    x = output[0]
                    y = output[1]
                    print(x)
                    key1 += x
                    total.append(y)

        sumBad = 0
        for i in total:
            sumBad += i
        print('\nTotal Negative Words: ', sumBad, '\n')
        neg.append(sumBad)

    #postiveWord
    with open("positiveWord.txt", "r") as b_file:
        total = []
        for line in b_file:
            for currentline in line.strip().split(', '):
                output = tr.search(currentline)
                if output:
                    x = output[0]
                    y = output[1]
                    print(x)
                    key1 += x
                    total.append(y)

        sumPos = 0
        for i in total:
            sumPos += i
        print('\nTotal Positive Words: ', sumPos)
        pov.append(sumPos)

    for j in key1:
        key = str(j)
        dictionary.pop(key)
    #print(dictionary.items())

    sumNeu = 0
    for key, value in dictionary.items():
        sumNeu += value
    neutralWord = list(dictionary.keys())
    #print(neutralWord)
    #print(dictionary.keys())
    print('Total Neutral Words: ', sumNeu, '\n')
    neu.append(sumNeu)


