from New_pupil import *
from New_subject import *
from New_grade import Add_grade
from Pupils_list import Pupils
from Grades_list import Grades
from Supplementary import *

school = {}
subject_list = ['математика', 'русский язык']
while True:
    print(f'выберите действие в школе:\n'
          f'    1.добавить ученика\n'
          f'    2.добавить предмет\n'
          f'    3.поставить оценку ученику\n'
          f'    4.вывести список учеников\n'
          f'    5.вывести список оценок ученика\n'
          f'    6.сгенерировать список учеников')
    action = input()
    if action == '1':
        Add_pupil(school, subject_list)
    elif action == '2':
        Add_subject(school, subject_list)
    elif action == '3':
        Add_grade(school)
    elif action == '4':
        Pupils(school)
    elif action == '5':
        Grades(school)
    elif action == '6':
        Occasional_generation(school, subject_list)
    else:
        break



