import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input( "Did you mean %s instead? Y if yes or N if No: " %get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return get_close_matches(w,data.keys())[0]
        elif yn == 'N':
            return "The Word doesn't exist. Please double check it"
        else:
            return "Can not Understand your input. "

    else:
    	return "The word doesn't exist. Please double check it"

word = input("Enter your word: ")
output = translate(word)

if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)
