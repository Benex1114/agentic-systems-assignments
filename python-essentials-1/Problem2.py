try:
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    age = int(input("Enter Age: "))

    if(age<0):
        print("Age cannot be negative")
    else:
        print(f"{firstName} {lastName}")
        print(f"You will be {age+1} next year")
except:
    print("Invalid age input")

