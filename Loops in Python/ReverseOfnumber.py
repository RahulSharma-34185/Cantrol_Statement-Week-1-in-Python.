#Wap to print reverse of a number.

n=int(input("Enter the number : "))
N=0

while n > 0 :

   digit=n%10
   N=N*10+digit
   N = n//10

print("Reverse of a number :", N);
