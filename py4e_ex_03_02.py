print("PY4E_EX_03_01")
hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")
try :
    h = float(hrs)
    r = float(rph)
except :
    print("Error, please enter numeric input")
    quit()
    
if h <= 40 :
    pay = h * r
else :
    pay = 1.5 * r * (h - 40) + 40 * r
print(pay)
