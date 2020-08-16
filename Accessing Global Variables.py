# Accessing global and nonlocal variables

globalvariable = 0


def printSomething():
    '''In this method we access the global variable by reference using the global keyword
    '''
    global globalvariable
    globalvariable += 1
    return globalvariable


printSomething()
printSomething()
printSomething()
print(printSomething())  #Output : 4

globalvariable2 = 0


def someMethod(globalvariable2):
    '''In this method we pass the globalvariable2 as a value to the method so the global variable value doesn't change on each function call
    '''
    globalvariable2 += 1
    return globalvariable2


someMethod(globalvariable2)
someMethod(globalvariable2)
someMethod(globalvariable2)
print(someMethod(globalvariable2))  # Output : 1


