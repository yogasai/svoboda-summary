# This program calculates some quantitative information about
# a sample diary (diary 47) and it's summary

import nltk
from nltk.stem import WordNetLemmatizer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# number of words in diary
# 1. total words
#diary = open('d47.rtf','rU')
diary = open('d47.txt','rU')
#tokenizes text
rawDiary = diary.read()
rawDiary= rawDiary.encode('ascii', errors='ignore')
dTokens = nltk.word_tokenize(rawDiary)
##creates text from tokens
text = nltk.Text(dTokens)

length = len(text)
print 'total number of words in diary 47: ', length
# 2. unique words
unique = len(set(text))
print 'total number of unique words in diary 47: ', unique


# number of words in summary
# 1. total words
summary = open('d47sum.txt','rU')
rawSum = summary.read()
rawSum = rawSum.encode('ascii', errors='ignore')
sTokens = nltk.word_tokenize(rawSum)
summary = nltk.Text(sTokens)
sumLength = len(summary)
print 'total number of words in d47 summary: ', sumLength
# 2. unique words
sumUnique = len(set(summary))
print 'total number of unique words in d47 summary: ', sumUnique

#words in common
common = list(set(text) & set(summary))
# print('PRINTS COMMON', common)
commonLength = len(common)
print '# words in common for diary and summary: ', commonLength

# AFTER LEMMATIZING
#diary
lemmatizer = WordNetLemmatizer()
diaryLem = [lemmatizer.lemmatize(t) for t in dTokens]
#print('PRINTS DIARY LEM',diaryLem)
#1. total number of words - diary
diaryLemLength = len(diaryLem)
print 'total # of lemmatized words in d47: ', diaryLemLength
# print(diaryLem)
# 2. unique words  - diary
dLemUniqueLen = len(set(diaryLem))
print 'total # of unique lemmaztized words in d47: ', dLemUniqueLen

#summary
summaryLem = [lemmatizer.lemmatize(t) for t in sTokens]
#print(summaryLem)
#1. total number of words -- summary
summaryLemLength = len(summaryLem)
print 'total # of lemmatized words in d47 summary: ', summaryLemLength
#2. unique words
sLemUniqueLen = len(set(summaryLem))
print 'total # of unique lemmatized words in d47 summary', sLemUniqueLen

#words in common
allLem = list(set(diaryLem) & set(summaryLem))
#print(common)
commonLemLen = len(allLem)
print 'total # of lemmatized words in common: ', commonLemLen
