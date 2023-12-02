from config import names
import pandas as pd

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

def levelToNum(level):
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

def totalScore(math, read, write):
    return math + read + write

def bring():
    data = pd.read_csv('StudentsPerformance.csv')
    data["lunch"] = data["lunch"].apply(launch_to_bool)
    data["gender"] = data["gender"].apply(gender_to_bool)
    data["parental level of education"] = data["parental level of education"].apply(levelToNum)
    data["race/ethnicity"] = data["race/ethnicity"].apply(race_to_num)
    data["test preparation course"] = data["test preparation course"].apply(course_to_bool)
    data["total score"] = data['math score'] + data['reading score'] + data['writing score']
    return data[names], data['total score'], data
