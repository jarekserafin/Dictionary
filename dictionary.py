import json
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" % get_close_matches(word, data.keys())[0])
        decide = input("y/n")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "No such a word in this dictionary :("
    else:
        return "No such a word in this dictionary :("


data = json.load(open("data.json"))
word = input("Enter the word you want to search")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
