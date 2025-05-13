
Name = str(input("Enter your name :  "))
print("")
print(f"Hi {Name}!!! this will help you to calculate ur BMI")
print("")
Height = float(input("Enter your height in centimeters : "))
Weight = float(input("Enter your Weight in kg : "))
Height = Height/100
BMI = Weight/(Height*Height)
if(BMI>0):
    if(BMI<=16):
        print(f"{Name} your are highly underweight")
    elif(BMI<=18.5):
        print(f"{Name} you are underweight")
    elif(BMI<=25):
        print(f"{Name} you are healthy")
    elif(BMI<=30):
        print(f"{Name} you are over weight")
    else:
        print(f"{Name} you are highly overweight")
else:
    ("enter the valid details ")    
