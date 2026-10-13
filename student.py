def add_student(name, age):
    student = {
        "name": name,
        "age": age
    }
    return student


student = add_student("Ravi", 20)
print(student)