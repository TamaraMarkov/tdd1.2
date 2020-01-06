# getting input from the user and assigning it to user
def Bmi_Calc(height,weight):
    bmi = weight / (height ** 2)
    print("Your BMI is: {0} and you are: ".format(bmi), end='')
    return bmi

def Bmi_Status(bmi):
    if ( bmi < 16):
       print("severely underweight")
       return 'severely underweight'

    elif ( bmi >= 16 and bmi < 18.5):
       print("underweight")
       return 'underweight'

    elif ( bmi >= 18.5 and bmi < 25):
       print("Healthy")
       return 'Healthy'

    elif ( bmi >= 25 and bmi < 30):
       print("overweight")
       return 'overweight'

    elif ( bmi >=30):
       print("severely overweight")
       return 'severely overweight'

#if you perform unit testing do not run those:
# height = float(input("Enter height in meters: "))
# weight = float(input("Enter weight in kg: "))
# Bmi_Status(Bmi_Calc(height, weight))


