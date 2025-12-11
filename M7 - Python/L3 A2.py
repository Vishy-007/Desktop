h = float(input("Enter your height in cm: "))
w = float(input("Enter your height in kg: "))

bmi = w / (h/100)**2

print("Your BMI is: ", bmi)

if bmi <= 18.4:
    print("Your underweight")
elif bmi <= 24.96:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are overwight")
elif bmi <=34.9:
    print("You are severly overwight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are severly obese")