maplist = [{"Name": "Dinesh", "Age": 22}, {"Name": "Kumaran", "Age": 22}]
for i in range(len(maplist)):
    map = maplist[i]
    # items method takes each object in the map and convert it into a tuple
    for k, v in map.items():
        if k == "Name" and v == "Dinesh":
            print(v)
