#!/usr/bin/python3

##
# To rank letters according to how frequently they appear in five-letter words, in English. 
# This can be used to select the most effective starter words in Wordle.
## 

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


# To create a list sorted in order of the most commonly occuring characters
myList = sorted(myDict.items(), key=lambda x:x[1])
# print("sorted list")
# print(myList)

# To convert the above list into a sorted dictionary
sortdict = dict(myList)
print("Sorted dictionary: how frequently each letter occurs in the full dictionary ")
print(sortdict)

wordle_dict = {}
for word in wordlist:
    #print("current word: ", word)
    if len(word)==5:
        print("Five-letter word: ", word)
        for char in word:
            if char in wordle_dict:
                wordle_dict[char] += 1
            else:
                wordle_dict[char] = 1
print("most common letters used in my saved wordle answers")
mynewlist = sorted(wordle_dict.items(), key=lambda x:x[1])
print(mynewlist)



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

# dictionary
# {'Q': 3, 'X': 7, 'Z': 14, 'Y': 23, 'W': 24, 'U': 29, 'V': 30, 'O': 38, 'F': 40, 'J': 50, 'R': 50, 'E': 53, 'I': 54, 'H': 55, 'N': 57, 'G': 64, 'D': 78, 'L': 83, 'K': 88, 'q': 95, 'P': 95, 'T': 97, 'B': 107, 'C': 115, 'M': 135, 'A': 169, 'S': 175, 'j': 198, 'x': 232, 'z': 294, 'v': 514, 'f': 697, 'w': 723, 'k': 1017, 'g': 1231, 'b': 1272, 'p': 1386, 'm': 1499, 'h': 1534, 'd': 1602, 'c': 1724, 'y': 1836, 'u': 2274, 't': 2639, 's': 2712, 'l': 2714, 'n': 2727, 'i': 3262, 'o': 3278, 'r': 3509, 'e': 4852, 'a': 5641}

# Letters grouped by dictionary usage: 
# a,e,r,o,i,n,l,s
# t,u,y,c,d,h,m,p
# b,g,k,w,f,v,z

# irony slate chump (dy)





# wordlist:
# [('x', 1), ('b', 4), ('g', 4), ('k', 4), ('v', 4), ('w', 5), ('u', 6), ('y', 6), ('f', 6), ('p', 10), ('m', 11), ('d', 12), ('c', 13), ('n', 14), ('h', 16), ('r', 19), ('i', 19), ('s', 19), ('l', 20), ('a', 22), ('o', 22), ('t', 24), ('e', 34)]

# Letters grouped by Wordle answers:
# e, t, o, a, l, s, i, r 
# h, c, n, d, m, p, f. y 
# u, w, v, k, g, b, x, 

# did not appear: j,q,z 



# shoal tried chump nfy