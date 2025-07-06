
##
# A very primitive Wordle-solver. Requires that you know three letters already.
# Instructions: 
# * Remaining letters go in the list. 
# * Revise line 21 to reflect the pattern of missing letters and known letters
##

list = ["q", "w", "o", "p",  "f", "g", "h", "j", "k", "z", "x", "v", "b", "n", "m"]
candidates = []
words = []

mydict=open("/usr/share/dict/web2", "r").read()
# f = open("demofile.txt", "r")

if "letter" in mydict:
    print("dictionary test successful")
else:
    print("dictionary test failed")
    exit()

for letter in list:
  for x in range(len(list)):
    candidates.append(("kno" + letter + list[x] ))

print("List completed")
print("candidates:")
print(candidates)
print("checking candidates")


for c in candidates:
    if c in mydict:
        words.append(c)

if len(words)==0:
  print("No words found.")
else:
  print("Words found: ")
  print(words)
