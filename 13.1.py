with open("file1.txt", "r") as fo:
    data = fo.read()

with open("file2.txt", "w") as fo:
    fo.write(data)
