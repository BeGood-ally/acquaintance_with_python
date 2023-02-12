def Grades(organization):
    first_name = input('введите имя ученика')
    second_name = input('введите фамилию ученика')
    pupil = first_name + '_' + second_name
    subject = input('введите предмет')
    try:
        if organization[pupil][subject] == []:
            print('ученик еще не имеет оценок по данному предмету')
        else:
            print(organization[pupil][subject])
    except KeyError:
        print('вы ввели несуществующего ученика либо предмет')