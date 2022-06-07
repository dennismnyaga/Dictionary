import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Did you mean %s instead? If yes type Y or if no type N:  " % get_close_matches(w, data.keys())[0] )
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, please double check it"

    else:
        return "The word does not exist"

word = input("Enter a word:  ")

output = translate(word)

if type(output) == list:

    for items in output:
        print(items)
else:
    print(output)