
# This program extracts the unique named entities from the 
# first 20 sentences of the sample diary.

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# read and store diary content as nltk text
summary = open('d47sum.txt','r')
rawSum = summary.read()
rawSum = rawSum.encode('ascii', errors='ignore')
sentences = nltk.sent_tokenize(rawSum)

# tokenize and tag content
tokens = [nltk.word_tokenize(sent) for sent in sentences] 
tagged = [nltk.pos_tag(sent) for sent in tokens] 
chunked = nltk.ne_chunk_sents(tagged, binary=True)

# extract named entities from content
	# returns an nltk.tree.Tree object which needs to be traversed 
	# the Tree is a list, chunks are subtrees, and non chunked words are regular strings
def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE' or t.label() == 'NP':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked:
    # print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))


# print unique entity names
unique = set(entity_names)
print(unique)

# output:
#set(['Deir', 'Basra', 'Mejidieh Class', 'Thani', 'Paris', 'Mejidieh', 'Suez Canal', 
#'Turkish Liras', 'Rezooki', 'Solon Calothi', 'European', 'Sayegh', 'Yousif', 'Hit', 
#'Stephen Lynch', 'Sippar', 'Yousif Marine', 'Lebany', 'Antone Marine', 'French', 'Baghdad', 
#'Construction', 'Yousif Sayegh', 'Customs House', 'North Africa', 'Shaban', 'Nasryeh', 'Nubar Pasha', 
#'Latin Church', 'Damascus Post', 'Patriarch', 'Snow', 'Ezra Daniel', 'Bad', 'Mons', 
#'Mushir Recep Pasha', 'Mezel', 'Yemen', 'Wind', 'Colonel Lock', 'Tigris', 'Yousif Korkis', 
#'Cairo', 'Consul', 'Khalifa', 'India', 'Milan', 'London', 'Fathallah', 'Ressafah', 'Austrian', 
#'Bombay', 'Arabs', 'Kut Jaffer Beg', 'Amara Mostapha', 'Kathem', 'Basra Quarantine', 'Gulf', 'Army', 
#'West', 'Eliza', 'Serkis Pasha', 'Tripoli', 'Hamidian', 'Mr. Mashkow', 'Joseph', 'Tigris River', 
#'Mr. Bhm', 'Diyarbakir', 'Bughela', 'Anton Marine', 'Commander', 'Vienna', 'Svoboda', 'Magasis', '
#New Year', 'Coot', 'Alexandretta', 'Rumelian', 'Mr. Bottomley', 'Paris Exhibition', 'Francis', 'Khazal', 
#'French Ambassador Mons', 'Karachi', 'Moossa Kadem Pasha', 'Monseigneur Altmayer', 'Karbala', 
#'Captain Cowley', 'Paris Exhibition Lottery', 'Sheikh Mezel', 'Isak Lurion', 'English', 
#'Nazaret Kasparyan', 'Mushir', 'Georgis Antone', 'Rezooki Korkis', 'Hatfield', 'Sheikh Seyhood', 
#'Agha Muhammad', 'Turkish Lira', 'Jawi', 'Mosul', 'Sheikhs', 'Hatfiled', 'Ottoman', 'Arabic', 'Syrian', 
#'Father Superior', 'Baghdad Vali', 'Lyon', 'Ibrahim', 'Istanbul', 'Turkish', 'Kuwait', 'Recep Pasha', 
#'Jassim', 'New School', 'Aleppo', 'Armenian Massacre', 'Yousif Korkis Tessy', 'Cambon', 'Turin', 
#'Europe', 'Basreh', 'Vali', 'Turks', 'Palmes', 'Mushir Rejeb Pasha', 'Mahomed', 'Saglawyeh', 'Rejeb', 
#'Chaldean Patriarch', 'Lynch', 'Archbishop', 'Russian', 'Rumelian Railway Lotteries', 'Iraq', 'Castor Oil', 
#'Amara', 'Mahomerah', 'Khalifah', 'Arab', 'Yousif Asfar', 'Sultan', 'Tell Abu Habbah', 'Mr. Hatfield', 
#'Armenian', 'Mesopotamian', 'Sheikh', 'Hassan', 'Mahomedans', 'Arif Pasha', 'Wazna', 'Noonoo Denoos', 
#'Kweit Moobarak', 'Mr. Julietti', 'German', 'Motserrif', 'Lynches', 'Euphrates', 'Ronet', 'Gejou', 
#'Church', 'Seyhood', 'Alexander', 'Rumelian Railway', 'Qatar', 'Mossul', 'Irak Arabia', 'Edward', 
#'Francs', 'Keleks', 'Sultan Abdulhamid II', 'Aleed Ishoh', 'Christian', 'Egyptian', 'Kit', 'Blosse Lynch', 
#'Islamic', 'Beni Laam', 'Constantinople', 'Sherif Beg', 'Army Corps', 'Marie Joseph', 'Kaiser Wilhelm', 
#'Eliahoo Denoos', 'Baghdadi Christian', 'Porte', 'Antone', 'Olloi', 'Ottoman Empire', 'British', 'Ibrahim Gejou', 
#'Persian Gulf', 'Philip Chiha', 'Grain', 'Residency', 'Mostapha Pasha Han', 'Bycicle', 'Johny', 'Egypt', 'Lock', 
#'Shia', 'Ramadan', 'Red Sea', 'Mushire', 'Anis Pasha', 'Native'])

# get first 20 sentences
#selection = sentences[:20]
#print(selection)


