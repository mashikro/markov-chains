"""Generate Markov text from text files."""

import random 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path) # output = file object
    file_as_string = file_name.read() # output = string 

    return file_as_string


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


def make_text(chains, n):
    """Return text from chains."""

    words = []

    initial_key = random.choice(list(chains.keys())) #random.choice iterates over a list of 2 item tuples
    words.extend(list(initial_key))

    #while loop - until no more key left in dict
    while tuple(words[-n:]) in chains:
        # new_key = last n words from the populated words list
        new_key = tuple(words[-n:]) #output is a tuple
        # pick a random word using generated key in chains dict to access list of values
        # if key exists in dict, pick a random value of that key, and assign it to random_word
        random_word = random.choice(chains[new_key])
            # add random_word to words list 
        words.append(random_word)  
       

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains, 4)

print(random_text)

# make_chains(open_and_read_file('gettysburg.txt'))