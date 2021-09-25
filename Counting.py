intro = input('Enter About your Self : ')
characterCount = 0
wordCount = 1

for i in intro:
    characterCount = characterCount + 1
    if(i == ' '):
        wordCount = wordCount + 1
print("words Count " + str( wordCount)   )
print(characterCount)


# using while loops
Count=5
while (Count>=0):
    print(Count)
    Count = Count -1
