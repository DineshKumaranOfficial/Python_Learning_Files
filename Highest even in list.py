def highest_even(numList):
  # The below one is the list comprehension in which we can perform looping and conditional statements during variable declaration itself
  temp_list = [value for value in numList if value % 2 == 0]
  highestEven = temp_list[0]
  for value in temp_list:
    if value > highestEven:
      highestEven = value
  return highestEven

print(highest_even([1,2,3,44,5,6,7,8,11]))
