from ParseEmail import parseEmail
import os
from DatabaseManage import retrieveConditional
from DatabaseManage import doesWordExist
from decimal import Decimal


def analysis(actualNumOfHam,actualNumOfSpam,correctPredictions,incorrectPredictions,spamCalcToHam ,hamCalcToSpam,pIsSpam,pIsHam):
    total = actualNumOfHam+actualNumOfSpam
    accuracy = correctPredictions/float(total)
    print 'P(isSpam): ',pIsSpam
    print 'P(~spam): ',pIsHam
    print 'Actual spam e-mails: ',actualNumOfSpam
    print 'Actual non-spam e-mails: ', actualNumOfHam
    print 'Accuracy: ', correctPredictions, accuracy
    error = incorrectPredictions/float(total)
    print 'Error:', incorrectPredictions, error
    print 'non-spam e-mails determined to be spam: ',hamCalcToSpam
    print 'spam e-mails determined to be non-spam: ',spamCalcToHam





#calculate
def calculateConditionalForEmail(wordList,isSpam):

    multiples = 1.0

    for word in wordList:
        #CHECK IF WORD IS IN DATABASE.
        #if word is in database:
        wordExist = doesWordExist(word)
        if(wordExist):
            #returned as Decimal
            conditonal = retrieveConditional(word,isSpam)
            if (conditonal == 0):
                #skip calculation if 0
                pass
            else:

                multiples = Decimal(multiples)*conditonal
        else:
            #word doesn't exist, ignore.
            # print word
            pass

    return multiples

def classify(totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam):
    pathHam = '/Users/tedouni/Desktop/CPSC531-Project/testData/ham/'
    pathSpam = '/Users/tedouni/Desktop/CPSC531-Project/testData/spam/'

    #incase run program without trainData
    #will load totalSpamword and totalHamWord from text fileName

    tempFileName = 'numOfWords.txt'

    if(numberOfSpam == 0):

        with open(tempFileName) as f:
            tempList = f.read().split()

        numberOfSpam = float(tempList[0])
        numberOfHam = float(tempList[1])
        totalSpamWord = float(tempList[2])
        totalHamWord = float(tempList[3])
        pIsSpam = float(tempList[4])
        pIsHam = float(tempList[5])
        f.close()


    actualNumOfSpam = 0
    calcNumOfSpam = 0
    actualNumOfHam = 0
    calcNumOfHam = 0
    calcEqualProb = 0
    correctPredictions = 0
    incorrectPredictions = 0
    spamCalcToHam = 0
    hamCalcToSpam = 0



    #SPAM dir
    for fileName in os.listdir(pathSpam):
        wordList = parseEmail(pathSpam + fileName)
        actualNumOfSpam += 1


        conditionalProbIsSpam = calculateConditionalForEmail(wordList, True)
        conditionalProbNotSpam = calculateConditionalForEmail(wordList, False)


        calcProbIsSpam = Decimal(conditionalProbIsSpam) * Decimal(pIsSpam)
        calcProbIsHam = Decimal(conditionalProbNotSpam) * Decimal(pIsHam)

        #E-mail is calculated to be spam
        if(calcProbIsSpam > calcProbIsHam):
            calcNumOfSpam += 1
            correctPredictions += 1
        #E-mail is calculated to NOT be spam
        else:
            calcNumOfHam += 1
            spamCalcToHam += 1
            incorrectPredictions += 1




        # print 'calcIsSpam,calcNotSpam: ',calcProbIsSpam,' ',calcProbIsHam


    #HAM dir

    for fileName in os.listdir(pathHam):
        wordList= parseEmail(pathHam + fileName)

        actualNumOfHam += 1


        conditionalProbIsSpam = calculateConditionalForEmail(wordList, True)
        conditionalProbNotSpam = calculateConditionalForEmail(wordList, False)


        calcProbIsSpam = Decimal(conditionalProbIsSpam) * Decimal(pIsSpam)
        calcProbIsHam = Decimal(conditionalProbNotSpam) * Decimal(pIsHam)

        #E-mail is calculated to be spam
        if(calcProbIsSpam > calcProbIsHam):
            calcNumOfSpam += 1
            incorrectPredictions += 1
            hamCalcToSpam += 1

        #E-mail is calculated to NOT be spam
        else:
            calcNumOfHam += 1
            correctPredictions += 1



        # print 'calcIsSpam,calcNotSpam: ',calcProbIsSpam,' ',calcProbIsHam

    analysis(actualNumOfHam,actualNumOfSpam,correctPredictions,incorrectPredictions,spamCalcToHam ,hamCalcToSpam,pIsSpam,pIsHam)
