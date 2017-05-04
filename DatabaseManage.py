#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os
from decimal import Decimal

def createTable():
    conn = sqlite3.connect('keywords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS keywords
             (keyword TEXT, spamFrequency REAL , hamfrequency REAL, bGivenA TEXT, bGivenNotA TEXT)''')

    conn.commit()
    conn.close()

def doesWordExist(word):
    conn = sqlite3.connect('keywords.db')
    conn.text_factory = str
    c = conn.cursor()

    c.execute("SELECT keyword FROM keywords WHERE keyword = ?", [word])
    data=c.fetchone()

    if data is None:
        return False
    else:
        return True


def retrieveConditional(word, isSpam):
    conn = sqlite3.connect('keywords.db')
    conn.text_factory = str
    c = conn.cursor()

    if(isSpam):

        # TODO:
        #retrieve value ,   isSpam means look for bGivenA
        c.execute("SELECT bGivenA FROM keywords WHERE keyword = ? ",[word])
        tempList =  list(c.fetchone())
        bGivenA = tempList[0]
        conn.commit()
        conn.close()

        return Decimal(bGivenA)

    else:
        # retrieve value ,   not spam means look for bGivenNotA
        c.execute("SELECT bGivenNotA FROM keywords WHERE keyword = ? ",[word])
        tempList =  list(c.fetchone())
        bGivenNotA = tempList[0]
        conn.commit()
        conn.close()

        return Decimal(bGivenNotA)


def addWord(word, isSpam):
    conn = sqlite3.connect('keywords.db')
    conn.text_factory = str
    c = conn.cursor()

    wordExist = True #temp
    # TODO: CHECK IF WORD EXIST FIRST

    c.execute("SELECT keyword FROM keywords WHERE keyword = ?", [word])
    data=c.fetchone()

    if data is None:
        wordExist = False
    else:
        wordExist = True

    if (wordExist):
        if (isSpam):
            c.execute("SELECT spamFrequency FROM keywords WHERE keyword = ? ",[word])
            tempRet =  list(c.fetchone())
            tempFreq = tempRet[0]
            tempFreq += 1
            c.execute('''UPDATE keywords SET spamFrequency = ? WHERE keyword = ? ''', (tempFreq, word))
        else:
            c.execute("SELECT hamFrequency FROM keywords WHERE keyword = ? ",[word])
            tempRet =  list(c.fetchone())
            tempFreq = tempRet[0]
            tempFreq += 1
            c.execute('''UPDATE keywords SET hamFrequency = ? WHERE keyword = ? ''', (tempFreq, word))


    else:
        if(isSpam):
            c.execute("INSERT INTO keywords VALUES (?,?,?,?,?)",(word,1,0,0,0))

        else:
            c.execute("INSERT INTO keywords VALUES (?,?,?,?,?)",(word,0,1,0,0))


    conn.commit()
    conn.close()

def updateConditionals(totalSpamWord,totalHamWord):
    conn = sqlite3.connect('keywords.db')
    conn.text_factory = str
    c = conn.cursor()

    c.execute('SELECT * FROM keywords')
    table = c.fetchall()
    for row in table:
        word = row[0]
        # print word

        #get spamFrequency for word
        c.execute("SELECT spamFrequency FROM keywords WHERE keyword = ? ",[word])
        tempRetS =  list(c.fetchone())

        spamFreq = tempRetS[0]



        #get hamFrequency for word
        c.execute("SELECT hamFrequency FROM keywords WHERE keyword = ? ",[word])
        tempRetH =  list(c.fetchone())

        hamFreq = tempRetH[0]

        #now do calculation

        #P(word |A)
        #db.bGivenA = db.wordFreqForSpam/totalSpamWord
        tempBGivenA = Decimal(spamFreq)/Decimal(totalSpamWord)

        #P(word | NOT A)
        #db.bGivenNotA =wordFreqForHam/totalHamWord
        tempBGivenNotA = Decimal(hamFreq)/Decimal(totalHamWord)

        c.execute('''UPDATE keywords SET bGivenA = ? WHERE keyword = ? ''', (str(tempBGivenA), word))

        c.execute('''UPDATE keywords SET bGivenNotA = ? WHERE keyword = ? ''', (str(tempBGivenNotA), word))
        # print tempBGivenA, tempBGivenNotA


    conn.commit()
    conn.close()
