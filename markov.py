"""Generate Markov text from text files."""

import random 
import sys


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name1 = open(file_path1) # output = file object
    file_name2 = open(file_path2)
    file1_as_string = file_name1.read() # output = string 
    file2_as_string = file_name2.read()
    file_name1.close()
    file_name2.close()

    return file1_as_string + file2_as_string


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    word_list = text_string.split()

    for i in range(len(word_list)-n):
        # slice from i to i + 2 ==> list of 2 words. make that into a tuple
        key = tuple(word_list[i:i+n])
        # check if item in dict if key not assign an (empty list + [word_list[i+2]]) to a key
        chains[key] = chains.get(key, []) + [word_list[i+n]]

    for key, value in chains.items():
        print(f'{key}: {value}')

    return chains


def find_initial_key(chains):
    '''Returns a string that is title cased'''
    
    title_case_word = '' 

    for key in list(chains.keys()):
        if key[0] == key[0].title():
            title_case_word = key[0]
            break


    # print('LOOK HERE:', title_case_word)


    # use the title case word to search dict for any key whose 1st item is that word
    initial_key = tuple()

    for key in list(chains.keys()):
        if key[0] == title_case_word:
            initial_key = key

    # print('LOOK HERE:',initial_key)

    return initial_key

# find_initial_key(make_chains(open_and_read_file("green-eggs.txt"),2))

def make_text(chains, n):
    """Return text from chains."""

    words = []

    # initial_key = random.choice(list(chains.keys())) #random.choice iterates over a list of 2 item tuples
    initial_key = find_initial_key(chains)
    words.extend(list(initial_key))
    end_here = tuple(words[-n:])[-1][-1] # last character of last item in key
    print('LOOK:',end_here)

    #while loop - until no more key left in dict
    while tuple(words[-n:]) in chains and end_here.isalpha():
        # new_key = last n words from the populated words list
        new_key = tuple(words[-n:]) #output is a tuple
        # pick a random word using generated key in chains dict to access list of values
        # if key exists in dict, pick a random value of that key, and assign it to random_word
        random_word = random.choice(chains[new_key])
            # add random_word to words list 
        words.append(random_word)  
       

    return " ".join(words)


input_path_1 = sys.argv[1]
input_path_2 = sys.argv[2]


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path_1, input_path_2)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains, 2)

print(random_text)

# make_chains(open_and_read_file('gettysburg.txt'))