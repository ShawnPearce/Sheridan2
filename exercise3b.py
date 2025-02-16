
#initialize variables
counter=0
studentNumber="991819655"

#Start the loop
while True:
    num=(input("Enter a number(Type my student number to quit):  "))  #Take the user input
    
    if num==studentNumber: #Check if user input matches student number
        print("cutoff point")
        break #If the input matches the student number then exit the loop
    
    num=int(num) #converts the input to an integer
    if num % 11 == 0: #Checks to see if the number is a multiple of 11
        continue #Skips the rest of the loop if the condition is met(the number is a multiple of 11)
    
    print("You entered",num)
    counter+=1 #increment the counter by 1
print("The loop ran: ",counter,"times")