# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: Luke O'Shea Scanlan
# date: 27-11-2020
# purpose: Educational Game for Secondary Schools

class Games:


    first_term = 0
    second_term = 1
    counter = 0
    calculation = 0

    try:
        term = int(input("Please Enter a Positive Whole Integer:"))
        # enter a character, see what happens
    except ValueError as ve:
        print("A value error has happened")
        #print(ve)
        term = 0  # keep any future usage of term from
        # crashing the program if we ran into this
    except Exception as e:
        print("I didn't realise this could happen")
        #print(e)
        term = 0

    print(term)

    if term <= 0:
        print("Please Enter a Positive Whole Integer:")
    elif term == 1: #The first two terms are a small exception and require special attention
        print(term," terms:")
        print(first_term)
    else:
    #Actual Fibonacci
        print("Your Input:",term)
        print("Terms Requested",term)
        while counter < term:
            print(first_term)
            calculation = first_term + second_term
            first_term = second_term
            second_term = calculation
            counter += 1

    correct = 0
    incorrect = 0

    while incorrect == 0:

        term = int(input("Guess the next integer in the series:"))

        if term != first_term:
            print("Incorrect")
            incorrect += 1


        else:
            print("Correct")
            correct += 1

        calculation = first_term + second_term
        first_term = second_term
        second_term = calculation
        counter += 1

    print("You got",correct,"correct!")


