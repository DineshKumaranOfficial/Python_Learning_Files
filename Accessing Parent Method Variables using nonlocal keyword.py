# Accessing parent methods variable in inner method using nonlocal

def outer():
  x = "Outer Local Variable"
  def inner():
    nonlocal x
    x = "Inner Local Variable"
    print("Inner : ", x)
  inner()
  print("Outer : ", x)

outer()
