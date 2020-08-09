list1 = ['a', 'b', 'c', 'b', 'd', 1, 2, 3, 4, 1, 3, 5, 2]
resultList = []
for element in list1:
    if list1.count(element) > 1 and element not in resultList:
        resultList.append(element)
print(resultList)
