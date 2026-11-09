try:
    code=input("Enter code: ")

    if len(code)<2:
        raise ValueError("Invalid code")

    age = input("Enter age: ")
    for symbol in age:
        if ord(symbol) not in range(ord(0), ord(9)+1):
            raise ValueError("You can't vote! ")
    age=int(age)
    if age<0 or age>150:
         raise ValueError("Invalid age.It has to be between 0-150!")
    else:
        print("You can vote")
except ValueError as error:
    print(error)
except Exception as err:
    print(err)
else:
    if age<18:
        print("You can't vote, too young!")
    else:
        print("You can vote")