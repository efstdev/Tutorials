number_one = float(input("Please enter a number: "))
operation = str(input("Please enter an operation to use ex; sum, sub, mult, div: "))
number_two = float(input("Please enter a second number: "))


#Check what the user wants to do with the numbers
if operation == "sum":
    calc = number_one + number_two
    print(calc)
if operation == "sub":
    calc = number_one - number_two
    print(calc)
if operation == "mult":
    calc = number_one * number_two
    print(calc)
if operation == "div":
    calc = number_one / number_two      
    print("Decimals:", calc)
    print("Rounded:", calc.__round__())

