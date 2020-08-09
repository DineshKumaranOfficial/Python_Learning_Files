# List Unpacking
a, b, c, *d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{a}\n{b}\n{c}\n{d}\n{e}")

# Enumerate method returns index and the value at the index
for i in enumerate(d):
    print(i)
