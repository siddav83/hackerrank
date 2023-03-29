# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())


name = ["david","sally","michael","annelle"]
score = [10,8,9.5,9.5]

nested_list = []
combined = []
for i in range(1):
    combined.append(name[i])
    combined.append(score[i])
    nested_list.append(combined)


print(nested_list)