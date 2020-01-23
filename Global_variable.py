x="awsome"
def myfunc():
    print("python is " + x)
myfunc()

y="awsome"
def newfunc():
    y="fantastic"
    print("python is " + y)
newfunc()
print("python is " + y)

def dobfun():
    global h
    h="fantastic"
dobfun()
print("python is " + h)