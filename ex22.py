def add(a, b):
    print("Adding", a + b )
    return a + b

def subtract(a, b):
    print("Subtracting ", a - b)
    return a - b

def multiply(a, b):
    print("Multiplying ", a * b)
    return a * b

def divide(a, b):
    print("Dividing ", a / b)
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print("Age: ", age, "Height :", height,"Weight", weight," IQ:", iq)


print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq))))

print("That becomes:",what ,"Can you do it by hand?")

