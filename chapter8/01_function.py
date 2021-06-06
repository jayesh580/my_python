def percente(marks):
    # p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    p = (sum(marks)/400)*100
    return p 

marks1 = [45, 67, 55, 88]
percentage1 = percente(marks1)

marks2 = [66, 77, 88, 44]
percentage2 = percente(marks2)

print(percentage1, percentage2)