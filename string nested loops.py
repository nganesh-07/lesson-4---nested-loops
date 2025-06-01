word = input("Enter a word here:")
character = input("Enter a character here:")

i = 0
count = 0

while i < len(word):
    if word[i] == character:
        count = count + 1
    i = i + 1

print("The character", character, "has occurred", count, "number of times in", word)