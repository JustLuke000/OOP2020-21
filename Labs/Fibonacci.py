# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: Luke O'Shea Scanlan
# date: 27-11-2020
# purpose: Educational Game for Secondary Schools

class Fibonacci:

    first_term = 0
    second_term = 1

    try:
        term = int(input("Input please:"))
        # enter a character, see what happens
    except ValueError as ve:
        print("A value error has happened")
        print(ve)
        term = 0  # keep any future usage of term from
        # crashing the program if we ran into this
    except Exception as e:
        print("I didn't realise this could happen")
        print(e)
        term = 0

    print(term)
