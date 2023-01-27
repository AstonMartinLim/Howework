#1
python = {'ivanov','petrov','sidorov','trofimov'}
java = {'moxov','goroxov','ivanov'}
fullstack = {'konovalov','sergeev','trofimov'}
frontend = {'konovalov', 'gordeev', 'sidorenko'}
groups = [python,java, fullstack, frontend]

def find_active_students(groups):
    active_students = set()
    for num, group in enumerate(groups):
        for other in groups[num+1:]:
            active_students.update(group & other)
    return active_students

print(find_active_students(groups))
back_students = python | java
front_students = fullstack | frontend
print(back_students - front_students)
print(back_students | frontend)
