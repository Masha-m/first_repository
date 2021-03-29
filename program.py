my_list = ["5", "65", "90", "127"]

n = 0 
while True:
    print ("Enter X to exit")
    a = input ("Gues a number from the list: ") 
    if a in my_list:
        print ("you are correct!")
    if a == "X":
        break
    else:
        print ("try again!")