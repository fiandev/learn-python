def jumlah(a, b):
  return a + b
# function with lambda
def func(x):
  return lambda a: a * x

doubler = func(2)
print(jumlah(1, 2)) # print 3
print(doubler(11)) # print 22