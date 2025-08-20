a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Entert the third number : "))

if ((a > b) and (a > c) ):
    print("a is Maximum") 
    
    if(b > c):
        print("b is Maximum")
else:
    print("C is Maximum")