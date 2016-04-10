def printnumber():
    for x in range(1,10000):
        if x%3 == 0 and x%5 == 0:
            print("fizfuz")
        if x%3 == 0:
            print("fiz")
        if x%5 == 0:
            print("fuz")
        else:
            print(x)
            
printnumber()