from random import shuffle

#welcome message and prompt
print("Welcome to 100 prisoners problem!")
x = input("Enter an even number of prisoners to emulate: ")
numPrisoners = int(x)

#only allows even numbers to be entered
while numPrisoners % 2 == 1:
    x = input("Enter an even number of prisoners to emulate: ")
    numPrisoners = int(x)

#creates a list of size entered by user, shuffes it
prisonerList = [i for i in range(numPrisoners)]

def singlePrisoner(i):# decides if a single prisoner succeeds
    prisonerNumber = i
    attempts = 0
    while prisonerNumber != prisonerList[i]:
            i = prisonerList[i]
            attempts = attempts + 1
            if attempts == numPrisoners/2:
                return False
    return True

def allPrisoners():#iterates for all prisoners
    prisonerSuccess = 0
    for i in range(numPrisoners):
        if singlePrisoner(i):
            prisonerSuccess = prisonerSuccess + 1
    if prisonerSuccess == numPrisoners:
        return True
    else:
        return False
    
trialSuccess = 0

for i in range (100):#iterates for 100 trials
     newPrisonerList = shuffle(prisonerList)
     if allPrisoners():
         trialSuccess = trialSuccess + 1

print("%s" % "Number of successful trials: " + str(trialSuccess) + "/100")#prints the number of successful trials out of 100 
