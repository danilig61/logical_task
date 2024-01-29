def find_lightest_weight(weights):
    group1 = weights[:3]   # Первая группа грузов
    group2 = weights[3:6]  # Вторая группа грузов
    group3 = weights[6:]   # Третья группа грузов

    # Измерение первых двух групп грузов
    if sum(group1) == sum(group2):
        # Если весы в равновесии, самый легкий груз в третьей группе
        lightest = min(group3)
    else:
        # Если весы неравновесны, самый легкий груз на чаше с меньшим весом
        lightest = group1 if sum(group1) < sum(group2) else group2

    # Измерение оставшихся трех грузов
    if lightest is group1:
        # Если самый легкий груз в первой группе
        if group1[0] == group1[1]:
            # Если весы в равновесии, самый легкий груз третий
            lightest = group1[2]
            index = 2
        elif group1[0] < group1[1]:
            lightest = group1[0]
            index = 0
        else:
            lightest = group1[1]
            index = 1
    elif lightest is group2:
        # Если самый легкий груз во второй группе
        if group2[0] == group2[1]:
            # Если весы в равновесии, самый легкий груз третий
            lightest = group2[2]
            index = 5
        elif group2[0] < group2[1]:
            lightest = group2[0]
            index = 3
        else:
            lightest = group2[1]
            index = 4
    else:
        # Самый легкий груз в третьей группе
        if group3[0] < group3[1]:
            lightest = group3[0]
            index = 6
        else:
            lightest = group3[1]
            index = 7

    return lightest, index

weights = [10, 10, 10, 10, 10, 9, 10, 10]

lightest_weight, index = find_lightest_weight(weights)

print("Самый легкий груз весит:", lightest_weight)
print("Индекс груза:", index)