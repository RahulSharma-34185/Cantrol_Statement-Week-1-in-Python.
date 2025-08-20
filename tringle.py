a = int(input("Enter first angle of triangle :"))
b = int(input("Enter second angle of triangle :"))
c = int(input("Enter third angle of triangle :"))

tm =a+b+c 

if(tm <= 180 ):
    print("Entered angles are valid.")
else:
    print("Entered angles are not valid.")