import ParseEmail


def analyzeEmail(bodyOfEmail, isSpam, totalSpamWord, totalHamWord):

    if(isSpam):

        #TODO:Check if word exist in database, if so increase  for spam frequency

        totalSpamWord += 1


    else:   #Not Spam
    #TODO:Check if word exist in database, if so increase for ham frequency
        totalHamWord += 1


def train(totalSpamWord,totalHamWord,totalEmail,numberOfSpam):
    #initiate
    totalEmail = 0
    numberOfSpam = 0


    #start train for spam
    #spamData = emails that are spam
    #hamData = emails that are not spam


    #TODO: Change for loop to iterate through all files in spam directory.
    #Call parseemail to parse email to return body (wihtout html)
    for email in spamData:
        numberOfSpam += 1
        totalEmail += 1

    for email in hamData::
        totalEmail += 1
