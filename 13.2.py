try:
    filename = input("Enter filename: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

    print("Total Lines:", line_count)
    print("Total Words:", word_count)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error:", e)
