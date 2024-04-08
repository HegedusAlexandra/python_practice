height = float(input('How high are you ?'))
weight = int(input('How heavy are you ?'))
BMI = round(weight / height ** 2,2)
if BMI > 35:
    print(f'your BMI is {BMI}, you are clinically obese!')
elif BMI > 30 :
    print(f'your BMI is {BMI}, you are overweight!')
elif BMI > 25:
    print(f'your BMI is {BMI}, you are slightly overweight!')
elif BMI > 18.5:
    print(f'your BMI is {BMI}, you are normal!')
else:
    print(f'your BMI is {BMI}, you are underweight')