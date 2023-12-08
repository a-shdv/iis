import pandas as pd

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()


def gender_to_bool(gender):
    if gender == "male":
        return 1
    return 0


def race_to_num(race):
    if race == "group A":
        return 0
    elif race == "group B":
        return 1
    elif race == "group C":
        return 2
    return 3


def launch_to_bool(lunch):
    if lunch == "standard":
        return 1
    return 0


def course_to_bool(course):
    if course == "completed":
        return 1
    return 0


def level_to_num(level):
    if level == "associate's degree":
        return 0
    elif level == "bachelor's degree":
        return 1
    elif level == "master's degree":
        return 2
    elif level == "some college":
        return 3
    elif level == "high school":
        return 4
    return 5


def total_score(math, read, write):
    return math + read + write


def convert_all_to_num():
    data = pd.read_csv('students-performance.csv')
    data["lunch"] = data["lunch"].apply(launch_to_bool)
    data["gender"] = data["gender"].apply(gender_to_bool)
    data["parental level of education"] = data["parental level of education"].apply(level_to_num)
    data["race/ethnicity"] = data["race/ethnicity"].apply(race_to_num)
    data["test preparation course"] = data["test preparation course"].apply(course_to_bool)
    data["total score"] = data['math score'] + data['reading score'] + data['writing score']

    # Вычисляем стандартное отклонение
    std_dev = data['total score'].std()

    # Определяем границы для выбросов (например, 3 стандартных отклонения от среднего)
    lower_bound = data['total score'].mean() - 1.5 * std_dev
    upper_bound = data['total score'].mean() + 1.5 * std_dev

    # Фильтруем данные, исключая выбросы
    filtered_data = data[(data['total score'] >= lower_bound) & (data['total score'] <= upper_bound)]

    return filtered_data[
        ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]], \
        filtered_data['total score'], filtered_data
