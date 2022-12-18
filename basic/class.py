class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def getName(self):
    return self.name
    
person = Person("fian", 16)
del person.age # ngehapus attribute age 
print(person.getName()) # orint fian
del person # hapus object person