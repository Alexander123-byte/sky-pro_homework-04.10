# Импортируем файл с функциями из папки src
from src import functions

# Загружаем списки словарей из файлов
all_students = functions.load_students("data/students.json")
all_professions = functions.load_professions("data/professions.json")


# Создаем функцию
def main():
    if len(all_students) == 0 or len(all_professions) == 0: # если файл пустой, выводим сообщение
        print("Один из файлов пустой или отсутствует. Проверьте данные")
        return

    # Запрашиваем номер студента
    print("Введите номер студента")
    student_pk = int(input())
    # Полученное значение подставляем в функцию, предварительно сохранив в переменную
    student = functions.get_student_by_pk(all_students, student_pk)

    # Если студент не нашелся, выводим сообщение
    if student is None:
        print("У нас нет такого студента")
        return

    # Если такой студент есть, запрашиваем его имя и специальность из файла и выводим
    student_name, student_skills = student['full_name'], student['skills']
    print(f"Студент {student_name}\nЗнает {', '.join(student_skills)}")

    # Все то же самое со специальностью
    print(f"Выберите специальность для оценки студента {student_name}")
    profession_title = input()
    profession = functions.get_profession_by_title(all_professions, profession_title)

    if profession is None:
        print("У нас нет такой специальности")
        return

    profession_skills = profession['skills']
    student_fitness = functions.check_fitness(student_skills, profession_skills)

    # В конце выводим статистику
    print(f"Пригодность {student_fitness['fit_percent']}%")
    print(f"{student_name} знает {', '.join(student_fitness['has'])}")
    print(f"{student_name} не знает {', '.join(student_fitness['lacks'])}")

# Запускаем функцию
main()
