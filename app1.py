import json

dictionary = json.load((open("data.json")))

# input: word
# return: the definition for that word. 
# Incorporate json file and print out the output
def getDefinition(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return f"Invalid Input: The word \'{word}\' does not exist in the dictionary."

word = input("Enter word: ")

print(getDefinition(word))


