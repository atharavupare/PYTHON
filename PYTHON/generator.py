def simpleGenerator(): # it is a generator class not a function
  print("Entry")
  yield 1 #as soon as a yield statement is written in a function it becomes a generator class
  print(1)
  yield 2
  print(2)
  yield 3
  print(3)
  yield 4
  print(4)
  yield 5,6

x = simpleGenerator() #created object of class generator
print("Type of x: ",type(x))
for val in x:
  print(val)

# OUTPUT
# Type of x:  <class 'generator'>
# Entry
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 4
# (5, 6)
