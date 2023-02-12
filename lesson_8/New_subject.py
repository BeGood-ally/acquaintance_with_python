def Add_subject(organization, shedule):
    subject = input("введите новый предмет")
    for i in organization:
        organization[i][subject] = []
    shedule.append(subject)