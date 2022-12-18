items = ["apel", "mangga", "strawberry", "pisang", "nanas"]
# length of items
print(len(items)) # print 5
# mirip foreach
for x in items:
  if x == "pisang":
    print(x, "ditemukan!")
    break
  else:
    print(x)
else:
  print("loop ended")