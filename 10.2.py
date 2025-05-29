students = {
    "Alice": {"Math": 85, "Science": 90, "English": 88},
    "Bob": {"Math": 78, "Science": 74, "English": 80},
    "Charlie": {"Math": 92, "Science": 89, "English": 95},
}

for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    students[name]["Average"] = avg

top_student = max(students, key=lambda x: students[x]["Average"])
print("Top Scorer is", top_student, "with average", students[top_student]["Average"])
