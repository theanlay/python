def myfunction(n):
    return n+10
number = (1, 2, 3, 4, 5)
result = map(myfunction, number)
print(list(result))
