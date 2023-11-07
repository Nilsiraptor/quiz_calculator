#!/usr/bin/env python3

import sys, random

# color defintion
NORMAL = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[96m"

# declare global variables
global num_questions
global correct_answers

# main checks for additional arguments
def main(args):
    if len(args) == 2:
        menu(int(args[1]))
    else:
        menu()

def menu(n=5):
    global num_questions, correct_answers

    num_questions = n
    correct_answers = 0
    curr_question = 0

    # game loop
    while True:
        sel = input(f"Select {BLUE}a{NORMAL}dd, {BLUE}m{NORMAL}ultiply or {BLUE}q{NORMAL}uit: ")
        if sel in ["a", "A", "add", "Add"]:
            sol, ques = add()
        elif sel in ["m", "M", "multiply", "Multiply"]:
            sol, ques = multi()
        elif sel in ["q", "Q", "quit", "Quit"]:
            exit()
        else:
            print("You have not selected one of the available options! Please try again.")
            continue

        curr_question += 1
        ans = input(ques)

        if int(ans) == sol:
            correct_answers += 1
            print(f"{GREEN}Correct{NORMAL}\n")
        else:
            print(f"{RED}Wrong{NORMAL} The correct answer is {sol}\n")

        if curr_question >= num_questions:
            break

    print(f"Congratulations, you answered {correct_answers} questions correctly!")

def add():
    a = random.randint(10, 200)
    b = random.randint(10, 200)
    return a+b, f"What is {a} + {b}?\n"

def multi():
    a = random.randint(2, 14)
    b = random.randint(2, 14)
    return a*b, f"What is {a} * {b}?\n"

if __name__ == "__main__":
    main(sys.argv)
