# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was:", self.user_input)

        # first scramble is just one word
        i = 0
        for i in range(len(self.user_input)):
            print(self.user_input[i])
            i = i + 1
            if i > 1 and self.user_input[i] != ' ':
                print(self.user_input[i])
                print(self.user_input[(i+1)])
                i = i + 1

        print(self.user_input)
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two

        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence

        # do just words first, then you can move on to work on

        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

