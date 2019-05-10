import os
import re
import json


def ingest_data():
    files = []
    sentences = []
    for index, filename in enumerate(os.listdir("data")):
        with open("data/" + filename, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
            text = re.sub("\n|''", " ", text)

            # splits sentences where full stop and space follows lower case letter
            sentence_split = (re.split("(?<=[a-z])\.\s+", text))
            for sentence in sentence_split:
                sentences.append(sentence)

            # use regex to remove all formatting except for letters, numbers, spaces, apostrophes and inter-word dashes
            text = re.sub("\s\-\s|\-\-|", "", text)
            text = re.sub("[^0-9a-zA-Z'\-\ ]+", "", text)

            text = text.lower()

            files.append(text)
    return files, sentences


def create_hashtag_list(files, sentences, min_letter_count=0):
    word_count = {}
    for index, file in enumerate(files):
        word_list = file.split(" ")
        for word in word_list:
            if len(word) > min_letter_count:
                if word_count.get(word):
                    word_count[word]["count"] += 1
                    word_count[word]["file"].append(index+1) if index+1 not in word_count[word]["file"] else None
                else:
                    sentence_matches = [sentence for sentence in sentences if word in sentence.lower()]
                    word_count[word] = {"count": 1, "file": [index + 1], "sentences": sentence_matches}

    word_count_list = [{word: {"count": info["count"], "file": info["file"], "sentences": info["sentences"]}}
                       for word, info in word_count.items()]

    sorted_word_count_list = sorted(word_count_list, key=lambda x: list(x.values())[0]["count"], reverse=True)

    return sorted_word_count_list


files, sentences = ingest_data()
hashtag_list = create_hashtag_list(files, sentences, 2)

with open("hashtag_list.json", "w") as f:
    for hashtag_dict in hashtag_list:
        json.dump(hashtag_dict, f)
        f.write("\n")
