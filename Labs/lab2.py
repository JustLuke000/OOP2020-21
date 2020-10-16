#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        # use slice notation:
        print(message[0])
        print(message[-1])

        # escaping a character:
        print('\n')

        # find all a's in the input word and count how many there are:
        str(message)
        counter = message.count('a')
        print("There were %d a('s) in "% counter + message)

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and

            # count = 0
            # for i in message:
            #     if i == 'a':
            #         count = count + 1
            # print(count)

        # observe what happens, then use replace():
        print(message.replace('a','-'))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        list = message.split()
        print(list)

        # append a new element to the list and print:
        #Method 1
        list = list + 'Appendment'.split()
        print(list)

        #Method 2 - Taken from notes
        # my_list1 = [1,2,3]
        # my_list2 = ['a','b','c']
        # my_list1.append(my_list2)
        # print(my_list1)
        # my_list1.extend(my_list2)

        # remove from the list in 3 ways:
        # Method 1
        list.remove('Appendment')
        print(list)

        # Method 2
        list.pop(-1)
        print(list)

        # Method 3
        del list[-1]
        print(list)

        # check if the word cake is in your input list:
        for i in list:
             if i == 'cake':
                 print('"cake" is in your input list')


        # reverse the items in the list and print:
        list.reverse()
        print(list)

        # reverse the list with the slicing trick:
        print(list[::-1])

        # print the list 3 times by using multiplication:
        print(list*3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
