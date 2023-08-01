def lw1():
    print("a")
    lw2()

def lw2():
    print("b")
    lw1()

lw1()
