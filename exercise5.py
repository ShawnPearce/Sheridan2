rows=(int)(input("Enter the number of rows:  "))

for i in range(1,rows+1):
    if i % 2==1:
        print("+"*(2*i-1))
    else:
        print("-"*(2*i-1))