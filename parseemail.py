#http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
#to strip html


import email
import os
import string
from HTMLParser import HTMLParser

from os.path import dirname, basename


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def convertToList(body):
    #Remove HTML
    body = strip_tags(body)

    #remove punctuation
    for p in string.punctuation:
        body = body.replace(p,'')

    #To Lower
    body = body.lower()

    #Split into list of words
    listOfWords = body.split()

    return listOfWords




with open('02474.c76ffef81a2529389e6c3bbb172184d7') as f:
    text = f.read()
    e = email.message_from_string(text)
    body = e.get_payload()
    if isinstance(body, list):
        body = ''.join(map(str,body))
    print body
    print '\n\n\n'
    print 'List as follows:'
    words = convertToList(body)
    print words
