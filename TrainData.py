from ParseEmail import parseEmail
import os
from DatabaseManage import addWord




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



    pathHam = '/Users/tedouni/Desktop/531Project/trainData/ham/'
    pathSpam = '/Users/tedouni/Desktop/531Project/trainData/spam/'

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




    return totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam
