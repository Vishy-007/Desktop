#Nested if-else
n = int(input("Enter a no. : "))

if n < 50:
    print("The number is less than 50")
    if n%2==0:
        print("It's an even number too")
    else:
        print("It's an odd number as well")
else:
    print("Your number is over 50")