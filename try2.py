try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))

    result = a / b

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Division not handled")

else:
    print(result)

finally:
    print("Code over: Division of numbers")