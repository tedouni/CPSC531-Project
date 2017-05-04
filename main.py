#!/usr/bin/env python
# -*- coding: utf-8 -*-
from TrainData import train
from TrainData import analyzeEmail
import os
from DatabaseManage import createTable
import time
from DatabaseManage import updateConditionals
from ClassifyEmail import classify



# import createDatabase
#
# Number of Spam emails 1398
# Number of Ham emails 5052
# Total emails = 6450
#
# Prob(Spam) = 0.21665632754
# Prob(~Spam) = 1- P(spam)= 0.78334367246
#
# P(A|B) = P(B|A) P(A)
#         -------------
#         P(B)
# Given A = Spam, B = Contents of Email
# IF P(A)*P(B|A) > P(NOT A)*P(B|NOT A)) then email is spam
# P(B) not relevant since common divisor
# P(A), P(~A) already calculated
# Need to calculate P(B|A) and P(B|~A)
#
# Will need to use bag of words model to calculate P(B|A) and P(B|~A)
# Will pay attention to frequency of words
# To calculate P(apple | spam), would count the number of times apple appears in
# all of the spam emails and divide by the total number of words in all spam emails


def main():
    #Create database

    #Initiate to 0

    start = time.time()
    print ("start of program")

    totalSpamWord =0
    totalHamWord =0
    totalEmail =0
    numberOfSpam = 0
    numberOfHam = 0
    pIsSpam = 0
    pIsHam = 0

    #Create database
    createTable()

    #train data
    totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam = train(totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam)

    #Calculate conditionals for all words in test data
    updateConditionals(totalSpamWord,totalHamWord)
    classify(totalSpamWord,totalHamWord,totalEmail,numberOfSpam,numberOfHam,pIsSpam,pIsHam)


    print pIsHam
    print pIsSpam
    print totalEmail
    print numberOfSpam
    print numberOfHam
    # print totalSpamWord
    # print totalHamWord

    end = time.time()
    print end - start





if __name__ == '__main__':
    main()
