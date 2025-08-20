a=float(input("Enter your Percentage : "))

if  a > 85 :
    print("Your grade is: A+ ")
elif 85 >= a > 65  :
        print("Your grade is: A")
elif 65 >= a >45 : 
            print("Your grade is: B")
elif 45 >= a >25 :
            print("Your grade is:  C")
elif a <=25  :
            print("your grade is:  D")
else:
    print("Enter valid percentage.")