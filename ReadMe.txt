Hashtag Generator

Surprisingly interesting tricky problem

code stored in hashtag_generator.py

    ingest_data()

reads the txt files stored in the data folder and using a number of regex funtions to create 2 outputs:
1. files -> a list, each item is a string containing only the words from the txt files
2. sentences -> a list, each item is a string containing a sentence from all the txt files

    create_hashtag_list()

the "files" and "sentence" objects from the above function are passed to this one, as well as an optional variable
min_letter_count which sets the length of words that will be considered when creating the hashtag list

the files list has its strings split into individual words and each one is added as a dictionary key to the word_count dictionary
or if there is already that word added, then the value of that nested dictionary key is increased by 1

then the sentences dictionary is checked iteratively for the word in question and if any are found they are added to the
nested dictionary

then the dictionary is converted to a list of dictionaries, which is then sorted by the count variable inside the nested
dictionary and returned to the user

The program then saves the outputted list to the "hashtag_list.json" file