from ParseEmail import parseEmail
import os
from DatabaseManage import retrieveConditional
from DatabaseManage import doesWordExist
from decimal import Decimal




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
    pathHam = '/Users/tedouni/Desktop/531Project/testData/ham/'
    pathSpam = '/Users/tedouni/Desktop/531Project/testData/spam/'

    actualNumOfSpam = 0
    calcNumOfSpam = 0
    actualNumOfHam = 0
    calcNumOfHam = 0
    calcEqualProb = 0
    calcUnknown = 0


    #SPAM dir
    for fileName in os.listdir(pathSpam):
        wordList = parseEmail(pathSpam + fileName)
        actualNumOfSpam += 1


        conditionalProbIsSpam = calculateConditionalForEmail(wordList, True)
        conditionalProbNotSpam = calculateConditionalForEmail(wordList, False)


        calcProbIsSpam = Decimal(conditionalProbIsSpam) * Decimal(pIsSpam)
        calcProbIsHam = Decimal(conditionalProbNotSpam) * Decimal(pIsHam)

        if(calcProbIsSpam > calcProbIsHam):
            calcNumOfSpam += 1
            #E-mail is calculated to be spam
        elif(calcProbIsSpam == calcProbIsHam):
            calcEqualProb += 1
            print 'EQUAL in SPAM'

        elif(calcProbIsHam > calcProbIsSpam):
            #E-mail is calculated to NOT be spam
            calcNumOfHam += 1
        else:
            calcUnknown += 1
            print 'unknown in spam'
            print (calcProbIsSpam,calcProbIsHam)



    #HAM dir

    for fileName in os.listdir(pathHam):
        wordList= parseEmail(pathHam + fileName)

        actualNumOfHam += 1


        conditionalProbIsSpam = calculateConditionalForEmail(wordList, True)
        conditionalProbNotSpam = calculateConditionalForEmail(wordList, False)


        calcProbIsSpam = Decimal(conditionalProbIsSpam) * Decimal(pIsSpam)
        calcProbIsHam = Decimal(conditionalProbNotSpam) * Decimal(pIsHam)
        if(calcProbIsSpam > calcProbIsHam):
            calcNumOfSpam += 1
            #E-mail is calculated to be spam
        elif(calcProbIsSpam == calcProbIsHam):
            calcEqualProb += 1
            print 'EQUAL in HAM'

        elif(calcProbIsHam > calcProbIsSpam):
            #E-mail is calculated to NOT be spam
            calcNumOfHam += 1
        else:
            calcUnknown += 1
            print 'unknown in ham'
            print (calcProbIsSpam,calcProbIsHam)


    print 'Calculated Spam,  actual number of spam'
    print calcNumOfSpam,actualNumOfSpam
    print 'calculated not spam, actual number of not spam'
    print calcNumOfHam, actualNumOfHam
    print 'undetermined'
    print calcUnknown
