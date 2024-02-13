height=float(input("Enter your height in metres: "))
weight=float(input("Enter your weight in kilograms: "))

BMI=weight/(height**2)
if BMI <18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("Healthy weight")
elif BMI>=25.0 and BMI<=29.9:
    print("Overweight")
elif BMI>=30.0:
    print("Obesity")