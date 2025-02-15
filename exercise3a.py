counter=0

while True:
    num=(int)(input("Enter a number(If the number is negative it will quit the program):  "))
    
    if num < 0:
        break
    print("You entered",num)
    counter+=1
print("The loop ran: ",counter,"times")