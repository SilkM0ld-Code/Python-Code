import time
item_storage = []

while True:
    time.sleep(0.5)
    print("")
    print("/¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\ ")
    print("|======[MENU]======|")
    time.sleep(0.1)
    print("|1 - [   Add item   ]            |")
    time.sleep(0.1)
    print("|2 - [Remove item]            |")
    time.sleep(0.1)
    print("|3 - [   View List   ]             |")
    time.sleep(0.1)
    print("|4 - [       Exit      ]             |")
    print("\_____________________________/")
    print("")
    time.sleep(0.5)
    print("/¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\ ")
    option= int(input("|Enter your choice: "))
    print("\______________________________/")
    print("")
    time.sleep(0.5)
    print("/¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\ ")
        
    if option == 1:
        add_item = input("|Enter the item to add: ")
        if add_item != "":
            item_storage.append(add_item)
            time.sleep(0.1)
            print("|'",add_item,"' has been added.")
            time.sleep(0.1)
            print("\______________________________/")
        else:
            time.sleep(0.1)
            print("|[   ] is empty")
            print("\______________________________/")
        
    elif option == 2:
        remove_item = input("|Item To Remove: ")
        if remove_item in item_storage:
            item_storage.remove(remove_item)
            print("\______________________________/")
        else:
            time.sleep(0.1)
            print("|No ITEM (",remove_item,") found in system")
            print("\______________________________/")

    elif option == 3:
        print("|[Current list storage]")
        item_number=0
        if not item_storage:
            time.sleep(0.1)
            print("| [The List is empty]")
            print("\______________________________/")
        for item in item_storage:
            time.sleep(0.1)
            item_number+=1
            print("|"+item_number,".",item)
            print("\______________________________/")

    elif option == 4:
        print("|Exiting...")
        time.sleep(0.1)
        print("|Good Bye")
        time.sleep(0.1)
        print("\______________________________/")
        break

    else:
        print("|Option Unavailable.")
        print("\______________________________/")
