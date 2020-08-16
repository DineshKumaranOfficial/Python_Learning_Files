# *args and **keywordargs or **kwargs
# *args support multiple arguments for the function and same as **kwargs support mulitple keyword arguments
# *args has the arguments in a form of tuple while **kwargs has them in the form of dictionary
def total(name, *num, msg='Hi', **anotherNum):
    total = 0
    print(num, anotherNum)
    for items in anotherNum.values():
        total += items
    return sum(num) + total


print(total(1, 2, 3, 4, 5, num1=5, num2=10))
