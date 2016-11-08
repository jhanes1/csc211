'''HW02: Python Review

These problems are (somewhat) representative of the sorts of
programming tasks you will need to be able to perform to create the
applications this class is designed to teach. You will (hopefully) be
able to solve these problems directly, but if you are having trouble
with them, then please use these problems as motivation for further
study.

Use the "Exercises" section from each chapter in "How to Think Like a
Computer Scientist" as a reference for further study.

'''

#----------------------------------------------------------------------
# Problem 0
#
# Create a function 'random_list' that generates a list containing 100
# random integers between 0 and 1000 (use iteration, append, and the
# random module).
#
# name: random_list
# parameters: none
# returns: (list) list of random integers between 0 and 1000
#
# Code goes below here

import random
def random_list():
    tempList = []
    for item in range(0,100):
        tempList.append(random.randint(0,1000))
    return tempList
#TEST rList = random_list()
#TEST print("randList:",len(rList))



#----------------------------------------------------------------------
# Problem 0.5
#
# Write a function called 'average' with a single parameter, 'numbers'
# (list), and return the average of all the numbers in that list.
#
# name: average
# parameters:
# - numbers (list)
# returns: (float) average of all the numbers in the list
#
# Code goes below here


def average(numbers):
    sum = 0
    for item in numbers:
        sum += item
    average = sum / len(numbers)
    return average
#TEST print("avrg:",average(rList))



#----------------------------------------------------------------------
# Problem 1
#
# Write a function to count how many even numbers are in a given
# list. Your function should be named "count_even" and it should take
# one parameter, "numbers" (a list).
#
# name: count_even
# parameters:
# - numbers (list)
# returns: (int) count of even numbers in the list
#
# Code goes below here



def count_even(numbers):
    count = 0
    for item in numbers:
        if item % 2 == 0:
            count += 1
    return count
#TEST print("cntEven:",count_even(rList))


#----------------------------------------------------------------------
# Problem 2
#
# Write a function to sum all the even numbers in a given list. Your
# function should be named "sum_even" and it should take one
# parameter, "numbers" (a list).
#
# name: sum_even
# parameters:
# - numbers (list)
# returns: (int) sum of even numbers in list
#
# Code goes below here


def sum_even(numbers):
    eSum = 0
    for item in numbers:
        if item % 2 == 0:
            eSum += item
    return eSum
#TEST print("sumEven:", sum_even(rList))




#----------------------------------------------------------------------
# Problem 3
#
# What is the longest word in Alice in Wonderland? You can obtain a
# free plain text version of the book, along with many others, from
# http://www.gutenberg.org. Go to this website and download the text
# of Alice in Wonderland. You will need to then upload it to your
# homework directory:
#
# /home/<username>/csc211/hw/hw2/<name_of_alice_textfile>
#
# To solve this problem, you will be creating TWO functions.
#
# Create a function 'word_count' that takes one parameter, "text" (a
# string), and returns a dictionary of all the words in this string.
#
# name: word_count
# parameters:
# - text (str)
# returns: (dict) map of word to count of occurrences
#
# You will also create a function 'longest_word_in_alice' that takes
# no parameters. It should:
#
# - Open the text file for "Alice in Wonderland" from gutenberg.org
# - Read the content into a string
# - Call 'word_count', retrieving the dictionary it returns
# - Find the longest word in that dictionary and return it
#
# name: longest_word_in_alice
# parameters: none
# returns: (str) longest word in "Alice in Wonderland"
#
# Code goes below here
from collections import Counter
def word_count(text):
    return Counter(text.split())

if 5 == 6:
    words = text.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

import re, string
def longest_word_in_alice():
    with open("/home/jhanes/csc211/hw/hw2/pg11.txt","rt") as rfp:
        booktxt = rfp.read()
    #booktxt = booktxt.replace('-', ' ').replace('/',' ').replace('gutenberg',' ').replace('@', ' ')
    booktxt = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', booktxt).lower()
    return max(word_count(booktxt), key=len)
#TEST print("alice:",longest_word_in_alice())

if 5 == 6:
    max_length, max_word = 0, None
    for word in count:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
    return max_word


#----------------------------------------------------------------------
# Problem 4
#
# KJV Bible class
#
# Create a new class, called 'Bible', that will provide an interface
# to the content of the 1611 King James translation of the Holy
# Bible. It should have a number of methods:
#
# - __init__ [i.e constructor]: The constructor should:
#     - take no parameters
#     - call the provided function 'read_bible' to load the Bible data
#       structure into memory
#     - save this data structure as the attribute 'verses'.
#
# - get_book
#
#    parameters:
#      - book (str): name of book to return
#
#    returns: (list) list of individual verse data structures (from
#       self.verses) whose book is equal to the given book name
#
# - get_chapter
#
#    parameters:
#      - book (str): name of book from which to find the chapter
#      - chapter (int): chapter number to return
#
#    returns: (list) list of individual verse data structures (from
#       self.verses) whose book is equal to the given book name and
#       whose chapter number is equal to the given chapter number
#
# - get_verse
#
#    parameters:
#      - book (str): name of book from which to find the chapter
#      - chapter (int): chapter number to return
#      - verse (int): verse number to return
#
#    returns: (list) list of individual verse data structures (from
#       self.verses) whose book is equal to the given book name and
#       whose chapter number is equal to the given chapter number and
#       whose verse number is equal to the given verse number
#
# EXTRA CREDIT
#
# - n_grams (ref: https://en.wikipedia.org/wiki/N-gram)
#
#    parameters:
#      - size (int): size of n-grams from which to build the table
#      - book (str, optional, default=None): name of book from which
#          to build N-gram table. If None, perform for whole Bible
#      - chapter (str, optional, default=None): name of chapter from
#          which to build N-gram table. If not None, assumes book has
#          been given (need to check and throw Exception if not
#          given). If None, perform for whole book.
#      - verse (str, optional, default=None): name of verse from which
#          to build N-gram table. If not None, assumes book and
#          chapter have been given (need to check and throw Exception
#          if not given). If None, perform for whole chapter.
#      - stopwords (list, optional, default=None): list of stop words to
#          ignore in building the n-gram table
#
#    returns: (dict) dictionary of n-gram to number of occurrences in
#       the given subset of the Bible



from functools import lru_cache
import gzip, csv
memoize = lru_cache(1)
@memoize
def read_bible():
    cols = ['book','chapter','verse','text']
    with gzip.open('/home/jhanes/csc211/hw/hw2/bible.tsv.gz','rt') as rfp:
        reader = csv.DictReader(rfp,cols,delimiter='\t')
        verses = list(reader)
    return verses

# Code goes below here

import re, string
from collections import Counter
class Bible:
    '''Entire Bible broken up into a list of DictObjs of each verse
        get_book(book),get_chapter(book,chapter),get_verse(book,chapter,verse),n_gram(size=1,book=None,chapter=None,verse=None,stopwords=None)
    '''
    def __init__(self):
        self.verses = read_bible()

    def get_book(self, book):
        '''Book is String and Return is (list)
        Return list of individual verse data structures (from self.verses)
        whose book is equal to the given book name
        '''
        bible = self.verses
        tlist = []
        for item in bible:
            if item["book"] == str(book).lower():
                tlist.append(item)
        return tlist

    def get_chapter(self, book, chapter):
        '''Book is String, Chapter is Int and Return (list)
        Return list of individual verse data structures (from self.verses)
        whose book is equal to the given book name and whose chapter number is equal to the given chapter number
        '''
        bible = self.verses
        tlist = []
        for item in bible:
            if item["book"] == str(book).lower() and item["chapter"] == str(chapter):
                tlist.append(item)
        return tlist

    def get_verse(self, book, chapter, verse):
        '''Book is String, Chapter is Int, Verse is Int and Return is (list)
        Return list of individual verse data structures (from self.verses)
        whose book is equal to the given book name and whose chapter number is equal to the given chapter number and
        whose verse number is equal to the given verse number
        '''
        bible = self.verses
        tlist = []
        for item in bible:
            if item["book"] == str(book).lower() and item["chapter"] == str(chapter) and item["verse"] == str(verse):
                tlist.append(item)
        return tlist

    def n_grams(self,size=1,book=None,chapter=None,verse=None,stopwords=None):
        '''Size: Int, Book: Str, Chapter: Str, Verse: Str, Stopwords: List, and Return: Dict
        Return dictionary of n-gram to number of occurrences in
        the given subset of the Bible
        #size is number of words(units) in each ngram
        #stopwords is list of strings(words) to ignore in forming ngrams
        '''
        tmpList = []
        if book != None:
            if chapter != None:
                if verse != None:
                    tmpList = self.get_verse(book,chapter,verse)
                    #TEST print("Verse:",len(tmpList))
                else:
                    tmpList = self.get_chapter(book,chapter)
                    #TEST print("Chapter:",len(tmpList))
            else:
                tmpList = self.get_book(book)
                #TEST print("Book:",len(tmpList))
        else:
            for item in self.verses:
                tmpList.append(item)
            #TEST print("Nothing:",len(tmpList))

        #Handle dicObjs.text -> List(words)
        gramList = []
        for tDict in tmpList:
            gramList.extend(re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', tDict["text"]).split()).lower()

        #Handle stopwords
        if stopwords != None:
            setStopwords = set(stopwords)
            filteredGrams = [x for x in gramList if x not in setStopwords]
            tDict = Counter(zip(*[filteredGrams[i:] for i in range(size)]))
        else:
            tDict = Counter(zip(*[gramList[i:] for i in range(size)]))
        return tDict    #End n_grams
    #End Bible()

#TEST Bib = read_bible()
#TEST print(Bib[0])
#TEST tmpBible = Bible()
#TEST print(tmpBible.get_book('genesis'))
#TEST print(tmpBible.get_chapter('genesis',0))
#TEST print(tmpBible.get_verse('genesis',0,0))
#TEST testy = tmpBible.n_grams(size=2)
#TEST print(testy)

