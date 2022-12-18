games = ["ml", "coc", "ff", "pubg", "codm"]

# append
games.append("aov")
print(games)
# pop 
# (mirip splice sama² buat hapus suatu item dalam array)
games.pop(0)
print(games) # index ke 0 di hapus
# copy 
#;(buat ngeduplikat array)
newArray= games.copy()
print(newArray)
# count
# buat nyari item didalan array kalo ketemu di itung ada berapa item yg sama didalam klo ngga ketemu return 0
a = games.count("ml")
b = games.count("ff")
print(a) # return 0
print(b) # return 1
# extends
# ngegabungin 2 array jadi 1 kek di warisin
games.extend(newArray)
print(games)
# index
# nyari posisi item dalam array (mulai dari 0)
# return error kalo ngga ada itemnya
ml = games.index("aov")
print(ml)
# insert
# kek append cuman bisa ngatur indexnya dimana
# index mulai dari 0
games.insert(2, "hay day")
print(games)
# remove
# mirip kek pop cuman spesifik nilai nya dan yg dihapus cuman yg pertama kali di temuin kek querySelector javascript
games.remove("coc")
print(games)
# reverse
games.reverse()
print(games)
# sort
games.sort()
print(games)
# clear
# hapus semua item dalam array
games.clear()
print(games)