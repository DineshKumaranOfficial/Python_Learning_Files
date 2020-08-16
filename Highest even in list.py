def highest_even(numList):
  # The below one is the list comprehension in which we can perform looping and conditional statements during variable declaration itself
  evens = [value for value in numList if value % 2 == 0]
  return max(evens)

print(highest_even([1,2,3,44,5,6,7,8,11]))
