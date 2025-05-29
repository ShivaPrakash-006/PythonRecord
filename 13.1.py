try:
    filename = input("Enter source filename: ")

    with open(filename, "r") as f:
        data = f.read()

    filename = input("Enter destination filename: ")

    with open(filename, "w") as f:
        f.write(data)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error:", e)
else:
    print("Successfully Copied")
