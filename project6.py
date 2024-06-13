# Project 6
# CMSC 254
# <Zerlyne>
# CMSC 254 Project 6 Template

import random


# Accepts a valid email address as a parameter
# and returns the normalized email address.
def normalizeEmail(emailIn):
#     Add your code here and replace the return statement
    personName, domain = map(str.lower, emailIn.split('@'))
    if domain == 'gmail.com':
        personName = personName.replace('.', '')
        if '+' in personName:
            personName, z = personName.split('+', 1)
    
    return f'{personName}@{domain}'

# Accepts a file name as a parameter and
# returns a dictionary with normalized email addresses as keys
# and the number of times that address is in the file as values.
def createDictionary(fileName):
    emailDict = dict()
#     Add your code here
    try:
        count = 0
        with open(fileName, 'r') as open_file:
            lines = open_file.readlines()
            for line in lines:
                key = line.split()[0]
                value = line.split()[0]
                if key not in emailDict.keys():
                    emailDict[key] = value
                    
                
        return emailDict       
        
    except FileNotFoundError:
        return("File cannot be opened: " + fileName)


# Accepts a dictionary as a parameter and
# returns a list of the normalized email addresses
# that have a value of 1.
def getEligibleEmails(emailDictionary):
    emailList = []
    #     Add your code here
    count = 0
    

    return emailList

# Accepts a list of email addresses as a parameter and
# returns a string with randomly selected email address from the list
def selectWinner(emailList):
    if emailList:
        winner = random.choice(emailList)
        
    else:
        return ''
    #     Add your code here

    return winner

if __name__ == "__main__":
    # Displays 'debraduke@gmail.com'
    print(normalizeEmail('debraduke+cmsc210@gmail.com'))
    # Displays 'debraduke@gmail.com'
    print(normalizeEmail('dEbRa.DuKe@gmail.com'))

    # Displays the number of unique emails --> 40 with sample file
    allEntries = createDictionary("allEmails.txt")
    print(len(allEntries))
    # Displays an error message if eml.txt doesn't exist
    fileError = createDictionary("eml.txt") # no file
    print(fileError)

    # Displays the number of email address with a value of 1 -->34 with sample file
    singleEmails = getEligibleEmails(allEntries)
    print(len(singleEmails))

    # Displays one email address randomly selected
    print(selectWinner(singleEmails))
