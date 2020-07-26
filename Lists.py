# Lists
list1 = [0, 1, 2, 3, 4, 5]

# Finding the length of the list
print(f"Length of the list is : {len(list1)}")

# List can be copies using the following line
# Below line passes the list 1 as a reference to list 2, So if you change the list 1 it is also reflected in list 2
list2 = list1
list1.append(6)
print("\nList Reference Copying")
print(f"List 1 : {list1}")
print(f"List 2 : {list2}")
list1.remove(6)

# To avoid the reference copy, we can copy it using the below line. It will copy all the values in list 1 to list 2
list2 = list1[:]
list1.append(6)
print("\nList Value Copying using list slicing method")
print(f"List 1 : {list1}")
print(f"List 2 : {list2}")

# Copying list using copy method
list1.pop()
list2 = list1.copy()
list1.append(6)
print("\nList Value Copying using copy method")
print(f"List 1 : {list1}")
print(f"List 2 : {list2}")

# Appends any object to the list. It may be string, int or another list
# Append can use only one argument
print("\nList Appending")
list1.append('a')
print(f"List 1 : {list1}")
list1.append(['b', 'c'])
print(f"List 1 : {list1}")

# Adding Elements in List using Insert
print("\nAdding Elements in List using Insert")
list1.insert(2, 'second_element')
print(f"List 1 : {list1}")

# Deleting list elements using Pop
# Specifying no Parameters in pop method will delete the last element from the list
print("\nRemoving Elements in List using Pop")
list1.pop()
print(f"List 1 : {list1}")

# Adding elements using extend
# Extend adds multiple elements to the list by iterating each value
print("\nList Extending")
list1.extend(['b', 'c', ['d']])
print(f"List 1 : {list1}")

# Deleting list elements using Pop
# Pop takes the index of the element as parameter
print("\nRemoving Elements in List using pop")
list1.pop(2)
print(f"List 1 : {list1}")

# Removing elements using remove method
# Remove method uses the element value as the parameter and removes it from the list
print("\nRemoving Elements in List using Remove")
list1.remove(['d'])
print(f"List 1 : {list1}")

# Finding presence of element in list using 'in' keyword
print(f"'a' present in list : {'a' in list1}")
print(f"'d' present in list : {'d' in list1}")

# Counting the element presence in list
list1.append('a')
print(f"'a' is present {list1.count('a')} times")

# Clear method clears all the elements in the list and makes it empty
print("\nClearing List")
list1.clear()
print(f"List 1 : {list1}")

# Sorting list elements using sort
print("\nSorting list elements using sort")
list2 = [4, 5, 2, 3, 1, 7, 6]
print(f"Before Sorting {list2}")
list2.sort()
print(f"After Sorting {list2}")

# Reversing list elements using reverse
list2.reverse()
print(f"After Reversing the list {list2}")

# Using Range Function to create a list
print("\nUsing Range Function to create a list")
list1 = list(range(1, 100))
print(list1)
print(
    f"\nList using only one parameter in range function : {list(range(100))}")

# Converting list to String using join
list1 = ["Hi", "I'm", "Dinesh"]
joinUsing = " "
resultString = joinUsing.join(list1)
print(f"\nConverted list to string : {resultString}")
