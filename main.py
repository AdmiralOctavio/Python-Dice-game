import math as mth
import random as rnd
import time as t
import list
import sys

loginVerif = 0

# refreshes page


def refresh():
    print("\n"*50)

# startup animation


def startup():
    refresh()
    x = rnd.randint(2, 6)
    i = 0
    while i-1 < x:
        print("* "*15 + "\n" + "--== Octavio's Dice game ==--" + "\n" + "* " *
              15 + "\nLoading." + "."*i + "\n" + str(mth.floor(i/x*100)) + "% done")
        t.sleep(0.25)
        refresh()
        t.sleep(0.25)
        i += 1

# login


def login():
    global loginVerif
    print("* "*15 + "\n" + "--== Octavio's Dice game ==--" +
          "\n" + "* "*15 + "\n100% Done")
    x = 0
    while x < 1:
        if(input("\nDo you have an account?\n").lower()in list.yList):
            username = input("\nPlease enter your username:\n")
            password = input("\nPlease enter your password:\n")
            p = 0
            while p < 1:
                user = []
                passwo = []
                with open("usernames.txt", "r") as readuser:
                    line = readuser.readline()
                    while len(line) != 0:
                        user.append(line)
                        line = readuser.readline()
                with open("passwords.txt", "r") as readpass:
                    line = readpass.readline()
                    while len(line) != 0:
                        passwo.append(line)
                        line = readpass.readline()
                ui = str(username + "\n")
                pi = str(password + "\n")
                if(ui in user and pi in passwo and user.index(ui) == passwo.index(pi)):
                    print("\nLogin details verified.")
                    loginVerif += 1
                    p += 1
                    x += 1
                else:
                    print("Incorrect login details!\n")
                    print(user + passwo)
                    username = input("Please enter your username:\n")
                    password = input("\nPlease enter your password:\n")
        else:
            if(input("Would you like to register an account?").lower()in list.yList):
                with open("usernames.txt", "a") as userwrite:
                    userwrite.write(
                        "\n" + input("\nPlease input a username:\n") + "\n")
                with open("passwords.txt", "a") as passwrite:
                    passwrite.write(
                        "\n" + input("\nPlease input a password:\n") + "\n")


# old login system
'''
def login():
    global loginVerif
    print("* "*15 + "\n" + "--== Octavio's Dice game ==--" +
          "\n" + "* "*15 + "\n100% Done")
    username = input("Please enter your username:\n")
    p = 0
    while p < 1:
        if(username in list.usernames):
            password = input("\nPlease enter your password:\n")
            if(password in list.passwords and list.usernames.index(username) == list.passwords.index(password)):
                print("\nLogin details verified.")
                loginVerif += 1
                p += 1

        else:
            print("Incorrect login details!\n")
            username = input("Please enter your username:\n")
'''
# start gui


def start():
    user_start = input("\nPress S to start\n")
    validate = 0
    while validate == 0:
        if(user_start.lower() == "s"):
            validate = 1
        else:
            print("\n"*50 + "Invalid input, try again\n")
            user_start = input("\nPress S to start\n")

# main game


def game():
    refresh()
    global P1_name
    global P2_name
    global P1_score
    global P2_score
    P1_name = input("Enter player 1's name:\n")
    P2_name = input("Enter player 2's name:\n")
    P1_score = 0
    P2_score = 0
    gl = 0
    for gl in range(5):
        refresh()
        print("---===<{{ R O U N D  " + str(gl+1) + " }}>===---")
        i = 0
        while i < 1:
            if(input("\nWould " + P1_name + " like to roll?\n").lower() in list.yList):
                rand11 = rnd.randint(1, 6)
                rand12 = rnd.randint(1, 6)
                P1_score += rand11
                P1_score += rand12
                t.sleep(0.25)
                print(str(P1_name) + " scored a " +
                      str(rand11) + " and a " + str(rand12) + "!")
                t.sleep(0.25)
                print(str("\n" + P1_name) + "'s new score is " + str(P1_score))
                i = 1
            else:
                print("\nHint: You need to say yes\n")
        x = 0
        while x < 1:
            if(input("\nWould " + P2_name + " like to roll?\n").lower() in list.yList):
                rand21 = rnd.randint(1, 6)
                rand22 = rnd.randint(1, 6)
                P2_score += rand21
                P2_score += rand22
                t.sleep(0.25)
                print("\n" + str(P2_name) + " scored a " +
                      str(rand21) + " and a " + str(rand22) + "!")
                t.sleep(0.25)
                print(str(P2_name) + "'s new score is " + str(P2_score))
                x = 1
            else:
                print("\nHint: You need to say yes\n")
            t.sleep(2)


# leaderboard stuff
scoreList = []


def score():
    with open("scoreboard.txt", "a")as writefile:
        if(P1_score > P2_score):
            writefile.write("\n" + str(P1_score) + " - " + str(P1_name))
        elif(P2_score > P1_score):
            writefile.write("\n" + str(P2_score) + " - " + str(P2_name))
    with open("scoreboard.txt", "r") as myfile:
        line = myfile.readline()
        while len(line) != 0:
            scoreList.append(line)
            line = myfile.readline()
    scoreList.sort(reverse=True)


def printscore():
    if(input("\n\nWould you like to see the scoreboard?\n").lower() in list.yList):
        score()
        i = 0
        print("\n")
        print("-==L E A D E R B O A R D==-\n")
        for i in range(len(scoreList)):
            t.sleep(0.4)
            print(scoreList[i].strip("\n"))

# main


def main():
    startup()
    login()
    if(loginVerif == 1):
        start()
        game()
        printscore()


main()