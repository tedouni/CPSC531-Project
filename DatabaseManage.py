import sqlite3
import os



def createTable():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS keywords
             (keyword TEXT, spamFrequency REAL , hamfrequency REAL, bGivenA REAL, bGivenNotA REAL)''')

    conn.commit()
    conn.close()

def addWord(word, isSpam):
    conn = sqlite3.connect('example.db')
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



createTable()
addWord('testSpam',True)
addWord('testHam',False)
addWord('testSpam',True)
addWord('testSpam',True)
addWord('bamSpam',True)
