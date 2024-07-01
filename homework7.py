grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
sorted_students = sorted(list(students))
average_grade = [sum(grades[0])/len(grades[0]),
                 sum(grades[1])/len(grades[1]),
                 sum(grades[2])/len(grades[2]),
                 sum(grades[3])/len(grades[3])]
grades_sict = dict(zip(sorted_students, average_grade))
print(grades_sict)
#average_score1 = students['Johnny'], grades[0][0:5]
#average_score_Aaron = ((sum(grades[0][0:5])) / 5)
#print(average_score_Aaron)
#average_score_Bilbo = ((sum(grades[1][0:4])) / 4)
#print(average_score_Bilbo)
#average_score_Johnny = ((sum(grades[2][0:4])) / 4)
#print(average_score_Johnny)
#average_score_Khendrik = ((sum(grades[3][0:3])) / 3)
#print(average_score_Khendrik)
#average_score_Steve = ((sum(grades[4][0:5])) / 5)
#print(average_score_Steve)
#result_ = {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
#print(result_)

# то что загнал в коменты - первая попытка решить задание , вторая получилась после того как решил,
# что в первой не достаточно всё автоматизировано по сути в ручную посчитал ) но решил оставить этот позор =)