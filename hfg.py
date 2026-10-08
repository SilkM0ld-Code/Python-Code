name=""
def greet_user():
    global name
    if name == "":
        name=input("Enter Name Here: ")
        if name == "The King":
            print("poser")
            Opt()
        else:
            print("Hello: ",name)
            print("My Name is ₮ⱧɆ ₭ł₦₲")
            Opt()
    else:
        print("Your Name Is:",name)
        change_name=input("Would You Like To Change Your Name: ")
        if change_name == "Y":
            print("Changing Name....")
            name=""
            greet_user()
        else:
            print("Canceled")
            Opt()

def Mult():
    global name
    num_a=input(name,"Input Number_A: ")
    num_b=input(name,"Input Number_B: ")
    print("Prosesing")
    num_ans=num_a*num_b
    print("Well Done:",name," you got:",num_ans)
    Opt()

def Aver():
    global name
    av_a=input(name,"Input Number_A: ")
    av_b=input(name,"Input Number_B: ")
    av_c=input(name,"Input Number_C: ")
    print("Prosesing")
    av_tot=av_a*av_b*av_c
    av_ans=av_tot/3
    print("Well Done:",name," you got:",ans)
    Opt()

def Opt():
    print("your options are: Name, Multiply, and Average")
    option=input("select you option: ")
    if option == "Name":
        greet_user()
    elif option == "Average":
        Aver()
    
    else:
        Opt()
Opt()
