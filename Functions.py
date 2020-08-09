# Simple funtion
print("\nSimple funtion")


def printMessage():
    print("hello")


printMessage()


# Function with positional parameters
print("\nFunction with positional parameters")


def printMessageWithArgs(name, emoji):
    print(f"Hi {name} {emoji}")


printMessageWithArgs("Dinesh", "B-)")


# Function with named parameters
# Named parameters don't expect the arguments to be in order
print("\nFunction with named parameters")


def sayHello(name, age):
    print(f"Hi {name}, You are {age} years old.")


sayHello(age=22, name="Dinesh")


# Function with default parameters
print("\nFunction with default parameters")


def giveIntro(name="Dinesh", age=22):
    print(f"Hi {name}, You are {age} years old.")


giveIntro("Kumaran", 22)
giveIntro("Hare")
giveIntro()


# Function with return type
def add(num1, num2):
    sum = num1 + num2
    return sum


sum = add(4, 4)
print(sum)


# Function that does nothing
# pass can be used as a placeholder for defining something later
def nothing():
    pass


print(nothing())
