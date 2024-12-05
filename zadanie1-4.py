# 4. Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).


n = input("A string:")

letters_occurence = dict()
for i in n:
    if i not in letters_occurence.keys():
        letters_occurence[i] = 1
    elif i in letters_occurence.keys():
        letters_occurence[i] = letters_occurence[i]+1

print(letters_occurence)