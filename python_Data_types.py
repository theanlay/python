x=5
print(type(x))

def strfun():
    x="Hello world"
    print(type(x))
def intfun():
    x=20
    print(type(x))
def floatfun():
    x=20.5
    print(type(x))
def complexfun():
    x=1j
    print(type(x))
def listfun():
    x=["apple","banana", "cherry"]
    print(type(x))
def tuplefun():
    x=("apple", "banna", "cherry")
    print(type(x))
def rangefun():
    x=range(6)
    print(type(x))
def dictfun():
    x={"name" : "Jonh" , "age":36}
    print(type(x))
def setfun():
    x={"apple","banana","cherry"}
    print(type(x))
def frozensetfun():
    x=({"apple","banana","cherry"})
    print(type(x))
def boolfun():
    x= True
    print(type(x))
def bytesfun():
    x=b"Hello"
    print(type(x))
def bytearrayfun():
    x=bytearray(5)
    print(type(x))
def memoryviewfun():
    x=memoryview(bytes(5))
    print(type(x))
strfun()
intfun()
floatfun()
complexfun()
listfun()
tuplefun()
rangefun()
dictfun()
setfun()
frozensetfun()
boolfun()
bytesfun()
bytearrayfun()
memoryviewfun()