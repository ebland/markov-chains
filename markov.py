"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path)
    file_name = file_name.read()

    return file_name

input_text = open_and_read_file("pledge.txt")

def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

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
    """

    text_string = text_string.rstrip()
    text_string = text_string.split()

    chains = {}

    for i in range(len(text_string) - 2):
        key = (text_string[i], text_string[i + 1])
        value = text_string[i + 2]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]

    #for i in chains.items():
        #print "%s: %s" % (i[0], i[1])

    return chains

    #print make_chains(input_text)


def make_text(chains):
    """Returns text from chains."""

    words = []

    dict_key = choice(chains.keys())
    words.append(dict_key[0])
    words.append(dict_key[1])

    while dict_key in chains:
        word_options = chains[dict_key]
        # word options -> ["could", "with", "in"]
        word = choice(word_options)
        words.append(word)
        dict_key = (words[-2], words[-1])

    #print words
    #print dict_key

    # your code goes here

    return " ".join(words)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# print chains

# Produce random text
random_text = make_text(chains)



print random_text
