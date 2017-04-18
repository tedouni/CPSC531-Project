#http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
#to strip html


import email
import os
from HTMLParser import HTMLParser


import email
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


with open('0022.7241da4491c49b50c0470a3638ee35c4') as f:
    text = f.read()
    e = email.message_from_string(text)
    body = e.get_payload()
    if isinstance(body, list):
        body = ''.join(map(str,body))
    body = strip_tags(body)
    print body
