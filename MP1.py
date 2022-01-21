import random 
import os
import string
import sys
import re

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
stopWordsList = set(stopWordsList)
delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    # TODO
    word_dict = {}
    content = sys.stdin.readlines()
    for idx in indexes:
        # clean and count word
        line = content[idx]
        add_word(word_dict, line)
    sorted_word_dict = sorted(word_dict.items(), key = lambda item: (-item[1], item[0]))
    for word, freq in sorted_word_dict[:20]:
        print(word)

def add_word(word_dict, line):
    line_split = re.split(r'[ \t,;.?!\-:@[\\\](){}_*/]', line)
    for word in line_split:
        word = word.strip().lower()
        if word not in stopWordsList and word:
            word_dict[word] = word_dict.get(word, 0) + 1
    
    
process(sys.argv[1])
