def Add_pupil(organization, shedule):
    first_name = input('введите имя ученика')
    second_name = input('введите фамилию ученика')
    pupil = first_name + '_' + second_name
    temp_np = {}
    for i in shedule:
        temp_np[i] = []
    organization[pupil] = temp_np