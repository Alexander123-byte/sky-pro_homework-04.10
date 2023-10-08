from src import functions
from pprint import pprint

all_students = functions.load_students("data/students.json")
# pprint(all_students)

all_professions = functions.load_professions("data/professions.json")
# pprint(all_professions)

one_student = functions.get_student_by_pk(all_students, 1)
# pprint(one_student)

one_profession = functions.get_profession_by_title(all_professions, "backend")
# pprint(one_profession)

fitness_result = functions.check_fitness(
    one_student['skills'],
    one_profession['skills']
)
# print(fitness_result)
