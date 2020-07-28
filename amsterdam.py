'''Given a string, return the number of times "am" 
appears in the string BUT ONLY WHEN "am" 
is not followed or preceded by any other LETTERS'''

def name(input):
    number = 0
    for word in input.split(" "):
        if word.lower() == "am":
            number = number + 1
    return number