print("hello world")

if 5 > 2:
    print("five is greater than two")


w = 5
y = "hellow roeke"
print(type(w))

x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)