# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())


# name = ["david","sally","michael","annelle"]
# score = [10,8,9.5,9.5]

# nested_list = []
# combined = []
# for i in range(4):
#         for j in range(1):
#             combined.append(name[i])
#             combined.append(score[i])
#             nested_list.append(combined)


# print(nested_list[-1])

# name = ["david","sally","michael","annelle"]
# score = [10,8,9.5,9.5]

# nest_list = []

# for i in range(len(name)):
#     nest_list.append([name[i], score[i]])

# print(nest_list)

# data = [ 
#         ["Harry", 37.21], 
#         ["Berry", 37.21], 
#         ["Tina", 37.2],
#         ["Akriti", 41], 
#         ["Harsh", 39]]

# new_data = []
# highest_num = []

# for i in data:
#     highest_num.append(i[1])
# sort = sorted(highest_num)
# # print(sort[0:-1])
# print(sort[-1])
# print(sort[-2])

name = ["david","sally","michael","annelle"]
score = [10,8,9.5,9.5]

students = []

for i in range(len(name)):
    students.append([name[i],score[i]])

# print(new_list_one)

students = sorted(students, key = lambda x: x[1])
print(students)
second_lowest_score = students[1][1]
second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
desired_students = []
for stu in students:
    if stu[1] == second_lowest_score:
        desired_students.append(stu[0])
print("\n".join(sorted(desired_students)))