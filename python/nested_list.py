

    combinedstu = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        combinedstu.append([name, score])

    combinedstu = sorted(combinedstu, key = lambda x: x[1])
    #print(combinedstu)
    #second_lowest_score = combinedstu[1][1]
    second_lowest_score = sorted(list(set([x[1] for x in combinedstu])))[1]
    desired_students = []
    for stu in combinedstu:
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))





