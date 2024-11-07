print("Welcome to calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Maltiplication")
print("4. Division")

option = int(input("Swlwct an option for Basic Calculator Operation: "))
if option == 1:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sum = num1 + num2
    print ("Addition is: " + str(sum))
elif option == 2:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sum = num1 - num2
    print ("Subtraction is: " + str(sum))
elif option == 3:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sum = num1 * num2
    print ("Maltiplication is: " + str(sum))
elif option == 4:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sum = num1 / num2
    print ("Division is: " + str(sum))
else:
    print("Invalid Operation") 
