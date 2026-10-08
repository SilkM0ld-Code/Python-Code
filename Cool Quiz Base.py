import time
import random

name=""
usernumb = 0
usernumb = random.randint(1, 1000)
lives = 3
skips = 1
points = 0
answer = [ ]
def Boot():
    name=input("Welcome <User {0}>. Enter Name To Execute Quiz: ".format(usernumb))
    print("Type 'skip' to skip a question")
    print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
    print("Hello {0}, starting quiz...".format(name))
    Q1()

#Question 1
def Q1():
    global name, points, lives, skips
    print("")
    Answer_Question=input("Question 1: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question == "vento aureo" or Answer_Question == "golden wind":
        answer.append(Answer_Question)
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q2()
    #Skip Code
    elif Answer_Question == "skip":
        if skips > 0:
            answer.append(Answer_Question)
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q2()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q1()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q1()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 2
def Q2():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_2=input("Question 2: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_2 == "vento aureo" or Answer_Question_2 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q3()
    #Skip Code
    elif Answer_Question_2 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q2()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q2()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q2()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 3
def Q3():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_3=input("Question 3: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_3 == "vento aureo" or Answer_Question_3 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q4()
    #Skip Code
    elif Answer_Question_3 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q4()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q3()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q3()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 4
def Q4():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_4=input("Question 4: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_4 == "vento aureo" or Answer_Question_4 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q5()
    #Skip Code
    elif Answer_Question_4 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q5()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q4()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q4()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return


#Question 5
def Q5():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_5=input("Question 5: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_5 == "vento aureo" or Answer_Question_5 == "golden wind":
        points+=10
        skips+=1
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q6()
    #Skip Code
    elif Answer_Question_5 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q6()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q5()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q5()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 6
def Q6():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_6=input("Question 6: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_6 == "vento aureo" or Answer_Question_6 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q7()
    #Skip Code
    elif Answer_Question_6 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q7()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q6()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q6()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 7
def Q7():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_7=input("Question 7: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_7 == "vento aureo" or Answer_Question_7 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q8()
    #Skip Code
    elif Answer_Question_7 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q8()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q7()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q7()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 8
def Q8():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_8=input("Question 8: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_8 == "vento aureo" or Answer_Question_8 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q9()
    #Skip Code
    elif Answer_Question_8 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q9()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q8()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q8()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

def Q9():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_9=input("Question 8: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_8 == "vento aureo" or Answer_Question_8 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Q10()
    #Skip Code
    elif Answer_Question_8 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q10()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q9()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q9()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return

#Question 10
def Q10():
    global name, points, lives, skips, Answer_Question_1
    print("")
    Answer_Question_10=input("Question 10: what is the name of the 5th part of JoJo's Bizarre Adventure, {0}?".format(name)).lower()
    #Corrct Code
    if Answer_Question_10 == "vento aureo" or Answer_Question_10 == "golden wind":
        points+=10
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
        Qredo()
    #Skip Code
    elif Answer_Question_4 == "skip":
        if skips > 0:
            skips-=1
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Qredo()
        else:
            print("It seems you have no more skips. You are required to do this question.")
            Q10()
    #Wrong Code
    else:
        if lives > 1:
            lives-=1
            if points > 0:
                points-=5
            print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
            Q10()
        else:
            print("Go leave Now.")
            print("")
            print("Fine, here is your SCORE: {0}.".format(points))
            return


#Question Redo
def Qredo():
    if Answer_Question_1 == "skip" or Answer_Question_2 == "skip" or Answer_Question_3 == "skip" or Answer_Question_4 == "skip" or Answer_Question_5 == "skip" or Answer_Question_6 == "skip" or Answer_Question_7 == "skip" or Answer_Question_8 == "skip" or Answer_Question_9 == "skip" or Answer_Question_10 == "skip":
        print("it seems you have some questions skipped. Please Redo them.")
    if Answer_Question_1 == "skip":
        Q1()
    elif Answer_Question_2 == "skip":
        Q2()
    elif Answer_Question_3 == "skip":
        Q3()
    elif Answer_Question_4 == "skip":
        Q4()
    elif Answer_Question_5 == "skip":
        Q5()
    elif Answer_Question_6 == "skip":
        Q6()
    elif Answer_Question_7 == "skip":
        Q7()
    elif Answer_Question_8 == "skip":
        Q8()
    elif Answer_Question_9 == "skip":
        Q9()
    elif Answer_Question_10 == "skip":
        Q10()
    else:
        print("well done, you have:")
        print("Lives: {0}. Skips: {1}. Points: {2}.".format(lives, skips, points))
#Boot Up
Boot()

