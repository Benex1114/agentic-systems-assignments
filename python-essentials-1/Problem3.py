def age_checker(age):
    if(age<13):
        print("You are a Child")
    elif(13<=age<=17):
        print("You are a Teenager")
    elif(18<=age<=59):
        print("You are an Adult")
    else:
        print("You are a Senior Citizen")
        

try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    print(f"Hello {name}")
    age_checker(age)
    if(age>=18):
        print("You are eligible to vote")
    else:
        print("You are Not eligible to vote")

except:
    print("Invalid age input")