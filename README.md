# Hangman-version-2# Hangman-Version-2
```
Language: Python
Libraries: Pandas, NumPy, Random
External Sources: Data set
```

### Description About the project:

Hangman is a simple word guess game in which the user attempts to build a missing word by guessing one letter at a time. After a certain number of incorrect guesses, the game ends and the player loses(Score and the correct word is shown).
If the player correctly identifies all the letters of the missing word, then points are given, and a new word is given if the user continues to play. 

### Implementation Method: 

Data set of the frequency of words were used in this project. Using Pandas irrelevant data was cleaned and stored in NumPy.Then this module was imported in the main program where the program for the word guess was written. 
In the main program, the word is converted to '*' and after each correct guess, those letters appear.

Yes, this is the second version of Hangman Project if you want to see the basic version the link is here https://github.com/abhi7585/Hangman-using-python or check my repositories. 


### The new changes are (Update 2.1) :
1) I have used a list which had limited word and decided by me thus used data set to enhance the variety of the words.
2) In the previous version, if the user enters an alphabet or character which the user has already entered before then it shows a message that the message has already used and the chances are deducted.
3) Also, there was no verification that the word which has been used will be used again or not.
4) Since the data set is used NumPy, pandas were implemented.

The data set was downloaded from here https://www.kaggle.com/rtatman/english-word-frequency

New Features :

Added a category option for the user's to select the type of word which users want to guess. Due to this, the user will have an idea that
what could the word be. 
The 3 categories are 1) English Vocabulary 2) Countries Name 3) Color Names

The two new data sets have been downloaded from here: 

Countries Names: https://www.kaggle.com/fernandol/countries-of-the-world/data

Colour Names: https://data.world/dilumr/color-names


### The new changes are (Update 2.2) :

Some additional tweaks have been made in this project. A new file named 'database.txt' has been added in the folder. It is a text file which is used as a database. Moreover, it will be used for Data Visualization.

The file will append new category, word, guessed (Yes / No) separated by ','. This will create a data set which can be used for visualization about the performance of the users. 

Some analysis work can be done and few questions can be answered. Introduction of File management was achieved via this method.
Every time someone runs the program the result will be appended in the file. Thus if you have used the program and would like to share the 'database.txt' updated file kindly connect with me. 

#### https://www.linkedin.com/in/abhi7585/
