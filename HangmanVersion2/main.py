import sys
from data import data  # importing the data.py to use get_word() function

file = open("database.txt", 'a')


def update(newWord):
    temp = []
    for i in range(len(newWord)):
        if str(newWord[i]).isalpha() == False:
            t = newWord[i]  # character is other then alphabets Eg. &, ' '
            temp.append(t)
        else:
            temp.append('*')
    return ''.join(temp)


def check_character(character, word, newWord):
    word = list(word)
    temp = list(newWord)
    flag = False
    for i in range(len(word)):
        if word[i] == character:
            temp[i] = character
            flag = True
        elif temp[i] == word[i]:
            temp[i] = word[i]
        else:
            temp[i] = '*'
    newWord = ''.join(temp)
    return [newWord, flag]


def play(name, category):
    chances = 5
    points = 0
    loop = True
    print("Welcome {} you have {} chances and your points are {}. ".format(
        name, chances, points))

    while loop:
        characterList = []
        chances = 5
        word = data.get_word(category)
        newWord = update(word)
        print("Word is : {}".format(newWord))
        while chances != 0:
            if '*' in newWord:
                character = input("Enter an alphabet: ").lower()
                while character in characterList and chances != 1:
                    print("You have already guessed this alphabet. Remaining chances are: {}".format(
                        chances-1))
                    character = input("Enter an alphabet again: ").lower()
                    chances = chances - 1
                    if chances != 1:
                        print("Guess was wrong. No remaining chances .")
                        print("Word was : {}".format(word))
                        print("Your score was: {}".format(points))
                        file.write(f"{category},{word},no \n")
                        file.close()
                        exit(0)
                else:
                    characterList.append(character)
                temp = check_character(character, word, newWord)
                newWord, flag = temp[0], temp[1]
                if flag == False and chances == 1:
                    print("Guess was wrong. No remaining chances .")
                    print("Word was : {}".format(word))
                    print("Your score was: {}".format(points))
                    file.write(f"{category},{word},no \n")
                    file.close()
                    exit(0)
                elif flag == False and chances > 0:
                    chances = chances - 1
                    print("Guess was wrong. Chances remaining are {}".format(chances))
                else:
                    print("Word is : {}".format(newWord))
            else:
                print("Hurray!!! you have guessed the word correctly.")
                points = points + 1
                print("Your points: {}".format(points))
                file.write(f"{category},{word},yes \n")
                answer = input("Do you wish to continue ? (Y/N)").upper()
                if answer == "N":
                    file.close()
                    loop = False
                break


print("Welcome to the Hangman Game!!!! ")
name = input("Enter your Name: ")
print("Select the types of words you want to guess.")
print("1) English Vocabulary")
print("2) Countries Names ")
print("3) Color Names ")
category = int(input("Enter (1/2/3) : "))
if category == 1 or category == 2 or category == 3:
    play(name, category)
else:
    print("Invalid input. Exiting..")
    file.close()
    exit(0)
