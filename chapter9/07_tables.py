# for i in range(2, 21):
#     with open(f"D:\python\chapter9\table_of_multiplication_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j} = {i*j}")
#             if j!=10:
#                 f.write('\n')

for i in range(2, 21):
    # with open(f"D:\python\chapter9\table_of_multiplication_of_{i}.txt", 'w') as f:
    with open(f"D:\python\chapter9\Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')