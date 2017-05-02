from ParseEmail import parseEmail
import os
from createDatabase import checkWords
from createDatabase import updateFrequencies
from createDatabase import insertWords




def calculateConditional(databaseConnection):
    #use this at the end of training data
    #used to calculate P(B_i |A_x) and P(B_i | NOT A_x)

    # TODO:

    #iterate through database :
    #spam

    #P(word |A)
    #db.bGivenA = db.wordFreqForSpam/(float)totalSpamWord

    #ham


    #P(word | NOT A)
    #db.bGivenNotA =wordFreqForHam/(float)totalHamWord


def retrieveConditional(word,isSpam, databaseConnection):
    if(isSpam):

        # TODO:
        #retrieve value ,   isSpam means look for bGivenA
        return bGivenA

    else:
        # retrieve value ,   not spam means look for bGivenNotA
        return bGivenNotA


#calculate
def calculateConditionalForEmail(wordList,isSpam,databaseConnection):

    multiples = 1.0

        for word in wordList:
            #CHECK IF WORD IS IN DATABASE.
            #if word is in database:

                conditonal = retrieveConditional(word,isSpam,databaseConnection)
                multiples *= conditonal

            #else (word not in database):
                #pass

    return multiples

def classify(totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam):
    pathHam = '/Users/tedouni/Desktop/531Project/testData/ham/'
    pathSpam = '/Users/tedouni/Desktop/531Project/testData/spam/'

    actualNumOfSpam = 0
    calcNumOfSpam = 0
    actualNumOfHam = 0
    calcNumOfHam = 0

    #initiate database connection
    calculateConditional(databaseConnection)

    #SPAM dir
    for fileName in os.listdir(pathSpam):
        wordList = parseEmail(pathSpam + fileName)

        actualNumOfSpam += 1

        conditionalProbIsSpam = calculateConditionalForEmail(wordList, True, databaseConnection)
        conditionalProbNotSpam = calculateConditionalForEmail(wordList, False, databaseConnection)


        calcProbIsSpam = conditionalProbIsSpam * pIsSpam
        calcProbIsHam = conditionalProbNotSpam * pIsHam

        if(calcProbIsSpam > calcProbIsHam):
            calcNumOfSpam += 1
            #E-mail is calculated to be spam
            pass
        else:
            #E-mail is calculated to NOT be spam
            calcNumOfHam += 1
            pass

    #HAM dir
    for fileName in os.listdir(pathHam):
        wordList= parseEmail(pathHam + fileName)

        actualNumOfHam += 1


        conditionalProbIsSpam = calculateConditionalForEmail(wordList, True)
        conditionalProbNotSpam = calculateConditionalForEmail(wordList, False)


        calcProbIsSpam = conditionalProbIsSpam * pIsSpam
        calcProbIsHam = conditionalProbNotSpam * pIsHam

        if(calcProbIsSpam > calcProbIsHam):
            calcNumOfSpam += 1
            #E-mail is calculated to be spam
            pass
        else:
            #E-mail is calculated to NOT be spam
            calcNumOfHam += 1
            pass

    # TODO: Create function for statistic accuracy etc.
