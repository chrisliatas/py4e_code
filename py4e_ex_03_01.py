print("PY4E_EX_03_01")
hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
r = float(rph)
if h <= 40 :
    pay = h * r
else :
    pay = 1.5 * r * (h - 40) + 40 * r
print(pay)
