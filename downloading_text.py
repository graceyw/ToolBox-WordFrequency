'''Software Design Spring 2017
Word Frequency ToolBox
Gracey Wilson

This script grabs the text from ProjectGutenberg online
and saves a local copy to my computer.'''

import requests
BOW_full_text = requests.get('http://www.gutenberg.org/cache/epub/7477/pg7477.txt').text

import pickle
# Save data to a file
f = open('BOW_full_text.pickle', 'wb')
pickle.dump(BOW_full_text, f)
f.close()
