# BMI CALCULATOR

age = int(input('Enter your age: '))
weight = float(input('Enter your weight (in kg): '))
height = float(input('Enter your height: ')) # Please add a decimal point (Ex. 1.80)

bmi = weight / height ** 2
if bmi < 18.5:
    print('Underweight.')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Normal Weight.')
elif bmi >= 25 and bmi <= 29.9:
    print('Overweight.')
elif bmi >= 30 and bmi <= 34.9:
    print('Obesity Class 1.')
elif bmi >=35 and bmi <= 39.9:
    print('Obesity Class 2.')
else:
    print('Obesity Class 3.')

print(round(bmi , 2))