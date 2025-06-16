import numpy as np

# Grade Classification

#Assign grades based on marks using NumPy conditions.

marks = np.array([88,76,59,92,67])
grades = np.where(marks >= 90, 'A',
         np.where(marks >=75, 'B',
         np.where(marks >=60, 'C','D')))

print("Grandes:",grades)


#Calendar Day Mapper
#Generate a sequence of 30 days and tag weekdays/weekends.


days = np.arange(1,31)
tags = np.where((days % 7 == 6) | (days % 7 == 0), "Weekend", "Weekday")
print(list(zip(days,tags)))


#Loan EMI Calculator
#Calculate monthly EMI using NumPy formula.

p = 100000
R =0.01
N = 12
emi = p * R * (1 + R)**N / ((1 + R)**N - 1)
print("Monthly EMI: $", round(emi,2))

#Matrix Transpose and Determinant
#Generate a random 3x3 matrix.
#Find its transpose and determinant

matrix = np.random.randint(1,10, (3,3))
transpose = matrix.T
det = np.linalg.det(matrix)

print("Matrix:\n",matrix)
print("Transpose:\n",transpose)
print("Daterminant:",round(det,2))


#Weather Data – Hot/Cold Days
#Given daily temperatures, count how many days were hot (>30°C) and cold (<20°C).

temps = np.random.randint(15,40,30)
hot_days = np.sum(temps > 30)
cold_days = np.sum(temps < 20)

print("Hot days:",hot_days)
print("cold days:",cold_days)

# Percentage Calculator for Exam Scores
#Given marks and total marks, calculate percentage.

marks_obtained = np.array([45,78,82,66])
total_marks = np.array([50,100,100,80])
percentage = (marks_obtained / total_marks) * 100
print("Percentages:",percentage)
                                                                         