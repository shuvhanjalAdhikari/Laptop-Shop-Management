def read():
    with open("Laptop.txt",'r') as file:
        laptop_ID = 1
        contents = {}
        for line in file:
            line = line.replace("\n","")
            contents[laptop_ID] = line.split(",")
            laptop_ID += 1
    #print(contents)
    return contents
