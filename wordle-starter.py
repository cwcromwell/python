#!/usr/bin/python3


wordstring=open("wordle-answer-list.txt", "r").read()
wordlist = wordstring.split()
#print("Here's the list:")
#print(wordlist)

dictionary=open("dict-link", "r").read().split()

if "alpha" in dictionary:
    print("dictionary is loaded")
else:
    print("dictionary broken")



# To count the number of occurences of every character (includes white spaces and newlines)
myDict = {}
for word in dictionary:
    #print("current word: ", word)
    if len(word)==5:
        print("Five-letter word: ", word)
        for char in word:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1
print(myDict)

# To create a list sorted in order of the most commonly occuring characters
myList = sorted(myDict.items(), key=lambda x:x[1])
print("sorted list")
print(myList)

# To convert the above list into a sorted dictionary
sortdict = dict(myList)
print("Sorted dictionary: ")
print(sortdict)


## Next steps:
## determine most commonly used letters

## extract a list of five-letter words from the dictionary
## re-calculate the list of commonly used letters based on the dictionary, rather than the set of wordle results. Is it different?

## list of words containing the most commonly used letters (search dictionary for matches)
## measure performance of the starter words found in the above steps. Which of them return the most hits against the actual Wordle answers? Which return the most hits against the five-letter words in the dictionary?

## list of words containing the least commonly occuring letters.
## A matrix of words combining each letter of the alphabet with the largest possible number of characters from the 10-least-used list. So that I can play Wordle in hard mode and lose.
## Optimize the list to find the smallest number of correct answers in a game.

# a program capable of playing wordle to win or to lose would be worth doing.
