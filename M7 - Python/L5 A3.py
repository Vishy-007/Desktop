def add(x, y):
    return (x + y)

def subtract(x, y): 
    return (x - y)

def multiply(x, y):
    return (x * y)

def division(x, y):
    return (x / y)

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

print("Sum: ", add(n1, n2))
print("Difference", subtract(n1, n2))
print("Product: ", multiply(n1, n2))
print("Quotient: ", division(n1, n2))
