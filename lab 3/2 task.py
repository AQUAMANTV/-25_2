def find_common_participants(group1, group2, delimiter=','):

    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)


    common = set(list1) & set(list2)


    return sorted(list(common))



participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники (запятая):", common_participants)


participants_first_group_pipe = "Иванов|Петров|Сидоров"
participants_second_group_pipe = "Петров|Сидоров|Смирнов"

common_participants_pipe = find_common_participants(participants_first_group_pipe, participants_second_group_pipe,
                                                    delimiter='|')
print("Общие участники (вертикальная черта):", common_participants_pipe)