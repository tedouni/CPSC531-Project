import sqlite3

conn = sqlite3.connect('spamfilter.db')
c = conn.cursor()
def createTables():

    c.execute('''CREATE TABLE wordfilter
                 (word text UNIQUE, spamfrequency real, hamfrequency real, spamprobability real, hamprobability real)''')  # Create table

def insertWords(word,spamfrequency,hamfrequency):
    try:
      c.execute("INSERT INTO wordfilter VALUES (?,?,?,?,?)",[word,spamfrequency,hamfrequency,0,0])
    except:
      word
        # c.execute("INSERT INTO wordfilter VALUE (?)", word)
# Insert a row of data
def checkWords(word):
    res=c.execute("select word from wordfilter where word ='{}'".format(word))
    return  res.rowcount
# Save (commit) the changes

def updateFrequencies(word,isHam):
    if isHam:
        c.execute("update wordfilter set hamfrequency=hamfrequency+{} where word='{}'".format(1,word))
    else:
        c.execute("update wordfilter set spamfrequency=spamfrequency+{} where word='{}'".format(1, word))

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

def endDbOperations():
    conn.commit()
    conn.close()
