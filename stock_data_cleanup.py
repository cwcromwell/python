import json
import sys

##
# a data cleanup script that does the following: 
# replace single quotes with double-quotes
# replaces "None" with "null" -- for use by Python
# loads JSON
##


with open("data_and_calc.json","r") as f:
   content = str(f.read())
#print(content)
content = content.replace("\'", "\"")
content = content.replace("None", "null")
with open("data_and_calc.json","w") as g:
   g.write(content)
with open("data_and_calc.json",  "r", encoding="utf-8") as h:
   data = json.load(h)
#print(data)

for record in data:
   if "NVDA" in str(record):
     print("Found record: ")
     print(record)



