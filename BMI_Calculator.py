'''
The Body Mass Index or BMI is calculated from weight and height of a Person. 
In this project we are going to create a BMI calculator with Python.


What is Body Mass Index (BMI)?

BMI is a measure of relative weight based on an individual's mass and height. 
Today, Body Mass Index is commonly used to classify people as underweight, overweight, and even with obesity. 
Also, it is adopted by countries to promote healthy eating.


BMI Calculator with Python:

The body mass index is calculated by dividing an individual's weight in kilograms by their height in meters, 
then dividing the answer again by their height. 
Now let's see how to create a BMI calculator with Python:

'''

print(" ---- BMI CALCULATOR ---- ")

Height=float(input("Enter your height in centimeters: "))

Weight=float(input("Enter your Weight in Kg: "))

Height = Height/100                                  #Converting Height into meters

BMI=Weight/(Height*Height)                           #Formula for BMI
print("Your Body Mass Index is: ",BMI)

if(BMI>0):

	if(BMI<=16):
		print("You are severely underweight")

	elif(BMI<=18.5):
		print("You are underweight")

	elif(BMI<=25):
		print("You are Healthy")

	elif(BMI<=30):
		print("You are overweight")

	else:print("You are severely overweight")

else:
    print("Enter valid details")