#!/usr/bin/env python3

import sys, random

# color defintion
NORMAL = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[96m"

# main checks for additional arguments
def main(args):
    try:
        menu(int(args[1]))
    except (ValueError, IndexError):
        menu()

def menu(n=5):
    correct_answers = 0

    username = input("Please enter your name to start: ")

    while True:
        sel = input(f"Select {BLUE}a{NORMAL}dd, {BLUE}m{NORMAL}ultiply or {BLUE}q{NORMAL}uit: ")
        if sel in ["a", "A", "add", "Add"]:
            func = add
            sel = "a"
            break
        elif sel in ["m", "M", "multiply", "Multiply"]:
            func = multi
            sel = "m"
            break
        elif sel in ["q", "Q", "quit", "Quit"]:
            exit()
        else:
            print("You have not selected one of the available options! Please try again.")


    for i in range(n):
        sol, ques = func()
        ans = input(ques)

        try:
            ans = int(ans)
        except ValueError:
            print(f"{RED}Wrong{NORMAL} The correct answer is {sol}\n")
        else:
            if ans == sol:
                correct_answers += 1
                print(f"{GREEN}Correct{NORMAL}\n")
            else:
                print(f"{RED}Wrong{NORMAL} - The correct answer is {sol}\n")

    print(f"Congratulations, you answered {correct_answers} questions correctly!")

    writeResult(username, sel, correct_answers/n*100)

def writeResult(user, task, perc):
    with open("result.txt", "a") as file:
        file.write(f"{user}\t{task}\t{perc}\n")

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
