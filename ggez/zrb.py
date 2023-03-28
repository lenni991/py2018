score = input("Enter Score: ")
try:
    x=float(score)
    if x>1.0 or x<0:
        print ("an error")
    else:
        if x>=0.9:
            print("A")
        elif x>=0.8:
            print("B")
        elif x>=0.7:
            print("C")
        elif x>=0.6:
            print("F")
except:
    print("Error!please enter a number.")
    quit()
