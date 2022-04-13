# Gets a list of all possible solutions in the answers.text file
def getAnswers():                               
    with open('answers.txt') as p:              #Opens .txt as "P"
        answers = []                            #Sets empty list
        for line in p:                          #Itterate through all lines
            answers.append(line.strip('\n'))    #Adds to list, removes \n
        return answers                          #Returns list

# Takes a dictionary and provides most common letters
# Might need to do more than 6, depending on how answer probability
def getLetters(letterCount):
    return sorted(letterCount, key=letterCount.get, reverse=True)[:6]  #Sorts dictionary by key values, and gets last 6

#Gets count of all letters in answer list, adds to dictionary
#Needs list as input
def getLetterCount(allAnswers):
    letterCount = {}                        #Sets empty DICT
    for answer in allAnswers:               #Itterate through list
        for letter in answer:               #Itterate through word
            letterCount[letter] = letterCount.get(letter, 0) + 1        #adds letter to dictionary, 0 is placed if null before adding 1
    return letterCount                      #Returns dictionary of letters and count of occurance

#Takes list of possible answers, and list of letters to find words with those letters
def getWord(allAnswers, letters):           
    words = []                                  #empty list
    for answer in allAnswers:                   #Itterate through words in list
        i = 0                                   #letter counter
        j = 0                                   #letters in word counter
        while i < len(letters):                 #letter counter to go through all letters
            if letters[i] in answer:            #if letter in letters is in word add one
                j += 1                          #adds one
            if j == 5:                          #if all 5 letters are in word add to list
                words.append(answer)            #adds word to list
            i += 1                              #adds 1 to check next letter in letters
    return words                                #returns list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    theAnswer = [0, 0, 0, 0, 0]                 # 0 = not in word, 1 = in word, wrong place, 2 = in word, correct place
    guessLimit = 7                              # Variable to limit guesses (easy mode / hard mode ? )

    allAnswers = getAnswers()                   # stores list of words in memory 

    letterCount = getLetterCount(allAnswers)    # gets dictionary for # of occurences of letters in previous list

    letters = getLetters(letterCount)           # gets most common letters from previous dict 

    firstWordToGuess = getWord(allAnswers, letters)     #gets best next guesses (current, no in depth probability


while guessLimit > 0:                           #while loop vs guess limit
    x = input("userInput Request here")         #get user input
    guessLimit -= 1                             #user input = guess limit goes up 1

