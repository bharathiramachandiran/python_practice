with open("notes.txt") as f:
    data = f.read()
    print(data)
data += "\nBharat"
with open("notes.txt", 'w') as f:
    f.write(data)
