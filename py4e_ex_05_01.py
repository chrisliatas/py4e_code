count = 0
tot = 0
averg = 0
while True :
    userinpt = input('Enter a number: ')
    if userinpt == 'done' :
        break
    else :
        try :
            userinpt = float(userinpt)
        except :
            print('Invalid input')
            continue
        count = count + 1
        tot = tot + userinpt
#        averg = tot/count
#print(tot,count,averg)
print(tot,count,tot/count)
