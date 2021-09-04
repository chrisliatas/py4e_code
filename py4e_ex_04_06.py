def computepay(h,r):
    if h <= 40 :
        return h * r
    else :
        return 1.5 * r * (h - 40) + 40 * r

hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")
try :
    h = float(hrs)
    r = float(rph)
except :
    print("Error, please enter numeric input")
    quit()

p = computepay(h,r)
print(p)
