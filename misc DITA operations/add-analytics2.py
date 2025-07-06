#!/usr/bin/python3

# PROBLEM: Google analytics tags are inserted in the head element of each HTML page. This would be difficult to accomplish while the pages are built, because SSGs don't take Google analytics into account. It's also tedious to manually add the tags after pages are built.
# SOLUTION: This script appends tags to all the HTML files in a simple website.

# Set variables
# Get your analytics script from google and store it in an XHTML or HTML file. Store the file name in the analyticsTags variable.
homepage = ["askme/index.html"] #The path and name for the index.html page, if it is not in the content directory. Must be a single-item list.
dirName = "askme/topics/" # directory that contains all the output files except index.html
analyticsTags="google-analytics.xhtml" # the name of the file that contains the google analytics tags
tagComment="!-- Global site tag (gtag.js) - Google Analytics --"
verbose = True


# Beautiful Soup to Pythonically parse HTML and grab elements in JQUERY-like fashion
from bs4 import BeautifulSoup
# OS to get a list of files in the directory
import os

# Open and read the analytics tags so the contents can be inserted as-is
tags=open(analyticsTags).read()
if verbose:
    print("PRINTING ANALYTICS SCRIPT")
    print(tags)

# Read a list of files in the output directory to find out which files you should modify
fileList = os.listdir(dirName)
if verbose:
    print("PRINTING FILE LIST")
    print(fileList)


# Open each file; append the analytics tags within the <head> element; write back to the file
print("PROCESSING")
for fileName in fileList:
    if ".html" not in fileName:
        continue
    fileName = dirName + fileName
    if verbose:
        print ("Processing file: " + fileName)
    bone = open(fileName).read()
    soup = BeautifulSoup(bone, 'html.parser')
    if tagComment not in bone: # avoids inserting analytics tags multiple times if things go badly and this script is re-started after doing half the job
        print("No analytics script found in: index.html. Inserting.")
        soup.head.insert(-0, tags)
    else:
        print("Analytics comment found. Analytics script was already inserted in: ", fileName, ". Skipping.")
        continue # Don't need to write the file if it already contains the analytics script and we're not inserting. Jumps to next file.

    if verbose:
        print("Writing file. Current fileName is : " + fileName)
    f = open(fileName, "w")
    f.write(str(soup))
    f.close()

# processing index.html separately -- only because it is not in the same folder with the content
#looping so we can use "continue" if we decide not to write the page. That's why homepage is a list.
for item in homepage:
    if verbose:
        print ("Processing homepage")
    bone = open(homepage[0]).read()
    soup = BeautifulSoup(bone, 'html.parser')
    if tagComment not in bone:
        print("No analytics script found in ", homepage[0], " Inserting.")
        soup.head.insert(-0, tags)
    else:
        print("Analytics comment found. Analytics script was already inserted in: ", homepage[0], ". Skipping.") # Don't need to write the file if it already contains the analytics script and we're not inserting. Jumps to next file.
        continue
    if verbose:
        print("Writing file. Current fileName is ", homepage[0])
    f = open(homepage[0], "w")
    f.write(str(soup))
    f.close()
print("PROCESSING COMPLETED: GOOGLE ANALYTICS TAGS WERE INSERTED.")
