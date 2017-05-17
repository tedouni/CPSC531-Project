from ParseEmail import parseEmail
import os
from DatabaseManage import addWord
from DatabaseManage import createTable


def analyzeEmail(bodyOfEmail, isSpam, totalSpamWord, totalHamWord):

    if(isSpam):
        #TODO:Check if word exist in database
        #if so increase  for spam frequency
        #else create entry for data base and set spam frequency to 1 and HAM =0
         for word in bodyOfEmail:
             addWord(word,isSpam)



    else:   #Not Spam
    #TODO:Check if word exist in database,
    #if so increase for ham frequency
    #Else create entry for database and set HAM (not spam) frequency to 1 and spam = 0
        for word in bodyOfEmail:
            addWord(word,isSpam)





def train(totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam):


    #start train for spam
    #spamData = emails that are spam
    #hamData = emails that are not spam
    tempFileName = 'numOfWords.txt'

    try:
        os.remove(tempFileName)

    except:
        print tempFileName,' does not exist'

    try:
        os.remove('keywords.db')
        print 'Success in deleting keywords.db'
    except:
        print 'keywords.db does not exist, creating'

    createTable()
    pathHam = '/Users/tedouni/Desktop/CPSC531-Project/trainData/ham/'
    pathSpam = '/Users/tedouni/Desktop/CPSC531-Project/trainData/spam/'

    #SPAM
    print 'Doing SPAM Directory'

    for fileName in os.listdir(pathSpam):
        wordList = parseEmail(pathSpam + fileName)

        tempNumOfWordInEmail = len(wordList)
        totalSpamWord += tempNumOfWordInEmail

        numberOfSpam += 1
        totalEmail += 1
        analyzeEmail(wordList,True,totalSpamWord,totalHamWord)


    #HAM
    print 'Doing HAM Directory'

    for fileName in os.listdir(pathHam):
        wordList= parseEmail(pathHam + fileName)
        numberOfHam += 1
        totalEmail += 1

        tempNumOfWordInEmail = len(wordList)
        totalHamWord += tempNumOfWordInEmail

        analyzeEmail(wordList,False,totalSpamWord,totalHamWord)


    pIsHam = float(numberOfHam)/float(totalEmail)
    pIsSpam = float(numberOfSpam)/float(totalEmail)


    #Store totalSpamWord and totalHamWord
    target = open(tempFileName, 'w')
    target.write(str(numberOfSpam))
    target.write(' ')
    target.write(str(numberOfHam))
    target.write(' ')
    target.write(str(totalSpamWord))
    target.write(' ')
    target.write(str(totalHamWord))
    target.write(' ')
    target.write(str(pIsSpam))
    target.write(' ')
    target.write(str(pIsHam))
    target.close()

    # print numberOfSpam
    # print numberOfHam
    # print totalSpamWord
    # print totalHamWord
    return totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam
