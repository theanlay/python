a="Hello world"
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H","J"))
print(a.split(","))
#check string
txt ="This rain in spain stays minly in the plain"
x= "rain" in txt
print(x)
#string concatenation
a="hello"
b="world"
c=a+b
print(c)
#format() method takes unlimited number of arguments, and are placed into the repesctive placeholder:
num =5
bold="my age is {}"
print(bold.format(num))

    