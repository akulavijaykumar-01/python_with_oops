try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))

    result = a / b
    print(result)

except ZeroDivisionError:
    print("Division not handled")

else:
    print("Result:", result)