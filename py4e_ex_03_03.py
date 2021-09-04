score = input("Enter Score: ")
try :
    scr = float(score)
except :
    print("Error, please enter numeric values")
    quit()
if 0.0 <= scr <= 1.0 :
    if scr >= 0.9 :
        print("A")
    elif scr >= 0.8 :
        print("B")
    elif scr >= 0.7 :
        print("C")
    elif scr >= 0.6 :
        print("D")
    else :
        print("F")
else :
    print("Error, score value is out of range 0.0 and 1.0")
    quit()
