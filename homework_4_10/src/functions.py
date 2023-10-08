import json


def load_students(path):
    """Загружает список студентов из файла"""
    with open(path, "r", encoding='utf-8') as json_file_students:
        data_students = json.load(json_file_students)
        return data_students


def load_professions(path):
    """Загружает список профессий из файла"""
    with open(path, "r", encoding='utf-8') as json_file_professions:
        data_profession = json.load(json_file_professions)
        return data_profession


def get_student_by_pk(all_student, pk):
    """Получает словарь с данными студента по его pk"""
    for one_student in all_student:
        if one_student['pk'] == pk:
            return one_student


def get_profession_by_title(all_profession, title):
    """Получает словарь с инфо о профе по названию"""
    title = title.lower()
    for one_profession in all_profession:
        if one_profession['title'].lower() == title:
            return one_profession


def check_fitness(student_skills, profession_skills):
    """Проверяет соответствие навыков и возвращает словарь типа:

    {
        "has": ["Python", "Linux"],
        "lacks": ["Docker", "SQL"],
        "fit_percent": 50
    }
    """

    # Конвертируем 2 словаря в множество
    set_student_skill = set(student_skills)
    set_profession_skill = set(profession_skills)

    # Получаем 2 пересечения на то, какие специальности нашлись и какие не нашлись
    has = set_profession_skill.intersection(set_student_skill)
    lacks = set_profession_skill.difference(set_student_skill)

    # Считаем процент
    fit_percent = len(has) / len(set_profession_skill) * 100

    # Возвращаем результат в виде списка
    return {
        "has": list(has),
        "lacks": list(lacks),
        "fit_percent": round(fit_percent)
    }
