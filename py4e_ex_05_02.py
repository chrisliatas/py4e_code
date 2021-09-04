largest = None
smallest = None
#count = 0
while True :
    userinpt = input('Enter a number: ')
    if userinpt == 'done' : break
    try :
        userinpt = int(userinpt)
    except :
        print('Invalid input')
        continue
#    if count == 0 :
#        largest = userinpt
#        smallest = userinpt
    if largest is None : largest = userinpt
    if smallest is None : smallest = userinpt
#    count += 1
    if largest < userinpt :
        largest = userinpt
    elif smallest > userinpt :
        smallest = userinpt

print('Maximum is', largest)
print('Minimum is', smallest)
#print('the counter is:', count)
