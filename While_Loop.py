my_list = ['a', 'b', 'c', 'd']
i = 0
list_length = len(my_list)
while i < list_length:
    print(my_list[i])
    i += 1
else:
    print("Out of the List")


while True:
    response = input("Loop will run until you say bye : ")
    if response == "bye":
        break
    if str(response).lower() == "hi":
        print("Good....!")
