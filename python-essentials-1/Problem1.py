try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Sum:", num1+num2)    

    if(num2==0):
        print("Cannot divide by 0")
    else:
        print("Division Result:", num1/num2)
except:
    #Printing invalid input for everything except integers
    print("Invalid input")