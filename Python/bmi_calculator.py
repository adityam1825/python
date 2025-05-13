Height = float(input("Enter your height in centimeters : "))
Weight = float(input("Enter your Weight in kg : "))
Height = Height/100
BMI = Weight/(Height*Height)
if(BMI>0):
    if(BMI<=16):
        print("your are highly underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30):
        print("you are over weight")
    else:
        print("you are highly overweight")
else:
    ("enter the valid details ")    
