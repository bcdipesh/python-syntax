def print_upper_words(words):
    """
        Prints each word passed to words list in uppercase.
    """

    # loop over each word from words list
    for word in words:
        # convert word to uppercase and print
        print(word.upper())


def print_upper_words_that_starts_with_e(words):
    """
        Prints each word passed to words list in uppercase that starts with e or E.
    """

    # loop over each word from words list
    for word in words:
        # check if the word stars with e or E
        if word.startswith('e') or word.startswith('E'):
            # if word passes the condition convert the word to uppercase and print
            print(word.upper())


def print_upper_words_that_starts_with(words, must_start_with):
    """
        Prints each word passed to words list in uppercase that starts with the words passed inside must_start_with.

        for example: 
        words = ["hello", "hey", "goodbye", "yo", "yes"]
        must_start_with=["h", "y"]

        this should print "HELLO", "HEY", "YO", and "YES"
    """

    # loop over each word in words list
    for word in words:
        # check if the current word starts with any of the letter passes inside must_start_with
        if word[0].lower() in must_start_with or word[0].upper() in must_start_with:
            # if the current word passes the condition, convert it to uppercase and print
            print(word.upper())
