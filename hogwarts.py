students = [
    {"name":"Rahull", "house":"Bihar", "language": "Hindi"},
    {"name":"mayo", "house":"manipur", "language": "Thanghul"},
    {"name":"Ayush", "house":"Ambala", "language": "none"}
]

for student in students:
    print(student["name"], student["house"], student["language"], sep="-")