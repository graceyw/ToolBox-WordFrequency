"""
Software Design Spring 2017
Word Frequency ToolBox
Gracey Wilson

Analyzes the word frequencies in a book downloaded from Project Gutenberg.
"""

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name,'r')
    lines = f.readlines()

    curr_line = 0
    while lines[curr_line].find('THE BRIDE OF THE MAN-HORSE') == -1:
        curr_line += 1                       # strips intro text
    lines = lines[curr_line+1:]
    l = len(lines) - 1
    while lines[l].find('End of the Project Gutenberg EBook of The Book of Wonder, by') == -1:
        l -= 1                               # strips outro text
    lines = lines[:l]

    lines = [''.join(c for c in s if c not in string.punctuation) for s in lines]   # strips punctuation from each string in list of lines
    list_all_lines = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()          # strips "white space" (i.e. the \n that indicates new lines)
        lines[i] = lines[i].lower()          # makes all characters lowercase
        list_one_line = list(lines[i].split())  # Make the words in the textfile a list of strings
        list_all_lines += list_one_line
    list_all_lines = [s for s in list_all_lines if s != '']    # removes empty strings (i.e. those that just had \n in them, meaning they were indicating a new line)
    return list_all_lines


def get_top_n_words(word_list,n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    '''ONCE YOU MAKE A DICTIONARY WHERE THE KEYS ARE WORDS
    AND THE VALUES ARE # OF OCCURENCES, YOU CAN RUN:'''
    dict_words_occurences = {}
    for item in word_list:
        if item not in dict_words_occurences:
            dict_words_occurences[item] = 0         # if it's the first time it has come up, make a new key
        dict_words_occurences[item] += 1            # then start counting the # of times it is mentioned
    ordered_by_frequency = sorted(dict_words_occurences, key=dict_words_occurences.get, reverse=True)
    return ordered_by_frequency[0:n]


if __name__ == "__main__":
    list_all_lines = get_word_list('BOW_text.txt')
    print("The most common words in the Book of Wonders text are:")
    print(get_top_n_words(list_all_lines,10))
