#!/usr/bin/python3

# This snippet collects the file names for all the files in a ditamap and creates an array so that all the files can be subsequently modified


ditamapFile="askme.ditamap"

# Get beautifulsoup4
from bs4 import BeautifulSoup

# Get ditamap and read
map=open("../ama-api-2021/src/en/askme.ditamap").read()
soup = BeautifulSoup(map, 'xml')

# Get topicrefs out of ditamap
stew = soup.find_all('topicref')
# Retrieve href attribute from each topicref and write to a new list, after replacing the ".md" extension with ".html"
# Because list of files is needed in order to add the analytics tags. Ditamap is the master list, but source files have a different extention from output files.
print("ATTEMPTING TO GATHER INDIVIDUAL FILENAMES")
stewList = []
for item in stew:
    link_text = item['href']
    print ("adding " + link_text)
    stewList.append(link_text.replace(".md", ".html"))


print("ATTEMPTING TO CREATE FILE LIST")
print(stewList)

print("___")
print("Number of items in list: ")
print(len(stewList))
