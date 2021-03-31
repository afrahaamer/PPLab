def printinfo(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print (var)
    return

printinfo(10)
printinfo(30,40,50)