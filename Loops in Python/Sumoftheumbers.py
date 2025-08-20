#Read N, print sum of digit in N.

n = int(input("Enter the number : "))
sum = 0

while (n>0):

    digit= n%10
    n=n//10
    sum+=digit

print("sum of digit", sum);
