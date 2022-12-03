x=input('press y to run or n to stop:')
while x=='y':
    num=int(input('enter number of seconds:'))
    a=num//60
    b=num%60
    print(a,'minutes',b,'seconds')
    x=input('press y to run or n to stop:')
    
