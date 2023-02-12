def Add_grade(organization):
    f_name = input('введите имя ученика')
    s_name = input('введите фамилию ученика')
    learner = f_name + '_' + s_name
    subj = input('введите предмет')
    grade = input('введите оценку')
    if grade.isdecimal():
        if 0 < int(grade) < 6:
            try:
                organization[learner][subj].append(grade)
            except KeyError:
                print("вы ввели несуществующего ученика либо предмет")
        else:
            print("вы ввели оценку не соответсвующую пятибальной шкале")
    else:
        print("вы ввели не число")



