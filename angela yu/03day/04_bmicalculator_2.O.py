height= float(input("Enter your height in m here : "))
weight= float(input("Enter your weight in kg  here : "))
bmi = (weight/(height*height))
if bmi <18.5:
    print(f"Your BMI is {bmi},you are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi},you are normal weight")
elif bmi<30:
    print(f"Your BMI is {bmi},you are overweight")
elif bmi<35:
    print(f"Your BMI is {bmi},you are obse")
else :
    print(f"Your BMI is {bmi},you are clinically obse")

