def find_lightest_weight(weights):
    # Делю грузы на три группы
    group1 = weights[:3]
    group2 = weights[3:6]
    group3 = weights[6:]
    # Измеряю первые две группы
    if sum(group1) == sum(group2):
        #если первая и вторая группа равны, значит груз находиться в 3 группе
        lightest = min(group3)
    # Иначе если грузы не равны то самый легкий груз на чаше с меньшим весом
    else:
        lightest = group1 if sum(group1) < sum(group2) else group2

    if lightest == group1:
        if group3[0] == group3[1]:
            lightest = group3[2]

        else:
            lightest = group3[0] if group3[0] < group3[1] else group3[1]

    elif lightest == group2:
        lightest = group3[0] if group3[0] < group3[1] else group3[1]

    return lightest


weights = [10, 10, 10, 10, 10, 10, 10, 9]

lightest_weight = find_lightest_weight(weights)

print("Самый легкий груз:", lightest_weight)





