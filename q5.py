num1= (input("Enter the first number: "))
num2=(input("Enter 2nd number:"))
num3=(input("Enter 3rd number:"))
if num1 >= num2 and num1 >= num3:largest = num1
elif num2 >= num1 and num2 >= num3:largest=num2
else: largest = num3
print ("The largest number is:",largest)